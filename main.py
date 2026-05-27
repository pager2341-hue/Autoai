from telethon import TelegramClient
import asyncio
import os
import base64

API_ID = 39359433                         
API_HASH = '34e0e459bb9dd046a0ed4db3311ea5b8'          

MYANMAR_TARGETS = [-1003157381562, -1003717273116] 
FOREIGN_TARGETS = [-1003828762835]

# Channel username တွေအစား ID အရှည်ကြီးကို သုံးရင် ပိုသေချာပါတယ်
MY_MYANMAR_CHANNEL = -1002241696035 # @abodlppdi ရဲ့ ID (Telegram မှာ စစ်ကြည့်ပါ)
MY_FOREIGN_CHANNEL = -1002012345678 # @ninkopint ရဲ့ ID

HISTORY_FILE = 'history.txt'

# (Session ဖတ်တဲ့ Code တွေ ဒီနေရာမှာ ထည့်ပါ)

client = TelegramClient('session_userbot', API_ID, API_HASH)

async def main():
    await client.start()
    print("Bot စတင်ပြီ...")
    
    while True:
        # 1. မြန်မာကားများ စစ်မယ်
        for target in MYANMAR_TARGETS:
            async for message in client.iter_messages(target, limit=5):
                # Video ဖြစ်ရမယ် + 60 စက္ကန့် (၁ မိနစ်) ကျော်ရမယ်
                if message.video and message.video.duration > 60:
                    if str(message.id) not in get_history():
                        try:
                            await client.send_file(MY_MYANMAR_CHANNEL, file=message.media, caption="🇲🇲 မြန်မာကား (၁ မိနစ်ကျော်)")
                            save_history(message.id)
                            print(f"✅ တင်ပြီးပြီ: {message.id}")
                            await asyncio.sleep(10)
                        except Exception as e:
                            print(f"Error: {e}")

        # 2. နိုင်ငံခြားကားများ စစ်မယ်
        for target in FOREIGN_TARGETS:
            async for message in client.iter_messages(target, limit=5):
                if message.video and message.video.duration > 60:
                    if str(message.id) not in get_history():
                        try:
                            await client.send_file(MY_FOREIGN_CHANNEL, file=message.media, caption="🍿 နိုင်ငံခြားကား (၁ မိနစ်ကျော်)")
                            save_history(message.id)
                            print(f"✅ တင်ပြီးပြီ: {message.id}")
                            await asyncio.sleep(10)
                        except Exception as e:
                            print(f"Error: {e}")
        
        await asyncio.sleep(60)

