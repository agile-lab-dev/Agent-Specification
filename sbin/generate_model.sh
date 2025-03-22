#!/bin/sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

pushd $SCRIPT_DIR/.. > /dev/null
uv run datamodel-codegen --input agent-specification.yaml --input-file-type openapi --output model.py
popd > /dev/null