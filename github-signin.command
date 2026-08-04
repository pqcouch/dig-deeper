#!/bin/bash
# =============================================================================
#  github-signin.command  —  sign in to GitHub once, without typing anything
# -----------------------------------------------------------------------------
#  Git's password prompt shows NOTHING as you paste — no dots, no stars — which
#  makes it look broken. This script sidesteps it entirely: it reads your token
#  straight from the clipboard and files it in the Mac's keychain.
#
#  HOW TO USE
#    1. Make a token at  https://github.com/settings/tokens
#         -> "Generate new token (classic)", tick the  repo  box, generate.
#    2. Copy it (Cmd-C). It starts  ghp_  and is shown only once.
#    3. Double-click this file.
#
#  You only ever do this once. After it, publish.command just works.
# =============================================================================

USERNAME="pqcouch"
REPO_URL="https://github.com/pqcouch/dig-deeper"

cd "$(dirname "$0")" || { echo "Cannot find my own folder."; exit 1; }

rule() { printf '%s\n' "-------------------------------------------------------------"; }
finish() {
  echo
  rule
  if [ -t 0 ]; then read -r -p "Press Return to close this window. " _ </dev/tty; fi
  exit "${1:-0}"
}

echo "GitHub sign-in for the study library"
rule

# ----- 1. get the token from the clipboard -----------------------------------
token="$(pbpaste 2>/dev/null | tr -d '[:space:]')"

if [ -z "$token" ]; then
  echo "Your clipboard is empty."
  echo
  echo "Copy your token first (Cmd-C), then double-click this file again."
  finish 1
fi

case "$token" in
  ghp_*|github_pat_*|gho_*) : ;;
  *)
    echo "What's on the clipboard doesn't look like a GitHub token."
    echo "A token starts with  ghp_  (classic) or  github_pat_  (fine-grained)."
    echo
    echo "Copy the token itself — not the URL, not your password — then run this again."
    finish 1
    ;;
esac

echo "Found a token on the clipboard (${#token} characters)."

# ----- 2. check it actually works before storing it --------------------------
echo "Checking it with GitHub..."
if ! GIT_TERMINAL_PROMPT=0 \
     git -c credential.helper="!f(){ echo username=$USERNAME; echo password=$token; };f" \
     ls-remote "$REPO_URL" HEAD >/dev/null 2>/tmp/signin-err; then
  echo
  echo "GitHub would not accept that token:"
  sed 's/^/    /' /tmp/signin-err | sed "s/$token/[token]/g"
  echo
  echo "Most likely causes:"
  echo "  - the  repo  checkbox wasn't ticked when the token was made"
  echo "  - the token has expired, or was copied incompletely"
  echo "Make a fresh one at  https://github.com/settings/tokens  and try again."
  rm -f /tmp/signin-err
  finish 1
fi
rm -f /tmp/signin-err
echo "GitHub accepted it."

# ----- 3. file it in the keychain --------------------------------------------
git config credential.helper osxkeychain
printf 'protocol=https\nhost=github.com\nusername=%s\npassword=%s\n\n' "$USERNAME" "$token" \
  | git credential-osxkeychain store
echo "Saved to your Mac's keychain."

# ----- 4. clear the clipboard so the token isn't left lying around -----------
printf '' | pbcopy 2>/dev/null && echo "Clipboard cleared."

rule
echo "Done. Double-click  publish.command  whenever you want to publish —"
echo "it will no longer ask for a username or password."
finish 0
