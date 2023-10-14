""" Market Service """
"""_summary_
this file to write any business logic for the Market
"""




import http.client
import json
from utils import utils
import http.client
import json
from utils import utils
def get_market_data_serivce():
    headers = utils.get_api_headers()
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
