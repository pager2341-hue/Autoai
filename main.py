from telethon import TelegramClient
import asyncio
import os

API_ID = 39359433                         
API_HASH = '34e0e459bb9dd046a0ed4db3311ea5b8'          

MYANMAR_TARGETS = [-1003157381562, -1003717273116] 
FOREIGN_TARGETS = [-1003828762835]

MY_MYANMAR_CHANNEL = '@abodlppdi'
MY_FOREIGN_CHANNEL = '@ninkopint'

HISTORY_FILE = 'history.txt'

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
    print("Bot စတင်ပြီ...")
    
    while True:
        # 1. မြန်မာကားများ စစ်မယ်
        for target in MYANMAR_TARGETS:
            history = get_history()
            async for message in client.iter_messages(target, limit=1):
                if message.media and message.video and str(message.id) not in history:
                    try:
                        await client.send_file(MY_MYANMAR_CHANNEL, file=message.media, caption="🇲🇲 မြန်မာကား", silent=True)
                        save_history(message.id)
                        print(f"✅ မြန်မာကားတင်ပြီး: {message.id}")
                        await asyncio.sleep(40) 
                    except Exception as e:
                        print(f"Error: {e}")
                        await asyncio.sleep(60)

        # 2. နိုင်ငံခြားကားများ စစ်မယ်
        for target in FOREIGN_TARGETS:
            history = get_history()
            async for message in client.iter_messages(target, limit=1):
                if message.media and message.video and str(message.id) not in history:
                    try:
                        await client.send_file(MY_FOREIGN_CHANNEL, file=message.media, caption="🍿 နိုင်ငံခြားကား", silent=True)
                        save_history(message.id)
                        print(f"✅ နိုင်ငံခြားကားတင်ပြီး: {message.id}")
                        await asyncio.sleep(40)
                    except Exception as e:
                        print(f"Error: {e}")
                        await asyncio.sleep(60)
        
        await asyncio.sleep(30)

if __name__ == '__main__':
    asyncio.run(main())
                      
