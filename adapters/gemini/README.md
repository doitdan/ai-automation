# Gemini CLI

- 매니페스트: `gemini-extension.json` (생성 파일)
- 컨텍스트: `GEMINI.md`가 진입 스킬과 이 파일을 @로 불러온다.
- 세션 시작 훅이 없다.
- 에이전트: `agents/<name>.md`를 읽고 그 본문으로 서브에이전트를 띄운다.

## 도구 대응표

스킬은 도구 이름 대신 행동으로 쓴다. Gemini CLI에서는 아래 도구로 바꿔 실행한다.

| 스킬이 말하는 행동 | Gemini CLI 도구 |
|--------------------|-----------------|
| 파일 읽기 | `read_file` |
| 여러 파일 한 번에 읽기 | `read_many_files` |
| 새 파일 만들기 | `write_file` |
| 파일 고치기 | `replace` |
| 셸 명령 실행 | `run_shell_command` |
| 파일 내용 검색 | `grep_search` |
| 파일 이름으로 찾기 | `glob` |
| 폴더 목록 보기 | `list_directory` |
| URL 가져오기 | `web_fetch` |
| 웹 검색 | `google_web_search` |
| 스킬 실행 | `activate_skill` |
| 서브에이전트 띄우기 | `invoke_agent`, `agent_name: "generalist"` |
| 서브에이전트 여러 개 동시에 | 한 응답에서 `invoke_agent`를 여러 번 호출 |
| 할 일 관리 | `write_todos` |

## 서브에이전트

`invoke_agent`는 `agent_name`과 `prompt`를 받는다.
채팅에서 `@generalist <프롬프트>`라고 쓰는 것과 같다.

`agents/<name>.md`를 쓸 때는 본문의 빈칸을 모두 채운 뒤 `invoke_agent`의 `prompt`로 넘긴다.
서로 의존하지 않는 일은 한 응답에서 여러 번 호출해 동시에 돌린다.

## 지시 파일

스킬이 "지시 파일"이라고 하면 Gemini CLI에서는 `GEMINI.md`다.
전역 `~/.gemini/GEMINI.md`, 작업 폴더와 그 상위 폴더의 `GEMINI.md`를 차례로 읽는다.
