import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from config import API_ID, API_HASH, STRING_SESSION

jmthon = TelegramClient(StringSession(str(STRING_SESSION)), int(API_ID), str(API_HASH)).start()
loop = asyncio.get_event_loop()


print("تم التنصيب")
jmthon.run_until_disconnected()
