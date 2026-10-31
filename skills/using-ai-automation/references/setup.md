# Setup

## 1. Tools

Check each row in order. Install what is missing, then check again.

| Tool | Check | Install on macOS | Install on Windows |
|------|-------|------------------|--------------------|
| Git | `git --version` | `brew install git`; without Homebrew, `xcode-select --install` | `winget install --id Git.Git -e` |
| GitHub CLI | `gh --version` | `brew install gh` | `winget install --id GitHub.cli -e` |
| GitHub login | `gh auth status` | `gh auth login` (GitHub.com → HTTPS → browser), then `gh auth setup-git` | same |

- Installing needs network access. Ask for approval before each install command.
- Your human partner does these themselves: approving the command, typing an administrator password, clicking the installer window, and logging in to GitHub in the browser. Never ask for a password in the chat.
- macOS without Homebrew and GitHub CLI missing → ask whether they want Homebrew installed (it asks for their password) or GitHub CLI downloaded from cli.github.com.
- A command is still not found after installing → open a new terminal session and check again.

## 2. GitHub plugin (Codex)

Ask your human partner whether the GitHub plugin by OpenAI is installed and connected to their GitHub account. Not yet → ask them to install it from Plugins and connect the account, then confirm by listing one repository they can access. Skills use it to open and review pull requests.

## 3. Config

1. Create `~/.config/ai-automation/`.
2. Copy `config/example.json` from the plugin root to `~/.config/ai-automation/config.json`.
3. Ask your human partner for every value marked `TODO` and fill it in. Never guess a local path.
4. Check the file against `config/schema.json`.
5. Confirm each path under `repositories` exists.

## 4. Report

One line per item above: ready, installed now, or still missing and why.
