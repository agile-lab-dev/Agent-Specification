#!/bin/sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
$SCRIPT_DIR/generate_model.sh

pushd $SCRIPT_DIR/.. > /dev/null
uv run validate_model.py
popd > /dev/null