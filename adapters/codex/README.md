# Codex

- 매니페스트: `.codex-plugin/plugin.json`. 다른 모든 매니페스트를 이 파일에서 만든다.
- 마켓플레이스: `.agents/plugins/marketplace.json` (생성 파일)
- 세션 시작 훅이 없다. `using-ai-automation`은 description으로만 Codex에 닿는다.
- 에이전트: Codex는 `agents/`를 읽지 않는다. `agents/<name>.md`를 읽고 그 본문으로 서브에이전트를 띄운다.

## 서브에이전트를 쓰려면

`~/.codex/config.toml`에 아래를 넣는다.

```toml
[features]
multi_agent = true
```

어떤 도구가 생기는지는 모델 프리셋이 고르는 멀티 에이전트 버전(V1·V2)에 따라 다르다.
이 문서와 실제 도구 목록이 다르면 실제 도구 목록을 따른다.

- **띄우기**: `spawn_agent {fork_turns: "none"}`로 깨끗한 컨텍스트에서 시작한다. 기본값 `"all"`은 지금까지의 대화를 통째로 복사한다.
- **고치기**: 같은 서브에이전트에게 `followup_task`로 다시 맡긴다. 새로 띄우지 않는다.
- **정리**: V2에는 `close_agent`가 없다. 끝난 서브에이전트는 자리가 필요할 때 자동으로 정리된다. V1에서는 결과를 받은 뒤 `close_agent`로 닫는다.
- **모델 이름**: 스킬이나 예전 세션의 모델 이름을 그대로 넣지 않는다. 현재 허용 목록에 있는지 먼저 확인한다.

## 기다리기

`wait_agent`는 폴링이 아니라 이벤트 구독이다.
짧게 여러 번 기다려도 빨라지지 않고 호출 비용만 늘어난다.

- 할 일이 남아 있으면 기다리지 않는다. 끝난 서브에이전트의 결과는 다음 차례에 저절로 들어온다.
- 할 일이 없을 때만 `timeout_ms` 300000~600000(5~10분)으로 기다린다.
- 한 번 기다린 뒤에는 상태를 한 줄 알리고 `list_agents`로 결과를 보고하지 않은 서브에이전트가 있는지 확인한다.

## 모델 지정

`spawn_agent`에는 `model`과 `reasoning_effort`를 함께 지정한다.
`model`만 지정하면 추론 강도가 그 모델의 기본값으로 돌아간다.

지정을 빠뜨렸을 때를 대비해 `~/.codex/config.toml`에 기본값을 두면 좋다.

```toml
[agents]
default_subagent_model = "<허용 목록에 있는 중간 등급 모델>"
default_subagent_reasoning_effort = "medium"
```
