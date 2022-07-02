import os
import asyncio
from pyrogram import Client
from dotenv import load_dotenv

api_id = int(os.environ.get("7931165"))
api_hash = os.environ.get("5a2e46d1e6deb1456c75aa743bc8e0e6")
bot_token = os.environ.get("5159774583:AAHaIX-f9DmCZWsbAH8X-j6B17BCpM8K6hI")
download_dir = os.environ.get("DOWNLOAD_DIR", "downloads/")
sudo_users = list(set(int(x) for x in os.environ.get("-1001749500356").split()))
ffmpeg = os.environ.get("FFMPEG", "")

app = Client("nirusakibot", api_id=api_id, api_hash=api_hash, bot_token=bot_token, workers=2)

data = []

if not download_dir.endswith("/"):
  download_dir = str(download_dir) + "/"
if not os.path.isdir(download_dir):
  os.makedirs(download_dir)
