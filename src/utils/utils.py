import os
from dotenv import load_dotenv


def get_api_headers():
    load_environment_variables()
    API_HOST = os.environ.get("RAPIDAPI_HOST")
    API_KEY = os.environ.get("RAPIDAPI_KEY")
    if not API_KEY:
        raise ValueError("Please set the RAPIDAPI_KEY environment variable.")

    headers = {
        'X-RapidAPI-Key': API_KEY,
        'X-RapidAPI-Host': API_HOST
    }

    return headers


def load_environment_variables():
    """
    Load environment variables from a .env file.
    """
    load_dotenv()
