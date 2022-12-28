# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os

from Shikimori import HEROKU_API_KEY, HEROKU_APP_NAME, REDIS_URL, SS_TOKEN, SS_USERNAME


def get_user_list(config, key):
    with open("{}/Senku/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 3344739  # integer value, dont use ""
    API_HASH = "88d43ee045dd90660b4360ba59fe3c48"
    TOKEN = "5229769235:AAGfk_6sVvRxOlPm_4uPGktY8GQleWW1pJs"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1719179612  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "SILVER_KING"
    SUPPORT_CHAT = "botperosupport"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001614799396
    )  # Prints any new group the bot is added to, prints just the name and ID.
    LOG_CHANNEL = (
        -1001675371197
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "something://somewhat:user@hosturl:port/databasename"  # needed for any database modules
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    URL = None
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = 1719179612
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = 5255427162 1037179104 790824807 1720329781 1833878636 1786637879 1673589690 5058417875 1749188073 1377359278 1477990134 1174476949 1005344893 1128635113 5173715306 1599920249
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = 1693209365 5385011323 1596559467 1908943391 1678517796 1704404400 1474610394 1599920249
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = "CAACAgQAAxkBAAI3aGLPOhSjc16o9HChRQjSlY-z7v0yAAJPAAP9SU4JudKXVgqptKIpBA"  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "6950f559377140a4e1594c564cdca6a3"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "SOME1HING_privet_990022"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    ERROR_LOG_CHANNEL = -1001701790469  # needed to make sure 'save from' messages persist
    HEROKU_API_KEY = "6950f559377140a4e1594c564cdca6a3"  # Your Heroku API key, get it from 'https://dashboard.heroku.com/account
    HEROKU_APP_NAME = (
        "easterfg"  # Enter the Heroku app name here (Must an exact same name with your input above)
    )
    ARQ_API = "AVJKDE-HBPTZF-MXXCNH-EUPLFS-ARQ"
    APOD_API_KEY = "UYrZnbgQwUtX81olaTwOGea1tcsXcZPGMr3hxOue"
    REDIS_URL = "redis://default:xmod@redis-14668.c232.us-east-1-2.ec2.cloud.redislabs.com:14668/xmod-db"
    ANIME_NAME = "POKEMON"
    START_MEDIA = "https://telegra.ph/file/5cca520a9faf44ed14f35.jpg"
    BOT_USERNAME = "officerjennyprobot"
    UPDATE_CHANNEL = "xmodnews"
    ALIVE_MEDIA = "https://telegra.ph/file/85592c5a721a6d62714d9.jpg"
    BOT_ID = 5410337371
    STATS_IMG = "awoo"
    NETWORK_USERNAME = "xmodnews"
    NETWORK = "X MOD"
    MEDIA_GM = "https://telegra.ph/file/fdab96a3ef494819e9869.mp4"
    MEDIA_GN = "https://telegra.ph/file/b2987003aa27cbb09b389.mp4"
    MEDIA_HELLO = "https://telegra.ph/file/60cbbd51c8e26005f8e77.mp4"
    MEDIA_BYE = "https://telegra.ph/file/1ed0895e859b0fb7e38f6.mp4"
    INLINE_IMG = "https://telegra.ph/file/85592c5a721a6d62714d9.jpg"
    API_WEATHER = "f6ae3985877d1cc3f1139a2388c6ea40"
    OWNER_WELCOME_MEDIA = "https://telegra.ph/file/b59ffc36a1dea7039bc94.mp4"

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
