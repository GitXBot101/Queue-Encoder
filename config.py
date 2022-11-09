## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
BOT_TOKEN = getenv("BOT_TOKEN", "")
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
SUDO_USERS = getenv("SUDO_USERS", ""))
