import configparser

config = configparser.ConfigParser()
config.read('config.ini')
print(config["pyrogram"])

def getDataFromConfig(category, variable):
    return config[category][variable]


LANG = "uk-UA"

# telegram api for pyrogram
api_id = getDataFromConfig('pyrogram', 'api_id')
api_hash = getDataFromConfig("pyrogram", "api_hash")

# urls
MOVIE_BASE_URL = "https://api.themoviedb.org/3/movie/"
MONOBANK_URL = "https://api.monobank.ua/personal/"
IMAGES_URL = "https://api.unsplash.com/search/photos"

# api_keys
MOVIE_API_KEY = getDataFromConfig("apikeys", "movie_api_key")
MONOBANK_API_KEY = getDataFromConfig("apikeys", "monobank_api_key")
IMAGES_API_KEY = getDataFromConfig("apikeys", "images_api_key")
