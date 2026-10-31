#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / ".codex-plugin" / "plugin.json"


def optional_fields(source, *keys):
    return {key: source[key] for key in keys if key in source}


def claude_plugin(source):
    return {
        "name": source["name"],
        "description": source["description"],
        "version": source["version"],
        "author": source["author"],
        **optional_fields(source, "homepage", "repository", "license", "keywords"),
        "hooks": "./adapters/claude/hooks.json",
    }


def claude_marketplace(source):
    return {
        "name": source["name"],
        "description": source["description"],
        "owner": source["author"],
        "plugins": [
            {
                "name": source["name"],
                "description": source["description"],
                "version": source["version"],
                "source": "./",
                "author": source["author"],
            }
        ],
    }


def cursor_plugin(source):
    return {
        "name": source["name"],
        "displayName": source["interface"]["displayName"],
        "description": source["description"],
        "version": source["version"],
        "author": source["author"],
        **optional_fields(source, "homepage", "repository", "license", "keywords"),
        "skills": "./skills/",
        "hooks": "./adapters/cursor/hooks.json",
    }


def gemini_extension(source):
    return {
        "name": source["name"],
        "description": source["description"],
        "version": source["version"],
        "contextFileName": "GEMINI.md",
    }


def codex_marketplace(source):
    return {
        "name": source["name"],
        "interface": {"displayName": source["interface"]["displayName"]},
        "plugins": [
            {
                "name": source["name"],
                "source": {"source": "url", "url": "./"},
                "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
                "category": source["interface"]["category"],
            }
        ],
    }


GENERATED = {
    ".claude-plugin/plugin.json": claude_plugin,
    ".claude-plugin/marketplace.json": claude_marketplace,
    ".cursor-plugin/plugin.json": cursor_plugin,
    "gemini-extension.json": gemini_extension,
    ".agents/plugins/marketplace.json": codex_marketplace,
}


def rendered_files():
    source = json.loads(SOURCE.read_text())
    return {
        path: json.dumps(build(source), ensure_ascii=False, indent=2) + "\n"
        for path, build in GENERATED.items()
    }


def stale_paths():
    return [
        path
        for path, text in rendered_files().items()
        if not (ROOT / path).exists() or (ROOT / path).read_text() != text
    ]


def write_all():
    for path, text in rendered_files().items():
        (ROOT / path).parent.mkdir(parents=True, exist_ok=True)
        (ROOT / path).write_text(text)
        print(f"rendered {path}")


def main():
    if "--check" not in sys.argv:
        write_all()
        return
    stale = stale_paths()
    for path in stale:
        print(f"stale: {path} — run scripts/render-manifests.py", file=sys.stderr)
    sys.exit(1 if stale else 0)


if __name__ == "__main__":
    main()
