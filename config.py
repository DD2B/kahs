from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID")
APP_HASH = os.environ.get("APP_HASH")
BOT_USERNAME = ("hha2hbot")
SESSION1 = os.environ.get("TERMUX")
token = ("6276696273:AAHE-aoWtFGPjyohuDAG0YecDW1hdQlyKZo")
DEVLOO = os.environ.get("DEVLO")
CHNA = os.environ.get("CHNA")
jalithon = TelegramClient(StringSession(SESSION1), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)


ispay = ['yes']
ispay2 = ['yes']
bot.start()

