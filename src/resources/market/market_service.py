from utils import api
import http.client
import json

from utils.api import get_api_headers


def get_market_data_service():
    """"""
    headers = headers_to_fetch = {
        'X-RapidAPI-Key': 'RAPIDAPI_KEY',
        'X-RapidAPI-Host': 'RAPIDAPI_HOST'
    }
    headers = get_api_headers(headers_to_fetch)
    symbols = ["AAPL", "MSFT", "GOOG", "AMZN", "META"]
    market_data = {}
    for symbol in symbols:
        endpoint = f"/price?&symbol={symbol}&outputsize=30&format=json"
        conn = http.client.HTTPSConnection("twelve-data1.p.rapidapi.com")
        try:
            conn.request("GET", endpoint, headers=headers)
            response = conn.getresponse()
            if response.status != 200:
                raise Exception(
                    f"API request failed for {symbol} with status {response.status}: {response.reason}")
            market_data[symbol] = json.loads(response.read())
        finally:
            conn.close()
    return market_data
