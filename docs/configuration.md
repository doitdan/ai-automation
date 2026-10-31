# 사용자 설정

사용자마다 파일 하나를 둔다: `~/.config/ai-automation/config.json`

플러그인은 설치할 때 각 하네스의 캐시 폴더로 복사된다.
그래서 플러그인 안에는 사용자마다 다른 값을 둘 수 없다.

- 형식: `config/schema.json`
- 예시: `config/example.json`
- `pluginRepository`: ai-automation 저장소 로컬 clone의 절대 경로. AI가 스킬·지식·에이전트를 고칠 때 여기에 쓴다
- `repositories`: `knowledge/repositories.md`의 저장소 이름 → 로컬 절대 경로
