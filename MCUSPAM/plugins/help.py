from MCUSPAM import first_bot,SUDO_USERS,BOT_NAME,ALIVE_PIC,LOGGER,OWNER_ID
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from MCUSPAM import CMD_HNDLR as hl
from MCUSPAM.strings import *
    
SPAMBOT_NAME = BOT_NAME if BOT_NAME else "MCU"

HELP_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/21c096e367555b22a8a22.jpg"

HELP_CAPTION = f"🔥{SPAMBOT_NAME} Spambot 🔥 \n(For entertainment purposes only)\n\n"
 
HELP_CAPTION += f"**BOT CMDS**\n\n"

HELP_CAPTION += f"`{hl}ping` - to check ping \n`{hl}alive` - to check bot alive \n`{hl}restart` - to restart all spam bots \n`{hl}addecho` - to addecho \n`{hl}rmecho` - To remove Echo\n" 
HELP_CAPTION += f"`{hl}leave` - to make bots leave the chat\n`{hl}changename` - to change spambot name\n`{hl}changepic` - to change bot alive/help pic used\n\n"

HELP_CAPTION2 = f"**ADVANCED CMDS** (Limited for owners)\n\n"

HELP_CAPTION2 += f"`{hl}listsudo` - to list all sudo users \n`{hl}addsudo` - to add sudo user \n`{hl}delsudo` - to remove sudo user\n"
HELP_CAPTION2 += f"`{hl}changehl` - to change command handler\n`{hl}showbt` - to print all bot tokens used\n"
HELP_CAPTION2 += f"`{hl}getlog` `{hl}usage_dynos` `{hl}setvar` `{hl}getvar`\n\n"

HELP_CAPTION3 = f"**RAID & SPAM CMDS**\n\n"

HELP_CAPTION3 += f"`{hl}nraid` - to raid user with \n (select n prefix => e for emoji😀, f for flirtline🌚, v for quotes😇,b for birthday wishes!🎂)\n"  
HELP_CAPTION3 += f"`{hl}replyraid` - to active reply raid\n`{hl}dreplyraid` - to de-active reply raid\n\n"

HELP_CAPTION3 += f"`{hl}nspam` - to spam user gif/images with \n (select n prefix => h for hugs🤗, s for slaps🤚, d for dance🕺)\n"
HELP_CAPTION3 += f"`{hl}spam` - for normal spam text/stickers \n`{hl}bigspam` - for big spam ( > 100)\n`{hl}delayspam` - to spam with some delay\n\n"

HELP_CAPTION3 += f"Edited By - @Cheems_huehuehue\n"

@first_bot.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):   
    Cheems_ID = 5593869533
    if event.sender_id == OWNER_ID or event.sender_id == Cheems_ID:
      CAPTION = HELP_CAPTION + HELP_CAPTION2 + HELP_CAPTION3
      return await first_bot.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=CAPTION,
                                  buttons=[
        [
        Button.url("Active Comrades ", "https://t.me/MCU_spambot"),
        ] 
        ]
        )
    if event.sender_id in SUDO_USERS:
      CAPTION = HELP_CAPTION + HELP_CAPTION3
      return await first_bot.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=CAPTION,
                                  buttons=[
        [
        Button.url("Active Comrades ", "https://t.me/MCU_spambot"),
        ] 
        ]
        )
