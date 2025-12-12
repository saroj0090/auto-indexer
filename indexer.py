#credit-@MADDY00error
#don't remove credit

import os
from pyrogram import Client, filters

API_ID = int(os.getenv("28057612"))
API_HASH = os.getenv("95295dca0ca9f41855ec0cabe9b440ed")
BOT_TOKEN = os.getenv("7715353540:AAG9tE3FFxy2d8mbcmYn-CNgukwTPPafs3A")

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


