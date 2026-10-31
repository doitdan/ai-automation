---
name: plugin-update
description: 내가 고친 스킬·지식을 ai-automation 저장소에 올리고 내 컴퓨터 플러그인에 적용하려 할 때, 또는 남이 올린 최신 플러그인을 받으려 할 때 쓴다. "플러그인 업데이트해줘", "스킬 올려줘", "내 스킬 반영해줘", "지식 올려줘", "최신으로 받아줘", "플러그인 최신으로", "update the plugin", "push my skill"
---

# 플러그인 업데이트

먼저 `skills/using-ai-automation/SKILL.md`의 "모든 스킬에 적용"을 따른다.

비개발자가 한마디로 자기 변경을 저장소에 올리고, 합쳐진 최신 플러그인을 자기 컴퓨터에 적용하게 한다.

## 실행 조건

- "플러그인 업데이트해줘", "스킬 올려줘", "내 스킬 반영해줘", "지식 올려줘"
- "최신으로 받아줘", "플러그인 최신으로", "update the plugin"
- 쓰지 않는 경우: 스킬 내용을 새로 만들거나 고치는 일. 그것은 `delegation-loop`이고, 이 스킬은 그 결과를 올리고 받는다.

## 입력

| 입력 | 위치 | 형식 |
|------|------|------|
| ai-automation 로컬 clone | 설정 `~/.config/ai-automation/config.json`의 `pluginRepository` | 폴더 경로 |
| 원격 저장소 | `knowledge/repositories.md`의 ai-automation 줄 | GitHub 저장소 |
| 버전 규칙 | 플러그인 저장소의 `AGENTS.md` "버전 규칙" | 문서 |
| 하네스별 업데이트 명령 | 플러그인 저장소의 `docs/releasing.md` 6단계 | 문서 |

## 참고 지식

| 파일 | 이 일에서 쓰는 곳 |
|------|-------------------|
| `knowledge/repositories.md` | 1단계. clone할 원격 저장소 주소 |
| `knowledge/rules/approval.md` | 모든 단계. 승인이 필요한 행동 |

## 단계

파일 목록은 `references/INDEX.md`에 있다.
사람에게 설명할 때는 `references/plain-words.md`의 쉬운 말을 쓴다.
명령은 실행하기 전에 무엇을 하는지 한 줄로 말하고 승인을 받는다.

1. `pluginRepository`를 읽는다.
   - 값이 없으면 `skills/using-ai-automation/references/setup.md` 6단계를 한다.
   - 폴더가 없으면 승인을 받아 `knowledge/repositories.md`의 주소로 `gh repo clone`한다.
2. clone에서 `git status --short`와 `git branch --show-current`를 돌리고, 바뀐 파일을 쉬운 말로 보여 준다.
   - 바뀐 파일이 없으면 9단계로 간다(받기만 한다).
   - `skills/`, `knowledge/`, `agents/` 밖의 파일이 바뀌었으면 그 파일을 올릴지 묻는다.
3. 올릴 내용을 점검한다.
   - `git diff`로 바뀐 줄을 보여 준다.
   - `grep -rnIE '(sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|password\s*[:=]|비밀번호\s*[:=])'`를 바뀐 파일에 돌린다. 나오면 멈추고 그 줄을 지우라고 알린다.
   - Person: 고객사 이름, 수신자, 계정 정보, 개인정보가 없는지 사람이 확인한다. 있으면 올리지 않는다.
4. 작업 브랜치를 만든다: `git switch -c update/<YYYY-MM-DD>-<짧은 영문 설명>`.
   - 이미 `update/`로 시작하는 브랜치에 있으면 그 브랜치를 쓴다.
5. 바뀐 파일만 골라 `git add <파일>`하고, 무엇을 왜 바꿨는지 한국어 한 줄로 커밋한다.
6. 저장소 최신 내용을 합친다: `git fetch origin` 후 `git merge origin/main`.
   - 충돌이 나면 `references/conflicts.md`를 따른다.
7. 버전을 올린다.
   - `AGENTS.md` "버전 규칙"으로 자리를 정한다. 스킬·에이전트를 더하거나 지웠으면 가운데 자리, 그 밖은 끝자리다.
   - `scripts/bump-version.sh <version>`을 돌린다.
   - `CHANGELOG.md` 맨 위에 `## <version> — <오늘 날짜>`와 바뀐 것을 한 줄씩 쓴다.
   - `python3 scripts/validate.py`가 `ok`가 될 때까지 고친다.
   - 커밋한다.
8. 올린다.
   - `git push -u origin <작업 브랜치>`
   - `gh pr create --base main --title "<무엇을 바꿨는지>" --body "<바뀐 것 목록>"`
   - PR 주소를 보여 주고, 합치려면 누가 승인해야 하는지 알린다.
   - Person: 합쳐도 되는지 승인한다.
   - 승인을 받으면 `gh pr merge <번호> --merge --delete-branch`로 합친다.
   - `gh pr view <번호> --json state`가 `MERGED`인지 확인한다.
   - `git switch main`, `git pull --ff-only`, `git tag v<version>`, `git push origin v<version>`.
9. 내 컴퓨터에 적용한다.
   - 받기만 할 때: clone에서 `git switch main`, `git pull --ff-only`를 먼저 한다.
   - Codex: `codex plugin marketplace upgrade ai-automation`. 그다음 `codex plugin list`에서 새 버전을 확인한다.
   - 다른 하네스를 쓰면 `docs/releasing.md` 6단계의 명령을 쓴다.
   - 새 세션을 열어야 바뀐 스킬이 적용된다고 알린다.

## 결정 규칙

- 사람이 "올려"라고 해도 `main`에 바로 push하지 않는다. 항상 `update/` 브랜치와 PR로 올린다.
- 사람의 승인 없이 PR을 합치지 않는다.
- `--force`, `--force-with-lease`, `git reset --hard`, `git push origin main`은 쓰지 않는다.
- 비밀번호나 토큰을 채팅으로 받지 않는다. 로그인이 필요하면 사람이 `gh auth login`을 직접 하게 한다.
- 3단계에서 비밀값이나 고객 자료가 나오면 그 파일은 올리지 않는다.
- 사람이 깃 용어를 쓰지 않으면 깃 용어 대신 `references/plain-words.md`의 쉬운 말을 쓴다.

## 예외

- 다른 사람이 같은 버전을 먼저 올려 6단계에서 버전 파일이나 `CHANGELOG.md`가 충돌한다 → 저장소 쪽 버전을 받아들이고 7단계에서 그다음 버전으로 다시 올린다.
- `gh`가 로그인되어 있지 않다 → `skills/using-ai-automation/references/setup.md` 1단계를 한다.
- PR이 이미 열려 있다(`gh pr list --head <작업 브랜치>`) → 새 PR을 만들지 않고 그 PR에 push한다.
- 받기만 하는데 clone에 올리지 않은 변경이 있다 → 먼저 올릴지 묻는다. 지우지 않는다.

## 완료 조건

무엇이든 보여 주기 전에 모든 항목을 돌린다.
항목마다 한 줄로 통과·실패와 근거를 보고한다.
돌리지 못한 항목은 그 이유를 적는다.

- [ ] clone에서 `git status --short`가 빈 출력이다
- [ ] 이번에 실행한 `git push` 명령의 대상이 모두 `update/` 브랜치나 `v<version>` 태그다
- [ ] 3단계 비밀값 `grep`이 아무것도 찾지 못했다
- [ ] (올린 경우) `python3 scripts/validate.py`가 `ok`를 출력한다
- [ ] (올린 경우) `gh pr view <번호> --json state`가 `MERGED`다
- [ ] (올린 경우) `git ls-remote --tags origin`에 `v<version>`이 있다
- [ ] `codex plugin list`(또는 쓰는 하네스의 목록)가 `main`의 `.codex-plugin/plugin.json`과 같은 버전을 보인다
