import requests
from config import MOVIE_API_KEY,LANG

def getDataFilm(title):
    title = title.split(" ")
    url = f"https://api.themoviedb.org/3/search/movie?query={'+'.join(title)}&api_key={MOVIE_API_KEY}&language={LANG}"
    res =  requests.get(url).json()["results"][0]

    imagepath = "https://image.tmdb.org/t/p/original"
    data = {
        "title": res["title"],
        "overview": res["overview"],
        "image": f"{imagepath}{res['poster_path']}",
        "vote": res["vote_average"]


    }
    return data



