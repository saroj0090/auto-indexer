#credit-@MADDY00error
#don't remove credit

import os
from pyrogram import Client, filters

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# space-separated list of source channels  
SOURCE_CHANNELS = [int(x) for x in os.getenv("-1002435736305").split()]
TARGET_CHANNEL = int(os.getenv("-1002636535986"))

app = Client(
    "forward-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.chat(SOURCE_CHANNELS))
async def forward_message(client, message):
    try:
        await message.copy(TARGET_CHANNEL)
        print(f"Forwarded from {message.chat.id}")
    except Exception as e:
        print(f"Error: {e}")

print("Bot is running...")
app.run()


