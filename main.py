import requests
import yaml
import sys
from openapi_core import OpenAPI
from openapi_core.contrib.requests import RequestsOpenAPIRequest

def pad_string(s: str, sep: str, ln: int = 50) -> str:
  """
  Pads the input string `s` with the specified character `sep` until the total length is 50 characters.
  Args:
      s (str): The input string to be padded.
      sep (chr): The character used for padding.
  Returns:
      str: The padded string with a total length of 50 characters.
  """
  return f"{s}{sep * (ln - len(s))}"

files = ['examples/health-care.yaml']
openapi = OpenAPI.from_file_path('agent-specification.yaml')

anyError = False
for fn in files:
    with open(fn, 'r') as f:
        body_content = yaml.safe_load(f)
    request = requests.Request(
        method='POST',  # Change to your HTTP method
        url='http://www.agents.com/agents',  # Must match spec
        json=body_content
    )
    openapi_request = RequestsOpenAPIRequest(request)
    try:
        openapi.validate_request(openapi_request)
        print(pad_string(fn, '.') + f" ✅ Validated successfully", file=sys.stderr)
    except Exception as e:
        anyError = True
        if e.__cause__:
          e = e.__cause__
        print(pad_string(fn, '.') + f" ❌ Not validated\n{e}", file=sys.stderr)

exit(anyError)