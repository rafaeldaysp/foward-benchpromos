import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
apiUrl = os.getenv("SERVER_API_URL")

def getProducts():
  return json.loads(requests.get(f'{apiUrl}/products/with-min-price/for-all').content)

def getSales():
  return json.loads(requests.get(f'{apiUrl}/sales?take=10000&skip=0').content)
