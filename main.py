from telethon import TelegramClient
import asyncio
import os
import base64

API_ID = 39359433                         
API_HASH = '34e0e459bb9dd046a0ed4db3311ea5b8'          

MYANMAR_TARGETS = [-1003157381562, -1003717273116] 
FOREIGN_TARGETS = [-1003828762835]
MY_MYANMAR_CHANNEL = '@abodlppdi'
MY_FOREIGN_CHANNEL = '@ninkopint'
HISTORY_FILE = 'history.txt'

# Session ဖတ်ခြင်း
session_str = os.environ.get('SESSION_STRING')
if session_str:
    with open('session_userbot.session', 'wb') as f:
        f.write(base64.b64decode(session_str))

def get_history():
    if not os.path.exists(HISTORY_FILE): return set()
    with open(HISTORY_FILE, 'r') as f: 
        return set(line.strip() for line in f if line.strip())

def save_history(message_id):
    with open(HISTORY_FILE, 'a') as f: 
        f.write(f"{message_id}\n")

client = TelegramClient('session_userbot', API_ID, API_HASH)

async def main():
    await client.start()
    
    # 1. မြန်မာကား စစ်မယ်
    for target in MYANMAR_TARGETS:
        async for message in client.iter_messages(target, limit=10):
            if message.video and message.video.duration > 60:
                if str(message.id) not in get_history():
                    try:
                        await client.send_file(MY_MYANMAR_CHANNEL, message.media, caption="🇲🇲 မြန်မာကား")
                        save_history(message.id)
                        print(f"✅ မြန်မာကားတင်ပြီး: {message.id}")
                        await asyncio.sleep(5)
                    except: pass

    # 2. နိုင်ငံခြားကား စစ်မယ်
    for target in FOREIGN_TARGETS:
        async for message in client.iter_messages(target, limit=10):
            if message.video and message.video.duration > 60:
                if str(message.id) not in get_history():
                    try:
                        await client.send_file(MY_FOREIGN_CHANNEL, message.media, caption="🍿 နိုင်ငံခြားကား")
                        save_history(message.id)
                        print(f"✅ နိုင်ငံခြားကားတင်ပြီး: {message.id}")
                        await asyncio.sleep(5)
                    except: pass

if __name__ == '__main__':
    asyncio.run(main())
    
