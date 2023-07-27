import configparser


def get_api_id():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['pyrogram']['api_id']

def get_api_hash():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['pyrogram']['api_hash']