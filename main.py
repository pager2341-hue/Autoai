import os
import base64
from telethon import TelegramClient
import asyncio

# GitHub Secret ကနေ Session String ကို ဖတ်ယူပြီး ဖိုင်ပြန်ထုတ်ခြင်း
session_str = os.environ.get('SESSION_STRING')
if session_str:
    with open('session_userbot.session', 'wb') as f:
        f.write(base64.b64decode(session_str))

API_ID = 39359433
API_HASH = '34e0e459bb9dd046a0ed4db3311ea5b8'
client = TelegramClient('session_userbot', API_ID, API_HASH)

async def main():
    await client.start()
    print("GitHub မှာ ဘော့တ် အောင်မြင်စွာ စတင်ပါပြီ!")
    # Bro ရဲ့ တင်မယ့် Logic တွေကို ဒီအောက်မှာ ဆက်ရေးပါ

if __name__ == '__main__':
    asyncio.run(main())


