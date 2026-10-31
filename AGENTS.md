# AI Automation 기여 규칙

Codex가 주 하네스다.
Claude Code·Cursor·Gemini CLI는 어댑터를 거쳐 같은 `skills/`·`knowledge/`·`agents/`를 읽는다.
이 파일은 이 저장소 안에서 작업할 때만 읽힌다.
플러그인을 쓰는 세션에는 들어가지 않으니, 그때 지킬 규칙은 `knowledge/`에 둔다.

## 구조

`docs/architecture.md`를 본다.

## 구조 규칙

- 직접 고치는 매니페스트는 `.codex-plugin/plugin.json` 하나다. 고친 뒤 `scripts/render-manifests.py`를 돌리고 생성된 파일까지 커밋한다.
- 스킬은 `skills/<name>/SKILL.md`에서만 찾는다. 하위 폴더로 묶지 않는다.
- 사실과 자료(조사 결과, 참고 데이터, 외부 규칙 원문, 목록, 용어)는 쓰는 스킬이 하나여도 `knowledge/`에 주제별로 둔다. 추가·갱신 규칙은 `knowledge/INDEX.md`에 있다.
- `skills/<name>/references/`에는 그 업무를 하는 방식만 둔다: 양식, 승인된 예시, 업무 전용 판단 규칙, 하위 프롬프트.
- 두 스킬 이상이 쓰는 양식과 팀 규칙은 `knowledge/templates/`, `knowledge/rules/`에 둔다.
- 모든 스킬이 꼭 지킬 규칙은 `knowledge/rules/`에 쓰고 `knowledge/INDEX.md`의 "필수 규칙"에 올린다. 스킬 본문에 복사하지 않는다.
- 업무 스킬은 제목 바로 아래, 첫 `##` 절보다 앞에 `skills/using-ai-automation/SKILL.md`의 "모든 스킬에 적용"을 먼저 따른다는 줄을 둔다. 에이전트는 첫 `##` 절보다 앞에 `knowledge/INDEX.md`의 "필수 규칙"을 읽고 지킨다는 줄을 둔다. `validate.py`가 검사한다.
- 요청 → 스킬 표는 `skills/using-ai-automation/SKILL.md`에만 둔다. 요청 → 저장소 표는 `knowledge/routing.md`에만 둔다.
- 에이전트는 `agents/<name>.md`에만 둔다. `adapters/`에 복사하지 않는다.
- 사용자마다 다른 값(로컬 경로 등)은 `~/.config/ai-automation/config.json`에 둔다. 이 저장소에 넣지 않는다.
- 설치된 플러그인은 각 하네스의 캐시 폴더에서 돈다. 스킬·지식·에이전트를 고칠 때는 캐시가 아니라 설정의 `pluginRepository`(이 저장소의 로컬 clone)에 쓴다.

## 문서 작성 규칙

이 저장소의 모든 Markdown(스킬, 에이전트, 지식, 문서)에 적용한다.

### 언어

- 본문은 한국어로 쓴다.
- `name`, 파일명, 폴더명은 영문 소문자와 하이픈으로 쓴다. 예: `meeting-notes.md`
- 명령어, 경로, 도구 이름, 코드 식별자는 원문 그대로 쓴다.

### frontmatter

- 스킬과 에이전트는 `name`과 `description`을 둔다. `name`은 파일명 또는 폴더명과 같다.
- `description`에는 언제 쓰는지만 쓴다. 절차를 요약하지 않는다. 요약이 있으면 에이전트가 본문을 건너뛰고 요약만 따른다.
- `description`에는 팀원이 실제로 치는 요청 문구를 따옴표로 나열한다. 한국어와 영어 표현이 둘 다 쓰이면 둘 다 넣는다.

### 스킬 본문

- 순서는 실행 조건 → 단계 → 완료 조건이다.
- 단계는 번호를 매기고, 한 단계에 행동 하나만 쓴다.
- 완료 조건은 확인할 수 있는 문장으로 쓴다. 예: "`validate.py`가 `ok`를 출력한다"
- 도구 이름 대신 행동을 쓴다. "파일을 읽는다", "서브에이전트를 띄운다"처럼 쓰면 네 하네스에서 같은 본문을 쓸 수 있다.
- 다른 파일의 내용을 복사하지 않고 경로를 가리킨다. 예: "`knowledge/rules/approval.md`를 읽는다"

### 문장

- 한 줄에 한 문장을 쓴다.
- 표는 같은 기준으로 여러 항목을 비교할 때만 쓴다.
- 결정을 적을 때는 고른 안과 함께 버린 안, 그 대가를 적는다.
- 번역체와 과장된 표현을 쓰지 않는다. 예: "~를 통해", "~에 있어서", "혁신적인"

### 결과물 문체

에이전트가 사용자에게 만들어 주는 결과물(보고서, 회의록, 메일)의 문체는 `knowledge/rules/writing.md`를 따른다.
이 파일에 같은 내용을 다시 쓰지 않는다.

## 버전 규칙

Claude Code는 버전이 같으면 새 커밋이 있어도 플러그인을 업데이트하지 않는다.
Codex는 커밋만 바뀌어도 받지만, 버전이 같으면 사용자가 어느 내용을 쓰는지 구분할 수 없다.

- 사용자에게 닿는 파일을 바꿨으면 푸시하기 전에 버전을 올린다. 대상은 `skills/`, `knowledge/`, `agents/`, `hooks/`, `adapters/`, `config/`, `GEMINI.md`다.
- `docs/`, `README.md`, `AGENTS.md`, `scripts/`, `.github/`만 바꿨으면 버전을 올리지 않는다.
- 스킬이나 에이전트를 더하거나 지우거나 이름을 바꾸면 가운데 자리를 올린다. 예: 0.1.3 → 0.2.0
- 그 밖의 변경은 끝자리를 올린다. 예: 0.1.0 → 0.1.1
- 한 번에 푸시하는 커밋이 여럿이어도 버전은 한 번만 올린다.
- 버전은 `scripts/bump-version.sh <version>`으로만 바꾼다. 매니페스트를 손으로 고치지 않는다.
- `CHANGELOG.md`에 `## <version> — <날짜>` 제목을 만들고, 바뀐 것을 한 줄씩 적는다.
- 푸시한 뒤 `v<version>` 태그를 붙여 푸시한다.
- `validate.py`는 마지막 태그 이후 위 대상이 바뀌었는데 버전이 그대로면, 또는 CHANGELOG에 현재 버전 제목이 없으면 실패한다.

## PR 전에

1. `python3 scripts/validate.py`를 돌린다.
2. 바꾼 스킬을 실제 Codex 세션에서 한 번 이상 실행하고 대화 기록을 PR에 붙인다.
3. `.github/pull_request_template.md`를 채운다.

## 릴리스

`docs/releasing.md`를 본다.
