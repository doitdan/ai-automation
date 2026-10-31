#!/usr/bin/env python3
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
HOOK_SCRIPTS = ["hooks/session-start", "hooks/run-hook.cmd"]
CHECKED_DATE = re.compile(r"^확인한 날: \d{4}-\d{2}-\d{2}$", re.M)
USER_FACING_PATHS = ["skills", "knowledge", "agents", "hooks", "adapters", "config", "GEMINI.md"]


def frontmatter(path):
    match = FRONTMATTER.match(path.read_text())
    if not match:
        return None
    return dict(
        line.split(":", 1) for line in match.group(1).splitlines() if ":" in line
    )


def json_errors():
    errors = []
    for path in ROOT.rglob("*.json"):
        if ".git" in path.parts:
            continue
        try:
            json.loads(path.read_text())
        except json.JSONDecodeError as error:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON ({error})")
    return errors


def skill_errors():
    errors = []
    for skill_dir in sorted((ROOT / "skills").iterdir()):
        skill = skill_dir / "SKILL.md"
        if not skill.exists():
            errors.append(f"{skill_dir.relative_to(ROOT)}: missing SKILL.md")
            continue
        meta = frontmatter(skill)
        if meta is None:
            errors.append(f"{skill.relative_to(ROOT)}: missing frontmatter")
            continue
        if meta.get("name", "").strip() != skill_dir.name:
            errors.append(f"{skill.relative_to(ROOT)}: name must be {skill_dir.name}")
        if not meta.get("description", "").strip():
            errors.append(f"{skill.relative_to(ROOT)}: missing description")
    return errors


def agent_errors():
    errors = []
    for agent in sorted((ROOT / "agents").glob("*.md")):
        meta = frontmatter(agent) or {}
        if meta.get("name", "").strip() != agent.stem:
            errors.append(f"{agent.relative_to(ROOT)}: name must be {agent.stem}")
        if not meta.get("description", "").strip():
            errors.append(f"{agent.relative_to(ROOT)}: missing description")
    return errors


def manifest_path_errors():
    errors = []
    for manifest in [".claude-plugin/plugin.json", ".cursor-plugin/plugin.json", ".codex-plugin/plugin.json"]:
        for key in ["skills", "hooks", "agents"]:
            target = json.loads((ROOT / manifest).read_text()).get(key)
            if isinstance(target, str) and not (ROOT / target).exists():
                errors.append(f"{manifest}: {key} points to missing {target}")
    return errors


def hook_errors():
    return [
        f"{script}: not executable"
        for script in HOOK_SCRIPTS
        if not os.access(ROOT / script, os.X_OK)
    ]


def current_version():
    return json.loads((ROOT / ".codex-plugin/plugin.json").read_text())["version"]


def git(*args):
    result = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else None


def version_bump_errors():
    last_tag = git("describe", "--tags", "--abbrev=0", "--match", "v[0-9]*")
    if not last_tag or last_tag[1:] != current_version():
        return []
    changed = git("diff", "--name-only", last_tag, "--", *USER_FACING_PATHS)
    if not changed:
        return []
    return [f"user-facing files changed since {last_tag} but version is still {current_version()} — run scripts/bump-version.sh"]


def changelog_errors():
    heading = f"## {current_version()} "
    lines = (ROOT / "CHANGELOG.md").read_text().splitlines()
    if any(line.startswith(heading) for line in lines):
        return []
    return [f"CHANGELOG.md: missing '{heading.strip()} — <date>' heading"]


def knowledge_errors():
    knowledge = ROOT / "knowledge"
    index = (knowledge / "INDEX.md").read_text()
    errors = []
    for path in sorted(knowledge.rglob("*.md")):
        relative = path.relative_to(knowledge).as_posix()
        if relative == "INDEX.md":
            continue
        if f"`{relative}`" not in index:
            errors.append(f"knowledge/{relative}: not listed in knowledge/INDEX.md")
        if relative.startswith("domains/") and not CHECKED_DATE.search(path.read_text()):
            errors.append(f"knowledge/{relative}: missing '확인한 날: YYYY-MM-DD' line")
    return errors


def render_errors():
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts/render-manifests.py"), "--check"],
        capture_output=True,
        text=True,
    )
    return result.stderr.splitlines()


def main():
    errors = (
        json_errors()
        + skill_errors()
        + agent_errors()
        + manifest_path_errors()
        + hook_errors()
        + knowledge_errors()
        + render_errors()
        + version_bump_errors()
        + changelog_errors()
    )
    for error in errors:
        print(error, file=sys.stderr)
    print("ok" if not errors else f"{len(errors)} problem(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
