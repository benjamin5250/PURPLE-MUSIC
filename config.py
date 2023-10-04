from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "8479389"))
API_HASH = getenv("API_HASH", "f75e6f068c8bb9b8c884484ea2c6177b")

ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN", "")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001554007729"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "3@cluster0.4wbux.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1962673406").split()))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/5e3c7aef33003ba82d358.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/5e3c7aef33003ba82d358.jpg")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/purpleplaneteer")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", " https://t.me/purpleplaneteers")

STRING_SESSION = getenv("STRING_SESSION", "BQFEoW8AbwHdgJtvoPv4h42F0OWb2YAmHdMB0bdi4mxDYxM-HTAcdZooOoncccwRfmPZvR0dGZI3H9ePGfJvIzlTf2ioYhI1e0vwxJVfmvI0ylx8kuBJVJj1-sqXWmgmzkIU1pURFFnPOlklBntbz2v_t1zgyukKGwTNTIarMd3Ny5hFCsDvshtoVsCrQ3Gk-rQHxF0TgcKx03apVcm5Qk57nuynCZz3qmYaSNQZuOlJ0BeRNRZjGP8Dg2lFI_nonxsdWDb5xCLHEnaKF95QPt4sKa9wLeEW31_PDtJ6DCo4p9WEnqeDGWeuimI-hg9cHO2SIPmcVx0yQ_4xLViXBvYCN0rlYwAAAAF6X2woAA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1962673406").split()))
