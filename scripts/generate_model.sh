#!/bin/sh

echo '- Generating the pydantic model'

uv run datamodel-codegen \
    --use-standard-collections \
    --use-union-operator \
    --use-annotated \
    --input agent-specification.yaml \
    --input-file-type openapi \
    --output model.py \

