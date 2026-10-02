%% BUILD_EMBEDDINGS_DEMO
% Demonstrates, from scratch using only core MATLAB (no toolboxes), how a
% high-dimensional "semantic vector space" is built from text documents,
% then searched with cosine similarity -- the same two ideas used by the
% Node.js embeddings.js / vectorStore.js files in this project, just made
% fully transparent step-by-step.
%
% Pipeline:
%   1. Load the same documents.json used by the Node.js demo
%   2. Tokenize text and build a vocabulary -> defines the vector space axes
%   3. Build a term-frequency ("bag of words") matrix: one high-dimensional
%      vector per document, one dimension per vocabulary word
%   4. Apply TF-IDF weighting so common words count less than distinctive ones
%   5. Reduce dimensionality with SVD (same math behind PCA) so the space
%      can be *visualized* in 2D/3D
%   6. Embed a query the same way, rank documents by cosine similarity
%
% Run with:  >> build_embeddings_demo

clear; clc; close all;

%% 1. Load documents (same dataset as the Node.js demo)
jsonPath = fullfile(fileparts(mfilename('fullpath')), '..', 'data', 'documents.json');
raw = jsondecode(fileread(jsonPath));
numDocs = numel(raw);

titles     = strings(numDocs, 1);
categories = strings(numDocs, 1);
bodies     = strings(numDocs, 1);
for i = 1:numDocs
    titles(i)     = string(raw(i).title);
    categories(i) = string(raw(i).category);
    bodies(i)     = string(raw(i).title) + ". " + string(raw(i).text);
end

fprintf('Loaded %d documents from documents.json\n', numDocs);

%% 2. Tokenize and build the vocabulary (the axes of the vector space)
tokensPerDoc = cell(numDocs, 1);
vocab = containers.Map('KeyType', 'char', 'ValueType', 'double');

for i = 1:numDocs
    tokens = tokenize(bodies(i));
    tokensPerDoc{i} = tokens;
    for t = 1:numel(tokens)
        if ~isKey(vocab, tokens{t})
            vocab(tokens{t}) = vocab.Count + 1; %#ok<NASGU>
        end
    end
end

vocabWords = keys(vocab);
vocabSize  = numel(vocabWords);
fprintf('Vocabulary size (vector space dimensionality): %d\n', vocabSize);

%% 3. Build the term-frequency matrix -> one row per document, one high-
%     dimensional vector per document, living in R^vocabSize
tf = zeros(numDocs, vocabSize);
for i = 1:numDocs
    tokens = tokensPerDoc{i};
    for t = 1:numel(tokens)
        col = vocab(tokens{t});
        tf(i, col) = tf(i, col) + 1;
    end
end

%% 4. TF-IDF weighting: downweight words that appear in almost every
%     document (e.g. "the", "and") and upweight distinctive words
docFreq = sum(tf > 0, 1);                     % how many docs contain each word
idf = log((numDocs + 1) ./ (docFreq + 1)) + 1; % smoothed inverse document freq
tfidf = tf .* idf;

% L2-normalize each document vector to unit length, exactly like
% normalize: true in embeddings.js -- this makes cosine similarity equal
% to a plain dot product later on.
docVectors = tfidf ./ vecnorm(tfidf, 2, 2);

fprintf('Built %d document embeddings, each with %d dimensions.\n', ...
    size(docVectors, 1), size(docVectors, 2));

%% 5. Dimensionality reduction (SVD / PCA) purely so we can *see* the space
%     The full vocabSize-dimension space can't be plotted directly, but its
%     dominant structure can be visualized in 2D/3D.
centered = docVectors - mean(docVectors, 1);
[~, S, V] = svd(centered, 'econ');
explainedVar = (diag(S).^2) / sum(diag(S).^2) * 100;

numComponents = min(3, size(V, 2));
projected = centered * V(:, 1:numComponents);

fprintf('Top %d components explain %.1f%% of variance.\n', ...
    numComponents, sum(explainedVar(1:numComponents)));

figure('Name', 'Semantic Vector Space (reduced to 2D)', 'Color', 'w');
uniqueCats = unique(categories);
colors = lines(numel(uniqueCats));
hold on;
for c = 1:numel(uniqueCats)
    mask = categories == uniqueCats(c);
    scatter(projected(mask, 1), projected(mask, 2), 80, colors(c, :), 'filled', ...
        'DisplayName', uniqueCats(c));
end
text(projected(:,1) + 0.01, projected(:,2), titles, 'FontSize', 7, 'Interpreter', 'none');
xlabel('Component 1'); ylabel('Component 2');
title('Document embeddings projected into 2D (SVD of TF-IDF vectors)');
legend('Location', 'bestoutside');
grid on; hold off;

saveas(gcf, fullfile(fileparts(mfilename('fullpath')), 'vector_space_plot.png'));

%% 6. Embed a query the same way and rank documents by cosine similarity
query = "computers that learn from data";
fprintf('\nQuery: "%s"\n', query);

queryTokens = tokenize(query);
queryVec = zeros(1, vocabSize);
for t = 1:numel(queryTokens)
    if isKey(vocab, queryTokens{t})
        col = vocab(queryTokens{t});
        queryVec(col) = queryVec(col) + 1;
    end
end
queryVec = queryVec .* idf;
norm_q = norm(queryVec);
if norm_q > 0
    queryVec = queryVec / norm_q;
end

% Cosine similarity == dot product, since every vector is unit-normalized
% (same shortcut used in src/vectorStore.js).
scores = docVectors * queryVec';

[sortedScores, order] = sort(scores, 'descend');
fprintf('\nTop matches (cosine similarity):\n');
topN = 5;
for k = 1:topN
    idx = order(k);
    fprintf('  %.3f  [%s] %s\n', sortedScores(k), categories(idx), titles(idx));
end

%% ---- Helper function ----
function tokens = tokenize(txt)
    % Lowercase, strip punctuation, split on whitespace, drop empties.
    lowered = lower(char(txt));
    cleaned = regexprep(lowered, '[^a-z0-9\s]', ' ');
    parts = strsplit(cleaned);
    tokens = parts(~cellfun('isempty', parts));
end
