import os
from dotenv import load_dotenv
import requests

load_dotenv()
HOST = os.getenv('HOST')
POLYGON_API_KEY = os.getenv('POLYGON_API_KEY')

headers = {
    "Authorization": f"Bearer {POLYGON_API_KEY}"
}

