#!/usr/bin/env bash
# Nightly sync of LIS 467 course folder to Google Drive (ExpanDrive)
SRC="/home/kameroncole/VSCode/simmons/467/"
DEST="/home/kameroncole/ExpanDrive/GD-Simmons/LIS-467-OL01/"
LOG="/home/kameroncole/VSCode/simmons/467/.sync_gdrive.log"

echo "=== $(date '+%Y-%m-%d %H:%M:%S') sync start ===" >> "$LOG"

if [ ! -d "$DEST" ]; then
    echo "ERROR: destination $DEST not available (ExpanDrive not mounted?)" >> "$LOG"
    exit 1
fi

rsync -av --exclude '.git' --exclude '.sync_gdrive.log' "$SRC" "$DEST" >> "$LOG" 2>&1
echo "=== $(date '+%Y-%m-%d %H:%M:%S') sync done (exit $?) ===" >> "$LOG"
