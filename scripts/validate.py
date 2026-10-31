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
        + render_errors()
    )
    for error in errors:
        print(error, file=sys.stderr)
    print("ok" if not errors else f"{len(errors)} problem(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
