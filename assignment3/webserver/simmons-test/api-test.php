<?php
// Tests whether this server can reach the Anthropic API over HTTPS.
// Does NOT make a real API call and does NOT need a key.
// Delete this file when you are done testing.
header('Content-Type: text/plain; charset=utf-8');

echo "=== PHP outbound HTTPS test ===\n";
echo "PHP: " . PHP_VERSION . "\n";
echo "OS: " . php_uname('s') . " " . php_uname('r') . "\n\n";

// 1. Check whether the curl extension is loaded.
if (!function_exists('curl_init')) {
    echo "FAIL: curl extension not loaded. PHP cannot make outbound HTTP calls without it.\n";
    exit;
}
echo "PASS: curl extension loaded (curl_version " . curl_version()['version'] . ")\n";

// 2. Try a plain HTTPS GET to example.com (proves SSL works at all).
echo "\n--- Probe 1: HTTPS to example.com ---\n";
probe("https://example.com", 200);

// 3. Try a HEAD request to api.anthropic.com (proves routing to the API host).
echo "\n--- Probe 2: HTTPS to api.anthropic.com ---\n";
$r = probe("https://api.anthropic.com", [200, 404, 401, 403, 405]);

// 4. Try the actual messages endpoint (expects 401 Unauthorized without a key — that is OK).
echo "\n--- Probe 3: POST to api.anthropic.com/v1/messages (no key, expects 401) ---\n";
$ch = curl_init("https://api.anthropic.com/v1/messages");
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT        => 15,
    CURLOPT_POST           => true,
    CURLOPT_POSTFIELDS     => '{}',
    CURLOPT_HTTPHEADER     => [
        'Content-Type: application/json',
        'x-api-key: test',
        'anthropic-version: 2023-06-01',
    ],
    CURLOPT_SSL_VERIFYPEER => true,
    CURLOPT_SSL_VERIFYHOST => 2,
]);
$body  = curl_exec($ch);
$code  = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err   = curl_error($ch);
curl_close($ch);
if ($err) {
    echo "FAIL: curl error: $err\n";
    echo "      → PHP cannot reach api.anthropic.com. API calls will not work from this server.\n";
} elseif ($code === 401) {
    echo "PASS: HTTP $code — server can reach api.anthropic.com and the API is responding.\n";
    echo "      → A real API key will work here.\n";
} else {
    echo "NOTE: HTTP $code (expected 401). Body: " . substr($body, 0, 200) . "\n";
}

function probe(string $url, $accept): bool {
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT        => 15,
        CURLOPT_NOBODY         => true,
        CURLOPT_SSL_VERIFYPEER => true,
        CURLOPT_SSL_VERIFYHOST => 2,
    ]);
    $body  = curl_exec($ch);
    $code  = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $err   = curl_error($ch);
    curl_close($ch);
    $accept = (array)$accept;
    if ($err) {
        echo "FAIL: curl error: $err\n";
        return false;
    }
    if (in_array($code, $accept, true)) {
        echo "PASS: HTTP $code from $url\n";
        return true;
    }
    echo "NOTE: HTTP $code from $url (accepted: " . implode(', ', $accept) . ")\n";
    return false;
}
