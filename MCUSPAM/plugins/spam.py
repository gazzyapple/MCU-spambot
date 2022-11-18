async def gifspam(e, file1):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=file1.media.document.id,
                    access_hash=file1.media.document.access_hash,
                    file_reference=file1.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

import asyncio
import random
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from MCUSPAM import BOT, first_bot, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from MCUSPAM.strings import *
from resources.data import HUG, SLAP, DANCE
from MCUSPAM.utils import check_restrictions

for boti in BOT:
    @boti.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
    async def spam(e):
        if e.sender_id in SUDO_USERS: 
            outer_msg = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
            replied_msg = await e.get_reply_message()
            if len(outer_msg[0])>=1 and not e.reply_to_msg_id: 
                try:
                    counter = int(outer_msg[0])
                except Exception:
                    return await e.reply(count_e_text)
                try:
                    message = str(outer_msg[1])
                except Exception as s:
                    return await e.reply(msg_e_text)
                if counter > 100:
                    return await e.reply(bigspam_e_text)
                return await asyncio.wait([e.respond(message) for i in range(counter)])
            elif e.reply_to_msg_id and replied_msg.media:
                try:
                    counter = int(outer_msg[0])
                except Exception:
                    return await e.reply(count_e_text)
                if counter > 100:
                    return await e.reply(bigspam_e_text)
                for _ in range(counter):
                    replied_msg = await e.client.send_file(e.chat_id, replied_msg, caption=replied_msg.text,reply_to=e.id)
                    await gifspam(e, replied_msg)
            elif e.reply_to_msg_id and replied_msg.text:
                message = replied_msg.text
                try:
                    counter = int(outer_msg[0])
                except Exception:
                    return await e.reply(count_e_text)
                if counter > 100:
                    return await e.reply(bigspam_e_text)
                await asyncio.wait([e.respond(message) for i in range(counter)])
            else:
                await e.reply(module[0]+usage[0]['spam'])

for boti in BOT:
    @boti.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
    async def bigspam(e):
        if e.sender_id in SUDO_USERS:
            if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
                return await e.reply(usage)
            outer_msg = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
            replied_msg = await e.get_reply_message()
            if len(outer_msg[0]) >= 1 and not e.reply_to_msg_id: 
                try:
                    counter = int(outer_msg[0])
                except Exception:
                    return await e.reply(count_e_text)
                try:
                    message = str(outer_msg[1])
                except Exception as s:
                    return await e.reply(msg_e_text)
                for _ in range(counter):
                     async with e.client.action(e.chat_id, "typing"):
                         if e.reply_to_msg_id:
                              await replied_msg.reply(message)
                         else:
                              await e.client.send_message(e.chat_id, message)
                     await asyncio.sleep(0.3)
            elif e.reply_to_msg_id and replied_msg.media:  
                try:
                    counter = int(outer_msg[0])
                except Exception:
                    return await e.reply(count_e_text)
                for _ in range(counter):
                    async with e.client.action(e.chat_id, "document"):
                        replied_msg = await e.client.send_file(e.chat_id, replied_msg, caption=replied_msg.text,reply_to=e.id)
                        await gifspam(e, replied_msg) 
                    await asyncio.sleep(0.3)  
            elif e.reply_to_msg_id and replied_msg.text:
                message = replied_msg.text
                try:
                    counter = int(outer_msg[0])
                except Exception:
                    return await e.reply(count_e_text)            
                for _ in range(counter):
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, message)
                        await asyncio.sleep(0.3)
            else:
                await e.reply(module[0]+usage[0]['bigspam'])

for boti in BOT:
    @boti.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
    async def delayspam(e):
        if e.sender_id in SUDO_USERS: 
            if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
                return await e.reply(usage)
            replied_msg = await e.get_reply_message()
            outer_msg = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)        
            if len(outer_msg[0]) >= 1 and not e.reply_to_msg_id:
                try:
                    sleeptime = float(outer_msg[0])
                except Exception:
                    return await e.reply(delay_e_text)
                try:
                    counter = int(outer_msg[1])
                except Exception:
                    return await e.reply(count_e_text)
                try:
                    message = str(outer_msg[2])
                except Exception as s:
                    return await e.reply(msg_e_text)
                for _ in range(counter):
                    async with e.client.action(e.chat_id, "typing"):
                        if e.reply_to_msg_id:
                            await replied_msg.reply(message)
                        else:
                            await e.client.send_message(e.chat_id, message)
                        await asyncio.sleep(sleeptime)
            elif e.reply_to_msg_id and replied_msg.media:
                try:
                    sleeptime = float(outer_msg[0])
                except Exception:
                    return await e.reply(delay_e_text)
                try:
                    counter = int(outer_msg[1])
                except Exception:
                    return await e.reply(count_e_text)

                for _ in range(counter):
                    async with e.client.action(e.chat_id, "document"):
                        replied_msg = await e.client.send_file(e.chat_id, replied_msg, caption=replied_msg.text,reply_to=e.id)
                        await gifspam(e, replied_msg)
                    await asyncio.sleep(sleeptime)
            elif e.reply_to_msg_id and replied_msg.text:
                message = replied_msg.text
                try:
                    sleeptime = float(outer_msg[0])
                except Exception:
                    return await e.reply(delay_e_text)
                try:
                    counter = int(outer_msg[1])
                except Exception:
                    return await e.reply(count_e_text)
                for _ in range(counter):
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, message)
                        await asyncio.sleep(sleeptime)
            else:
                await e.reply(module[0]+usage[0]['delayspam'])
                
for boti in BOT:
    @boti.on(events.NewMessage(incoming=True, pattern=r"\%sdspam(?: |$)(.*)" % hl))
    @boti.on(events.NewMessage(incoming=True, pattern=r"\%shspam(?: |$)(.*)" % hl))
    @boti.on(events.NewMessage(incoming=True, pattern=r"\%ssspam(?: |$)(.*)" % hl))
    async def nspam(e):
        if e.sender_id in SUDO_USERS:
            replied_msg = await e.get_reply_message()
            outer_msg = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)  
            if len(outer_msg[0]) >= 1 and not e.reply_to_msg_id:
                counter = 0
                if outer_msg[0].isdigit():
                    counter = int(outer_msg[0])
                else:
                    return await e.reply(count_e_text)
                spam_select = e.text[1]
                restrict = check_restrictions(e.chat_id)
                if restrict == None:
                 for _ in range(counter):
                     reply = get_select_reply(spam_select)
                     async with e.client.action(e.chat_id, "document"):
                         sendingfile = await e.client.send_file(e.chat_id, reply)
                         await gifspam(e, sendingfile) 
                     await asyncio.sleep(0.4)
                 return
                else:
                      return await e.reply(restrict)
            elif e.reply_to_msg_id and (replied_msg.text or replied_msg.media):
                try:
                    counter = int(outer_msg[0])
                except Exception:
                    return await e.reply(count_e_text)
                spam_select = e.text[1]
                restrict = check_restrictions(e.chat_id)
                if restrict == None:
                 for _ in range(counter):           
                     reply = get_select_reply(spam_select)
                     async with e.client.action(e.chat_id, "document"):
                         sendingfile = await e.client.send_file(e.chat_id, reply,reply_to=e.id)
                         await gifspam(e, sendingfile) 
                     await asyncio.sleep(0.4)
                 return
                else:
                     return await e.reply(restrict)
            else:
                await e.reply(module[0]+usage[0]['nspam'])
                
def get_select_reply(select):
    if select == 'h': 
        reply = random.choice(HUG)
    elif select == 's': 
        reply = random.choice(SLAP)
    elif select == 'd':
        reply = random.choice(DANCE)
    else:
        reply = random.choice(HUG)
    return reply
           
