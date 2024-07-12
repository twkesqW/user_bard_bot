import configparser
from dotenv import load_dotenv
import os
load_dotenv()




LANG = "uk-UA"

# telegram api for pyrogram
api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")

# urls
MOVIE_BASE_URL = "https://api.themoviedb.org/3/movie/"
MONOBANK_URL = "https://api.monobank.ua/personal/"
IMAGES_URL = "https://api.unsplash.com/search/photos"

# api_keys
MOVIE_API_KEY = os.getenv("movie_api_key")
MONOBANK_API_KEY = os.getenv("monobank_api_key")
IMAGES_API_KEY = os.getenv("images_api_key")
