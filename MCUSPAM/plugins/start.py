
import asyncio
import os
from telethon import events, Button
from telethon.tl.custom import button
from MCUSPAM import BOT, ALIVE_PIC, OWNER_ID, OWNER_NAME, BOT_NAME

START_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/21c096e367555b22a8a22.jpg"


START_Button = [
        [
        Button.url("ππΏπΌππ½", "https://t.me/MCU_spambot"),
        Button.url(" π₯π²π½πΌ ", "https://github.com/Spambotmcu/MCU-SPAMBOT")
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
                πππ {mention},
                ππππ ππ `{BOT_NAME}` πππππππ!
                πππ πππππ :- {myOwner}
                ππππ πππππππ :- {creator}
                    """
                await e.client.send_file(e.chat_id, START_IMG, caption=START_CAPTION, buttons=START_Button)
