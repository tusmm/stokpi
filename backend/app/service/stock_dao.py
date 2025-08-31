import os
from dotenv import load_dotenv
from polygon import RESTClient


class StockDAO():
    def __init__(self):
        load_dotenv()
        POLYGON_API_KEY = os.getenv('POLYGON_API_KEY')

        client = RESTClient(api_key=POLYGON_API_KEY)

    