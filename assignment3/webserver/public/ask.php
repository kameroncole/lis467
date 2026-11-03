<?php
/**
 * ask.php — RAG endpoint for the MOS educator portal search.
 *
 * Accepts POST JSON: { "query": "...", "persona": "students"|"parents"|"educators" }
 * Returns JSON:      { "answer": "...", "results": [ {id, title, category, type, url, score}, ... ] }
 *
 * The Anthropic API key is read from ~/.anthropic_key (one level above public_html).
 * The vector index is read from ../data/index.json relative to this file.
 * Nothing sensitive is exposed to the browser.
 */

header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') { http_response_code(204); exit; }

// --- Config -----------------------------------------------------------
define('KEY_FILE',   $_SERVER['HOME'] . '/.anthropic_key');
define('INDEX_FILE', __DIR__ . '/../data/index.json');
define('MODEL',      'claude-haiku-4-5-20251001');
define('TOP_K',      6);
define('MAX_TOKENS', 350);

// --- Persona filter: which document types each persona sees -----------
const PERSONA_TYPES = [
    'students'  => ['exhibit', 'yes-unit', 'yes-overview'],
    'parents'   => ['exhibit'],
    'educators' => null,   // null = all types
];

// --- Helpers ----------------------------------------------------------
function json_error(int $code, string $msg): void {
    http_response_code($code);
    echo json_encode(['error' => $msg]);
    exit;
}

// --- Parse request ----------------------------------------------------
$raw = file_get_contents('php://input');
$req = json_decode($raw, true);
$query   = trim($req['query']   ?? '');
$persona = strtolower(trim($req['persona'] ?? 'educators'));
if ($query === '') json_error(400, 'Missing query');
if (!array_key_exists($persona, PERSONA_TYPES)) $persona = 'educators';

// --- Load API key -----------------------------------------------------
if (!file_exists(KEY_FILE)) json_error(500, 'API key file not found');
$key = trim(file_get_contents(KEY_FILE));
if ($key === '' || !str_starts_with($key, 'sk-')) json_error(500, 'API key appears invalid');

// --- Load index -------------------------------------------------------
if (!file_exists(INDEX_FILE)) json_error(500, 'Vector index not found — run npm run build-index first');
$docs = json_decode(file_get_contents(INDEX_FILE), true);

// --- Keyword retrieval (PHP, no external embedding needed) ------------
// The index.json vectors were built with Node/MiniLM. PHP can't run
// the same model, so we use TF keyword matching as the retrieval step
// and let Claude handle the semantic understanding in the answer.
$allowed = PERSONA_TYPES[$persona];
$terms   = array_filter(preg_split('/\W+/u', strtolower($query)));
$scored  = [];
foreach ($docs as $doc) {
    if ($allowed !== null && !in_array($doc['type'], $allowed, true)) continue;
    $hay  = strtolower($doc['title'] . ' ' . $doc['category'] . ' ' . $doc['text']);
    $hits = 0;
    foreach ($terms as $t) {
        if (strlen($t) > 2 && str_contains($hay, $t)) $hits++;
    }
    if ($hits > 0) $scored[] = ['doc' => $doc, 'score' => $hits / count($terms)];
}
usort($scored, fn($a, $b) => $b['score'] <=> $a['score']);
$top = array_slice($scored, 0, TOP_K);

// Fallback: if no keyword hits, return first TOP_K allowed docs
if (empty($top)) {
    foreach ($docs as $doc) {
        if ($allowed !== null && !in_array($doc['type'], $allowed, true)) continue;
        $top[] = ['doc' => $doc, 'score' => 0];
        if (count($top) >= TOP_K) break;
    }
}

// --- Build context for Claude -----------------------------------------
$context = '';
foreach ($top as $i => $item) {
    $d = $item['doc'];
    $context .= ($i + 1) . ". [{$d['type']}] {$d['title']} ({$d['category']})\n";
    $context .= "   " . substr($d['text'], 0, 400) . "\n";
    $context .= "   Link: {$d['url']}\n\n";
}

$system = <<<SYSTEM
You are a helpful assistant for the Museum of Science, Boston educator portal.
A user has asked a question. You have been given a list of relevant resources
from our index (YES curriculum units, museum exhibits, Massachusetts STE standards,
and curated STEM research documents). Answer the user's question in 2-4 sentences,
citing only the provided resources by their title. Be specific and practical.
End with a one-sentence suggestion for how to explore further on the portal.
Do not invent resources not listed below.
SYSTEM;

$user_msg = "Persona: $persona\nQuery: $query\n\nRelevant resources:\n$context";

// --- Call Claude ------------------------------------------------------
$payload = json_encode([
    'model'      => MODEL,
    'max_tokens' => MAX_TOKENS,
    'system'     => $system,
    'messages'   => [['role' => 'user', 'content' => $user_msg]],
]);

$ch = curl_init('https://api.anthropic.com/v1/messages');
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT        => 30,
    CURLOPT_POST           => true,
    CURLOPT_POSTFIELDS     => $payload,
    CURLOPT_HTTPHEADER     => [
        'Content-Type: application/json',
        'x-api-key: ' . $key,
        'anthropic-version: 2023-06-01',
    ],
    CURLOPT_SSL_VERIFYPEER => true,
    CURLOPT_SSL_VERIFYHOST => 2,
]);
$resp   = curl_exec($ch);
$status = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err    = curl_error($ch);
curl_close($ch);

if ($err || $status !== 200) {
    $answer = '(AI answer unavailable — ' . ($err ?: "HTTP $status") . ')';
} else {
    $data   = json_decode($resp, true);
    $answer = $data['content'][0]['text'] ?? '(No response text)';
}

// --- Return response --------------------------------------------------
echo json_encode([
    'answer'  => $answer,
    'persona' => $persona,
    'results' => array_map(fn($item) => [
        'id'       => $item['doc']['id'],
        'title'    => $item['doc']['title'],
        'category' => $item['doc']['category'],
        'type'     => $item['doc']['type'],
        'url'      => $item['doc']['url'],
        'score'    => round($item['score'], 3),
        'snippet'  => substr($item['doc']['text'], 0, 200),
    ], $top),
], JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
