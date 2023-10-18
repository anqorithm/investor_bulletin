import os
from dotenv import load_dotenv


def get_api_headers(header_env_vars):
    """
    Constructs headers for API requests based on provided environment variable keys.
    """
    load_dotenv()
    headers = {}
    for header, env_var in header_env_vars.items():
        value = os.environ.get(env_var)
        if not value:
            raise ValueError(f"Please set the {env_var} environment variable.")
        headers[header] = value
    return headers
