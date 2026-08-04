#!/bin/bash
# =============================================================================
#  publish.command  —  send the Dig Deeper study library to GitHub
# -----------------------------------------------------------------------------
#  Double-click this file. It will:
#
#    1. rebuild the catalogue pages (runs rebuild-index.command for you),
#    2. compare this folder with the GitHub repository,
#    3. show you exactly what is new, changed and removed,
#    4. ask before publishing anything that DELETES files, then
#    5. commit and push.
#
#  Only the differences travel — unchanged files are not re-uploaded.
#  .odt print copies stay on this Mac and are never published.
#
#  To see the comparison without publishing, run in Terminal:
#      DRY=1 ./publish.command
#  (a dry run writes nothing at all, so it also skips the catalogue rebuild —
#   the real run may therefore show a few more changed index.html pages)
# =============================================================================

REPO_URL="https://github.com/pqcouch/dig-deeper"
BRANCH="master"

cd "$(dirname "$0")" || { echo "Cannot find my own folder."; exit 1; }
ROOT="$(pwd)"

rule() { printf '%s\n' "-------------------------------------------------------------"; }
finish() {                      # $1 = exit code
  echo
  rule
  if [ -t 0 ]; then read -r -p "Press Return to close this window. " _ </dev/tty; fi
  exit "${1:-0}"
}

do_push() {
  echo "Uploading to GitHub..."
  if git push -q -u origin "HEAD:$BRANCH" 2>/tmp/publish-push-err; then
    echo "Published. Everything is now on GitHub."
    return 0
  fi
  err="$(cat /tmp/publish-push-err)"
  if echo "$err" | grep -qi 'non-fast-forward\|fetch first\|rejected'; then
    echo "GitHub had newer changes — merging them in and retrying..."
    if git pull -q --rebase origin "$BRANCH" && git push -q -u origin "HEAD:$BRANCH"; then
      echo "Published. Everything is now on GitHub."
      return 0
    fi
    err="$(cat /tmp/publish-push-err)"
  fi
  echo
  echo "The upload did not go through:"
  echo "$err" | sed 's/^/    /'
  echo
  if echo "$err" | grep -qi 'auth\|username\|password\|token\|denied'; then
    echo "GitHub no longer accepts account passwords for this. You need to sign in"
    echo "once; after that this script will never ask again. Two ways:"
    echo
    echo "  EASIEST — GitHub CLI (needs Homebrew):"
    echo "      brew install gh"
    echo "      gh auth login        (choose GitHub.com, HTTPS, login with a web browser)"
    echo
    echo "  NO HOMEBREW — a personal access token:"
    echo "      1. Go to  https://github.com/settings/tokens"
    echo "      2. 'Generate new token (classic)', tick the  repo  box, generate it,"
    echo "         and copy the token (it starts ghp_ and is shown only once)."
    echo "      3. Double-click this file again. At 'Username' type  pqcouch ;"
    echo "         at 'Password' paste the token."
    echo "      The token is then saved in your Mac's keychain."
  fi
  echo
  echo "Your work is safely committed on this Mac — nothing has been lost."
  echo "Just double-click this file again once you have signed in."
  return 1
}

echo "Publishing library:  $ROOT"
echo "To:                  $REPO_URL  (branch $BRANCH)"
[ -n "${DRY:-}" ] && echo "(DRY RUN — nothing will be committed or pushed)"
rule

# ----- 0. is git installed? ---------------------------------------------------
if ! command -v git >/dev/null 2>&1; then
  echo "Git is not installed on this Mac."
  echo "Open Terminal and run:  xcode-select --install"
  echo "then double-click this file again."
  finish 1
fi

# ----- 1. first run: wire this folder up as the repository --------------------
if [ ! -d .git ]; then
  echo "First run — connecting this folder to GitHub..."
  git init -q || { echo "Could not create the repository."; finish 1; }
  git symbolic-ref HEAD "refs/heads/$BRANCH"
  git remote add origin "$REPO_URL"
  git config core.precomposeunicode true
  echo "Downloading the current state of the repository (this may take a moment)..."
  if ! git fetch -q origin "$BRANCH"; then
    echo "Could not reach GitHub. Check your internet connection and try again."
    finish 1
  fi
  # Point the index at what GitHub already has, WITHOUT touching your files,
  # so only genuine differences are published.
  git reset --mixed -q FETCH_HEAD || { echo "Could not compare with GitHub."; finish 1; }
  echo "Connected."
  rule
fi

# keep the remote correct even if it was set up differently before
git remote set-url origin "$REPO_URL" 2>/dev/null || git remote add origin "$REPO_URL"
# remember the GitHub sign-in in the Mac keychain, so it is asked for only once
[ -z "$(git config --get credential.helper)" ] && git config credential.helper osxkeychain
# a shallow history cannot always be pushed — deepen it once
[ -f .git/shallow ] && { echo "Completing repository history..."; git fetch -q --unshallow 2>/dev/null; }

# ----- 2. refresh the catalogue pages ----------------------------------------
if [ -x ./rebuild-index.command ] || [ -f ./rebuild-index.command ]; then
  echo "Rebuilding catalogue pages..."
  bash ./rebuild-index.command >/dev/null 2>&1 && echo "Catalogue rebuilt." \
    || echo "(rebuild-index.command reported a problem — continuing anyway)"
  rule
fi

# ----- 3. pick up anything published from GitHub itself ----------------------
echo "Checking GitHub for changes made elsewhere..."
git fetch -q origin "$BRANCH" 2>/dev/null
behind="$(git rev-list --count HEAD..FETCH_HEAD 2>/dev/null || echo 0)"
[ "$behind" != "0" ] && echo "GitHub has $behind commit(s) this folder hasn't seen; they'll be merged in on push."

# ----- 4. stage the differences ----------------------------------------------
# .odt copies are ignored, but untrack any that were published in the past
git rm -r -q --cached --ignore-unmatch '*.odt' >/dev/null 2>&1
git add -A || { echo "Could not read the folder. If files show iCloud cloud icons,"; \
                echo "select all in Finder, right-click and choose 'Download Now', then retry."; finish 1; }

added="$(git diff --cached --name-only --diff-filter=A | wc -l | tr -d ' ')"
changed="$(git diff --cached --name-only --diff-filter=M | wc -l | tr -d ' ')"
removed="$(git diff --cached --name-only --diff-filter=D | wc -l | tr -d ' ')"
renamed="$(git diff --cached --name-only --diff-filter=R | wc -l | tr -d ' ')"
total=$((added + changed + removed + renamed))

rule
if [ "$total" -eq 0 ]; then
  # Nothing new to commit — but an earlier run may have committed and then failed
  # to upload (e.g. a sign-in problem). If so, just send that commit now.
  ahead="$(git rev-list --count FETCH_HEAD..HEAD 2>/dev/null || echo 0)"
  if [ "${ahead:-0}" -gt 0 ]; then
    echo "No new changes, but $ahead earlier commit(s) never reached GitHub."
    do_push || finish 1
    finish 0
  fi
  echo "Everything is already up to date. Nothing to publish."
  finish 0
fi

echo "WHAT WILL BE PUBLISHED"
echo "  new:      $added"
echo "  changed:  $changed"
echo "  removed:  $removed"
[ "$renamed" -gt 0 ] && echo "  renamed:  $renamed"
echo

show() { # $1 = filter letter, $2 = heading
  local n; n="$(git diff --cached --name-only --diff-filter="$1" | wc -l | tr -d ' ')"
  [ "$n" -eq 0 ] && return
  echo "$2"
  git diff --cached --name-only --diff-filter="$1" | sed 's/^/    /' | head -30
  [ "$n" -gt 30 ] && echo "    ...and $((n - 30)) more"
  echo
}
show A "New files:"
show M "Changed files:"
show D "Files to be REMOVED from GitHub:"

# ----- 5. confirm deletions ---------------------------------------------------
if [ "$removed" -gt 0 ] && [ -z "${DRY:-}" ]; then
  rule
  echo "$removed file(s) will be deleted from the online repository."
  echo "They stay on this Mac — only the published copies go."
  if [ -t 0 ]; then
    read -r -p "Type  yes  to continue (anything else cancels): " ok </dev/tty
    if [ "$ok" != "yes" ]; then
      echo "Cancelled. Nothing was published."
      git reset -q            # unstage, leave your files untouched
      finish 0
    fi
  fi
fi

if [ -n "${DRY:-}" ]; then
  rule
  echo "DRY RUN — stopping here. Nothing was committed or pushed."
  git reset -q
  finish 0
fi

# ----- 6. commit --------------------------------------------------------------
rule
stamp="$(date '+%e %B %Y' | sed 's/^ *//')"
parts=""
[ "$added"   -gt 0 ] && parts="$parts, $added new"
[ "$changed" -gt 0 ] && parts="$parts, $changed changed"
[ "$removed" -gt 0 ] && parts="$parts, $removed removed"
parts="${parts#, }"
git -c user.name="${GIT_AUTHOR_NAME:-$(git config user.name || echo 'Study library')}" \
    -c user.email="${GIT_AUTHOR_EMAIL:-$(git config user.email || echo 'pqcouch@gmail.com')}" \
    commit -q -m "Update study library ($stamp): $parts" || { echo "Commit failed."; finish 1; }
echo "Committed."

# ----- 7. push ----------------------------------------------------------------
do_push || finish 1

finish 0
