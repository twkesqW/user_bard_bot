import requests
from config import IMAGES_URL, IMAGES_API_KEY


def getImage(desc):
    url = f"{IMAGES_URL}?client_id={IMAGES_API_KEY}&query={desc}&page=1&per_page=5"
    # print(url)
    res = [x["urls"]["small"] for x in requests.get(url).json()["results"]]
    return res
