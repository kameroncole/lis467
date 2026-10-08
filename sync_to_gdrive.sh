#!/usr/bin/env bash
# Sync LIS 467 with Google Drive (colek@simmons.edu).
#  1. PULL  467-Museum-of-Science-Project from Drive via rclone ("simmons:" remote);
#     native Google Docs are exported as .docx/.xlsx/.pptx. Newer local files are kept.
#  2. PUSH  everything else in this folder to Drive via the ExpanDrive mount.
BASE="/home/kameroncole/VSCode/simmons/467"
DEST="/home/kameroncole/ExpanDrive/GD-Simmons/LIS-467-OL01/"
LOG="$BASE/.sync_gdrive.log"

echo "=== $(date '+%Y-%m-%d %H:%M:%S') sync start ===" >> "$LOG"

mkdir -p "$BASE/467-Museum-of-Science-Project"
rclone copy simmons: "$BASE/467-Museum-of-Science-Project" \
    --update --drive-export-formats docx,xlsx,pptx -v >> "$LOG" 2>&1
echo "rclone pull exit $?" >> "$LOG"

if [ ! -d "$DEST" ]; then
    echo "ERROR: destination $DEST not available (ExpanDrive not mounted?)" >> "$LOG"
    exit 1
fi

# The Museum folder is excluded from the push: it lives natively in Drive as Google Docs.
rsync -rt --no-perms --no-owner --no-group \
    --exclude '.git' --exclude '.sync_gdrive.log' --exclude '467-Museum-of-Science-Project' \
    "$BASE/" "$DEST" >> "$LOG" 2>&1
echo "=== $(date '+%Y-%m-%d %H:%M:%S') sync done (rsync exit $?) ===" >> "$LOG"
