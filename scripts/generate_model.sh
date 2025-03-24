#!/bin/sh

echo '- Generating the pydantic model'

uv run datamodel-codegen --input agent-specification.yaml --input-file-type openapi --output model.py
