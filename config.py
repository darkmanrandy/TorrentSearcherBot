import os

TOKEN = os.environ.get("BOT_TOKEN")
API_HASH = os.environ.get("API_HASH")
API_ID = int(os.environ.get("API_ID"))
START_MESSAGE = os.environ.get("START_MESSAGE", "<b>Hi! I'm ∪∩∩᭄_1997 - a simple  torrent file search engine...\n\n\nMade with 🐍 by @gangstertamizhan</b>")
FOOTER_TEXT = os.environ.get("FOOTER_TEXT", "<b>Create by @gangstertamizhan 😎</b>")
TORRENTS = {}
