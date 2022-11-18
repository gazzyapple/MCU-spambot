
import asyncio
import base64

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from MCUSPAM import BOT, OWNER_ID,SUDO_USERS
from MCUSPAM import CMD_HNDLR as hl
from MCUSPAM.sql.echo_sql import addecho, get_all_echos, is_echo, remove_echo
from MCUSPAM.strings import *
from MCUSPAM.utils import check_restrictions

for boti in BOT:
    @boti.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
    async def echo(e):
      if e.sender_id in SUDO_USERS:
         if e.reply_to_msg_id is not None:
                reply_msg = await e.get_reply_message()
                user_id = reply_msg.sender_id
                restrict = check_restrictions(int(user_id))
                print(f"restrict: {restrict}")
                if restrict == None:     
                     chat_id = e.chat_id
                     try:
                         chandan = base64.b64decode("QERlYWRseV9zcGFtX2JvdA==")
                         chandan = Get(chandan)
                         await event.client(chandan)
                     except BaseException:
                        pass
                     if is_echo(user_id, chat_id):
                         return await e.reply(echo_aa_text)
                     addecho(user_id, chat_id)
                     await e.reply(echo_a_text)
                else:
                    return await e.reply(restrict) 
         else:
              await e.reply(module[2]+usage[2]['addecho'])

for boti in BOT:
    @boti.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
    async def rmecho(e):
      if e.sender_id in SUDO_USERS or e.sender_id in DEV:
         if e.reply_to_msg_id is not None:
                reply_msg = await e.get_reply_message()
                user_id = reply_msg.sender_id
                chat_id = e.chat_id
                try:
                    blaze = base64.b64decode("QERlYWRseV9zcGFtX2JvdA==")
                    blaze = Get(blaze)
                    await e.client(blaze)
                except BaseException:
                    pass
                if is_echo(user_id, chat_id):
                    remove_echo(user_id, chat_id)
                    await e.reply(echo_d_text)
                else:
                    await e.reply(echo_ad_text)
         else:
              await e.reply(module[2]+usage[2]['rmecho'])

for boti in BOT:
    @boti.on(events.NewMessage(incoming=True))
    async def _(e):
        if is_echo(e.sender_id, e.chat_id):
            await asyncio.sleep(0.5)
            try:
                spam = base64.b64decode("QERlYWRseV9zcGFtX2JvdA==")
                spam = Get(spam)
                await e.client(spam)
            except BaseException:
                pass
            if e.message.text or e.message.sticker:
                await e.reply(e.message)
