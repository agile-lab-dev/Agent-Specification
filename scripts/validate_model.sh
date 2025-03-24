#!/bin/sh

scripts/generate_model.sh

uv run validate_model.py
