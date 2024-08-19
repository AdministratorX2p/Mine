from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 27353035))
API_HASH = getenv("API_HASH", "cf2a75861140ceb746c7796e07cbde9e")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", 5350929381))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "Nexa_Verse")
UPDATE_CHNL = getenv("UPDATE_CHNL", "DadEyeBotz")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Dev_Arora_0981")

# Random Start Images
IMG = [
    "https://graph.org/file/8fe8c4eb2886376e48423.jpg",
    "https://graph.org/file/89e0800248a16eb93515b.jpg",
    "https://graph.org/file/df74d3cb75436c6f1e345.jpg",
    "https://graph.org/file/d57d12a1d0cd409d8eec4.jpg",
    "https://graph.org/file/e8a56835015bf849637cf.jpg",
    "https://graph.org/file/6ce1ae50a475b058b79f9.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgQAAxkBAALRi2NZXUgjZCT775L5Nr0XrLbQ6XIpAAK_EQACpvFxHq2xh5JRVJNrKgQ",
    "CAACAgQAAxkBAALRjGNZXUs6YPggISBdtg4nXaU0vjNzAALqCwACbCIRU61ZQKi3F88DKgQ",
    "CAACAgQAAxkBAALRjWNZXUvETcfHR2Yi9ftTQLLP2uD8AAIVDAAC1SMQU-QrCHEcbz8rKgQ",
]


EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
]
