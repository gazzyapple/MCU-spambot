
import asyncio
import os
from telethon import events, Button
from telethon.tl.custom import button
from MCUSPAM import BOT, ALIVE_PIC, OWNER_ID, OWNER_NAME, BOT_NAME

START_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/21c096e367555b22a8a22.jpg"


START_Button = [
        [
        Button.url("𝗚𝗿𝗼𝘂𝗽", "https://t.me/MCU_spambot"),
        Button.url(" 𝗥𝗲𝗽𝗼 ", "https://github.com/Spambotmcu/MCU-SPAMBOT")
        ],
        ]
        
#USERS 

for boti in BOT:
    @boti.on(events.NewMessage(incoming=True, pattern='/start'))

    async def start(e):
            if e.chat_id is e.sender_id:
                name = e.sender.first_name
                user_id = e.sender_id
                mention = f"[{name}](tg://user?id={user_id})"
                myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
                creator = f"[BLAZE](tg://user?id={5256676062})"
                START_CAPTION = f"""
                𝐇𝐄𝐘 {mention},
                𝐓𝐇𝐈𝐒 𝐈𝐒 `{BOT_NAME}` 𝐒𝐏𝐀𝐌𝐁𝐎𝐓!
                𝐁𝐎𝐓 𝐎𝐖𝐍𝐄𝐑 :- {myOwner}
                𝐂𝐎𝐃𝐄 𝐂𝐑𝐄𝐀𝐓𝐎𝐑 :- {creator}
                    """
                await e.client.send_file(e.chat_id, START_IMG, caption=START_CAPTION, buttons=START_Button)
