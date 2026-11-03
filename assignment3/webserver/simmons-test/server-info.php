<?php
// Optional: reports PHP version and whether Node.js is installed on this server.
// Runs only the fixed commands below. Delete this file when you are done testing.
header('Content-Type: text/plain; charset=utf-8');
echo "PHP version: " . PHP_VERSION . "\n";
echo "Server software: " . ($_SERVER['SERVER_SOFTWARE'] ?? 'unknown') . "\n";

$disabled = array_map('trim', explode(',', (string) ini_get('disable_functions')));
if (!function_exists('shell_exec') || in_array('shell_exec', $disabled, true)) {
    echo "shell_exec: disabled, so Node.js cannot be detected from PHP.\n";
    exit;
}
foreach (['node -v', 'npm -v'] as $cmd) {
    $out = trim((string) shell_exec($cmd . ' 2>&1'));
    echo $cmd . ': ' . ($out !== '' ? $out : '(no output)') . "\n";
}
