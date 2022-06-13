## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
BOT_TOKEN = getenv("BOT_TOKEN", "5159774583:AAHaIX-f9DmCZWsbAH8X-j6B17BCpM8K6hI")
API_ID = int(getenv("API_ID", "7931165"))
API_HASH = getenv("API_HASH", "5a2e46d1e6deb1456c75aa743bc8e0e6")
SUDO_USERS = getenv("SUDO_USERS", "1615607413"))
