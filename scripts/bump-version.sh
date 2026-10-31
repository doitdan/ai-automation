#!/usr/bin/env bash
set -euo pipefail

if [ $# -ne 1 ]; then
  echo "usage: scripts/bump-version.sh <version>" >&2
  exit 1
fi

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
python3 - "$ROOT/.codex-plugin/plugin.json" "$1" <<'PY'
import json, sys
path, version = sys.argv[1], sys.argv[2]
manifest = json.load(open(path))
manifest["version"] = version
open(path, "w").write(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
PY
python3 "$ROOT/scripts/render-manifests.py"
