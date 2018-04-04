from settings import URL
from models import Junior
import requests

def conn():

    r = requests.get(URL, data={},headers={"Content-Type": "application/json"})
    rjson = r.json()

    return rjson
