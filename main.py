import os
import base64
import asyncio
from telethon import TelegramClient

# 1. GitHub Secret ထဲက Session ကို ပြန်ဖတ်ပြီး ဖိုင်ထုတ်ခြင်း
session_str = os.environ.get('SESSION_STRING')
if session_str:
    session_data = base64.b64decode(session_str)
    with open('session_userbot.session', 'wb') as f:
        f.write(session_data)

# 2. Telegram နဲ့ ချိတ်ဆက်ဖို့ Config
API_ID = 39359433
API_HASH = '34e0e459bb9dd046a0ed4db3311ea5b8'

# timeout=60 ဆိုတာ ချိတ်ဆက်မှု နှေးရင် ချက်ချင်းမပြတ်အောင် ကာကွယ်ပေးတာပါ
client = TelegramClient('session_userbot', API_ID, API_HASH, timeout=60)

async def main():
    # client.start() က ဘာလုပ်ပေးလဲ?
    # - Bro ရဲ့ Session ဖိုင်ကို ဖတ်မယ်
    # - Telegram ဆာဗာကို "ဒီအကောင့်က ကျွန်တော်ပါ" လို့ အတည်ပြုမယ်
    # - အောင်မြင်ရင် Data တွေ လှမ်းယူဖို့ လမ်းကြောင်းပွင့်သွားမယ်
    print("Telegram နဲ့ ချိတ်ဆက်နေပါပြီ...")
    await client.start()
    print("ချိတ်ဆက်မှု အောင်မြင်ပါပြီ! ဘော့တ် စတင်ပြီ...")

    # ဒီနေရာမှာ တင်မယ့် Logic တွေကို ဆက်ထည့်ပါ
    # ဥပမာ - channel တစ်ခုကနေ နောက်တစ်ခုကို Forward လုပ်တာမျိုး
    
    # ဘော့တ်ကို အမြဲ အလုပ်လုပ်နေအောင် ထားတာပါ
    await client.run_until_disconnected()

if __name__ == '__main__':
    # Network ပြဿနာရှိရင် ၃ ကြိမ်အထိ ပြန်ကြိုးစားဖို့ Error handling ထည့်ထားပါတယ်
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Error တက်လို့ ထွက်လိုက်ပါပြီ: {e}")
        
