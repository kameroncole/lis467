# Linux steps for Assignment 3 (do these first tomorrow)

Goal: get the pages built on the Linux machine (`index.html`, `search-results.html`, two CSS files, subfolders)
into the GitHub repo so the Mac session can wire them to the vector search.

Repo: https://github.com/kameroncole/lis467.git (branch `master`)

## 1. Find the repo folder and check the remote
```
cd <the folder where you built the pages>
git rev-parse --show-toplevel      # shows the repo root; if this fails, the folder is not a git repo
git remote -v                      # should be https://github.com/kameroncole/lis467.git
git branch -vv
git status
git log --oneline -5
```
- Not a git repo, or the remote is something else: copy the pages into a fresh clone (step 2) instead of fixing it.
- Files not listed by `git status`: check `git check-ignore -v index.html search-results.html` (a .gitignore may exclude them).

## 2. If you need a fresh clone
```
git clone https://github.com/kameroncole/lis467.git ~/lis467
```
Copy the pages into `~/lis467/assignment3/` (keep the subfolders, for example `css/`, `js/`, `images/`), then continue below from `~/lis467`.

## 3. Pull the Mac work (do this before committing, so nothing conflicts)
```
cd ~/lis467        # or your repo folder
git pull origin master
```
This brings in `assignment3/webserver/` (documents.json, build scripts, `simmons-test/`) and `.github/copilot-instructions.md`.

## 4. Commit and push the pages
Only the assignment files (the repo has unrelated files):
```
git add assignment3
git status                              # confirm only your pages, CSS, JS and images are listed
git commit -m "Assignment 3: index.html, search-results.html and CSS from Linux"
git push origin master
```
If the push is rejected, run `git pull --rebase origin master` and push again.
If it asks for credentials, use your GitHub account (token or SSH key).

## 5. Tell the Mac session
Say "Linux pages are pushed". Then on the Mac: `git pull` and the wiring can start.

## 6. Optional: rebuild the vector index on Linux
Not needed for the browser version (the Mac already built `index.json`), but if you want it locally:
```
cd assignment3/webserver
npm ci
npm run build-index        # first run downloads the embedding model; needs network
```

## Notes
- Simmons web server: plain HTTP, Apache, PHP 8.4, no Node.js. The in-browser vector search test passed there
  (`assignment3/webserver/simmons-test/`). SFTP: `lcd` to the local folder, then `put -r <folder>`, remote dir is `public_html`.
- Delete `simmons-test/server-info.php` from the server (`rm simmons-test/server-info.php`), then the whole folder when done.
- Routine: `git pull` at the start of a session, commit and `git push origin master` at the end.
