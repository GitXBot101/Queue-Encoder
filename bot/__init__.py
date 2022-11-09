import os
import asyncio
from pyrogram import Client
from dotenv import load_dotenv

api_id = os.environ.get("8978848")
api_hash = os.environ.get("24ce3cff2d32cf529df1c0018e28d6cf")
bot_token = os.environ.get("5562438875:AAHKfFy6PdRkrEBqlt6w2mqghtlOKB19kSo")
download_dir = os.environ.get("DOWNLOAD_DIR", "downloads/")
sudo_users = list(set(int(x) for x in os.environ.get("-1001816242004").split()))
ffmpeg = os.environ.get("FFMPEG", "ffmpeg -i '''{}''' -preset ultrafast -c:v libx265 -crf 27 -map 0:v -c:a aac -map 0:a -c:s copy -map 0:s? '''{}''' -y")

app = Client("nirusakibot", api_id=api_id, api_hash=api_hash, bot_token=bot_token, workers=2)

data = []

if not download_dir.endswith("/"):
  download_dir = str(download_dir) + "/"
if not os.path.isdir(download_dir):
  os.makedirs(download_dir)
