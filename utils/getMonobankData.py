from config import MONOBANK_URL,MONOBANK_API_KEY
import requests

def getMonobankData():
    url = f"{MONOBANK_URL}client-info"
    header = {"X-Token": MONOBANK_API_KEY}
    res = requests.get(url,headers=header)

    return res.json()["accounts"]
