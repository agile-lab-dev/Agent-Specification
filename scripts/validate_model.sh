#!/bin/sh

if [ ! -f model.py ]; then
    scripts/generate_model.sh
fi

uv run validate_model.py
