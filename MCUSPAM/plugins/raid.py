
import asyncio
import base64
import os
import random        
from telethon import events,functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from resources.data import RAID, BRAID, QRAID, FRAID, ERAID
from MCUSPAM import BOT, first_bot,SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from MCUSPAM.strings import *
from MCUSPAM.utils import check_restrictions

que = {}

for boti in BOT:
    @boti.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
    @boti.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
    @boti.on(events.NewMessage(incoming=True, pattern=r"\%seraid(?: |$)(.*)" % hl))
    @boti.on(events.NewMessage(incoming=True, pattern=r"\%svraid(?: |$)(.*)" % hl))
    @boti.on(events.NewMessage(incoming=True, pattern=r"\%sfraid(?: |$)(.*)" % hl))
    async def nraid(e): 
        if e.sender_id in SUDO_USERS:
            if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
                return await first_bot.client.e.reply("usage")
            outer_msg = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
            if len(outer_msg[0]) >=1 and not e.reply_to_msg_id:      
                try:
                    counter = int(outer_msg[0])
                except Exception:
                    return await e.reply(count_e_text)
                try:
                    message = str(outer_msg[1])
                except Exception as s:
                    return await e.reply(user_e_text)
                try:     
                    user = await e.client.get_entity(outer_msg[1])
                except Exception as s:
                    return await e.reply(str(s)) 
                restrict = check_restrictions(int(user.id))
                if restrict == None:     
                    await do_raid(counter,user,e)
                    return
                else:
                    return await e.reply(restrict) 
            elif e.reply_to_msg_id:      
                try:
                    counter = int(outer_msg[0])
                except Exception:
                    return await e.reply(count_e_text)
                replied_msg = await e.get_reply_message()
                replied_user = await e.client.get_entity(replied_msg.sender_id) 
                restrict = check_restrictions(int(replied_user.id))
                if restrict == None:
                    await do_raid(counter,replied_user,e)
                    return
                else:
                    return await e.reply(restrict)
            else:
                await e.reply(module[1]+usage[1]['nraid'])
    
for boti in BOT:
    @boti.on(events.NewMessage(incoming=True))
    async def _(event):
        global que
        queue = que.get(event.sender_id)
        if not queue:
            return
        async with event.client.action(event.chat_id, "typing"):
            await asyncio.sleep(0.2)
        async with event.client.action(event.chat_id, "typing"):
            await event.client.send_message(
                entity=event.chat_id,
                message="""{}""".format(random.choice(REPLYRAID)),
                reply_to=event.message.id,
            )

for boti in BOT:
    @boti.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
    async def replyraid(e):
        global que
        if e.sender_id in SUDO_USERS:
            outer_msg = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
            if len(outer_msg[0]) >= 1 and not e.reply_to_msg_id:
                try:
                    message = str(outer_msg[0])
                except Exception as s:
                    return await e.reply(user_e_text)
                try:     
                    user = await e.client.get_entity(str(outer_msg[0]))
                except Exception as s:
                    return await e.reply(str(s)) 
                restrict = check_restrictions(int(user.id))
                if restrict == None:
                    user_id = int(user.id)
                    que[user_id] = []
                    gey = que.get(user_id)
                    phucker = [user_id]
                    gey.append(phucker)
                    await e.reply(replyraid_a_text)
                    return 
                else:
                    return await e.reply(restrict)
            elif e.reply_to_msg_id:             
                replied_msg = await e.get_reply_message()
                replied_user = await e.client.get_entity(replied_msg.sender_id) 
                restrict = check_restrictions(int(replied_user.id))
                if restrict == None:
                    user_id = int(replied_user.id)
                    que[user_id] = []
                    gey = que.get(user_id)
                    phucker = [user_id]
                    gey.append(phucker)
                    await e.reply(replyraid_a_text)
                    return
                else:
                    return await e.reply(restrict)
            else:
                await e.reply(module[1]+usage[1]['replyraid'])
                
for boti in BOT:
    @boti.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
    async def dreplyraid(e):
        global que    
        if e.sender_id in SUDO_USERS:
            if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
                return await first_bot.client.e.reply(usage)
            outer_msg = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
            if len(outer_msg[0]) >= 1 and not e.reply_to_msg_id:   
                try:
                    message = str(outer_msg[0])
                except Exception as s:
                    return await e.reply(user_e_text)
                try:     
                    user = await e.client.get_entity(str(outer_msg[0]))
                except Exception as s:
                    return await e.reply(str(s)) 
                try:
                    queue = que.get(user.id)
                    queue.pop(0)
                except Exception as f:
                    return await e.reply(replyraid_ad_text)
                await e.reply(replyraid_d_text)
            elif e.reply_to_msg_id:             
                replied_msg = await e.get_reply_message()
                replied_user = await e.client.get_entity(replied_msg.sender_id)
                try:
                    queue = que.get(replied_user.id)
                    queue.pop(0)
                except Exception as f:
                    return await e.reply(replyraid_ad_text)
                await e.reply(replyraid_d_text)
            else:
                await e.reply(module[1]+usage[1]['dreplyraid'])

for i, boti in enumerate(BOT):
    @boti.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
    async def delayraid(e):
       if e.sender_id in SUDO_USERS:
             if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
                return await e.reply(usage, parse_mode=None, link_preview=None )
             outer_msg = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
             if len(outer_msg[0]) >= 1 and not e.reply_to_msg_id:   
                 try:
                    counter = int(outer_msg[0])
                 except Exception:
                    return await e.reply(count_e_text)
                 try:
                        sleeptimet = sleeptimem = float(outer_msg[1])
                 except Exception:
                    return await e.reply(delay_e_text)    
                 try:
                    message = str(outer_msg[2])
                 except Exception as s:
                    return await e.reply(user_e_text)
                 try:     
                    user = await e.client.get_entity(outer_msg[2])
                 except Exception as s:
                    return await e.reply(str(s)) 
                 restrict = check_restrictions(int(user.id))
                 if restrict == None:      
                     await do_raid(counter,user,e,sleeptimem)
                     return
                 else:
                    return await e.reply(restrict) 
             elif e.reply_to_msg_id:
                   try:
                        sleeptimet = sleeptimem = float(outer_msg[0])
                   except Exception:
                        return await e.reply(delay_e_text)           
                   try:
                        counter = int(outer_msg[1])
                   except Exception:
                        return await e.reply(count_e_text)
                   replied_msg = await e.get_reply_message()
                   try:
                      replied_user = await e.client.get_entity(replied_msg.sender_id)
                   except Exception as s:
                      return await e.reply(str(s)) 
                   restrict = check_restrictions(int(replied_user.id))
                   if restrict == None:  
                       await do_raid(counter,replied_user,e,sleeptimem)
                       return
                   else:
                       return await e.reply(restrict)
             else:
                    await e.reply(module[1]+usage[1]['delayraid'])
                    
#                 print(f"{i} : {event.id}")
#                 print(f"bot : {first_bot} = {boti}")
#                 if first_bot is boti :
#                     prin("Matched")
#                     await first_bot.send_message(event.peer_id.channel_id,message=usage, reply_to=event.id)
                #event.sender_id - one who typing the msg - event.id - typed msg's object event id, event.reply_to_msg_id - reply msg id
                #event.peer_id.channel_id - id of the channel where event created
#                await event.reply(usage)

def get_select_reply(select):
    if select == 'f': 
        reply = random.choice(FRAID)
    elif select == 'v': 
        reply = random.choice(VRAID)
    elif select == 'b': 
        reply = random.choice(BRAID)
    elif select == 'e':
        emoji_list_key = list(ERAID)
#         len_e = len(emoji_list_key)
#         reply = EMOJI_DICT[emoji_list_key[random.randrange(0,len_e)]]
        reply = ERAID[random.choice(emoji_list_key)]
    else:
        reply = random.choice(RAID)
    return reply

async def do_raid(counter,raid_user,e,sleeptimem = 0.5):               
   username = f"[{raid_user.first_name}](tg://user?id={raid_user.id})"
   for _ in range(counter):                            
        reply = get_select_reply(e.text[1])
        caption = f"{username} {reply}"
        async with e.client.action(e.chat_id, "typing"):
             await e.client.send_message(e.chat_id, caption)
             await asyncio.sleep(sleeptimem)
