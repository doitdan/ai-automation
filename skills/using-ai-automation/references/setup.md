# 초기 설정

## 1. 도구

표의 순서대로 확인한다.
없는 것은 설치하고 다시 확인한다.

| 도구 | 확인 | macOS 설치 | Windows 설치 |
|------|------|------------|--------------|
| Git | `git --version` | `brew install git`. Homebrew가 없으면 `xcode-select --install` | `winget install --id Git.Git -e` |
| GitHub CLI | `gh --version` | `brew install gh` | `winget install --id GitHub.cli -e` |
| GitHub 로그인 | `gh auth status` | `gh auth login`(GitHub.com → HTTPS → 브라우저) 후 `gh auth setup-git` | 같음 |

- 설치에는 네트워크가 필요하다. 설치 명령마다 먼저 승인을 받는다.
- 명령 승인, 관리자 비밀번호 입력, 설치 창 클릭, 브라우저에서 GitHub 로그인은 사람이 직접 한다. 채팅으로 비밀번호를 묻지 않는다.
- macOS에 Homebrew가 없고 GitHub CLI도 없으면 묻는다. Homebrew를 설치할지(비밀번호를 묻는다), cli.github.com에서 GitHub CLI를 받을지 고르게 한다.
- 설치한 뒤에도 명령을 찾지 못하면 새 터미널 세션을 열고 다시 확인한다.

## 2. GitHub 플러그인 (Codex)

OpenAI의 GitHub 플러그인이 설치돼 있고 GitHub 계정과 연결돼 있는지 사람에게 묻는다.
아직이면 Plugins에서 설치하고 계정을 연결해 달라고 한다.
연결한 뒤 접근할 수 있는 저장소 하나를 조회해 확인한다.
스킬은 이 플러그인으로 풀 리퀘스트를 열고 검토한다.

## 3. 설정 파일

1. `~/.config/ai-automation/` 폴더를 만든다.
2. 플러그인 루트의 `config/example.json`을 `~/.config/ai-automation/config.json`으로 복사한다.
3. `TODO`로 표시된 값을 사람에게 물어 채운다. 로컬 경로를 추측하지 않는다.
4. 파일이 `config/schema.json` 형식에 맞는지 확인한다.
5. `repositories`에 적은 경로가 모두 실제로 있는지 확인한다.

## 4. 보고

위 항목마다 한 줄씩 알린다: 준비됨, 지금 설치함, 아직 없음과 그 이유.
