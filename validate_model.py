"""
This script uses an auto-generate pydantic model to validate a YAML Agent Descriptor.

When the descriptor is invalid the pydantic model throws a ValidationError exceptions listing
all the specs violations (so fixing the errors is quick).

When the OpenAPI specs are modified the pydantic model must be regenerated with:

uv run datamodel-codegen  --target-python-version=3.12 --input agent-specification.yaml --output model.py

"""

from pathlib import Path

import yaml

from model import AgentDescriptor

PATH = Path('examples/health-care.yaml')
yaml_dict = yaml.safe_load(PATH.read_text())
AgentDescriptor.model_validate(yaml_dict)

print(f'\n✅ Validation of "{PATH}" succeded!\n')
