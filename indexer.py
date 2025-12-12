#credit-@MADDY00error
#don't remove credit

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import pymongo
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

#Optional
MONGO_URI = os.getenv("MONGO_URI")
SOURCE_CHANNELS = list(map(int, os.getenv("SOURCE_CHANNELS").split()))
TARGET_CHANNEL = int(os.getenv("TARGET_CHANNEL"))

client = pymongo.MongoClient(MONGO_URI)
db = client["AutoIndexer"]
collection = db["Indexed"]

bot = Client(
    "AutoIndexerBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.channel & filters.chat(SOURCE_CHANNELS))
async def index_files(client, message):

    if not message.media:
        return

    file_id = message.id  
    chat_id = message.chat.id  

    # Prevent duplicate indexing
    exists = collection.find_one({"chat_id": chat_id, "file_id": file_id})
    if exists:
        return

    try:
        forwarded = await message.copy(TARGET_CHANNEL)

        # Save in Mongo
        collection.insert_one({
            "chat_id": chat_id,
            "file_id": file_id,
            "new_message_id": forwarded.id
        })

        print(f"Indexed: {chat_id}/{file_id}")

    except FloodWait as e:
        print(f"Waiting {e.value} seconds due to flood control...")
        await asyncio.sleep(e.value)
    except Exception as ex:
        print(f"Error: {ex}")


print("🤖 Auto Indexer Running...")
bot.run()

