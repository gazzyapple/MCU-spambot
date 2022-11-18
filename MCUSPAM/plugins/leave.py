import asyncio
from MCUSPAM import BOT, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl 
from MCUSPAM.strings import *
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest, InviteToChannelRequest
from telethon import events
import os
import random
import sys

for boti in BOT:
    @boti.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
    async def leave(e):
        if e.sender_id in SUDO_USERS:
            outer_msg = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
            ok = await e.reply("Leaving.....")
            if len(outer_msg[0]) >= 1 :
                chat = outer_msg[0][1:]
                if chat.isdigit() :
                    await ok.edit(left_text)
                    try:    
                        await e.client(LeaveChannelRequest(int(outer_msg[0])))
                    except Exception as s:
                        await ok.edit(str(s))   
                else :
                    await ok.edit(left_text)                   
                    try:
                        await e.client(LeaveChannelRequest(outer_msg[0]))
                    except Exception as s:
                        await ok.edit(str(s)) 
            else:
                await e.reply(module[3] + usage[3]['leave'], parse_mode=None, link_preview=None )   

for boti in BOT:
    @boti.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
    async def join(e):
        users_list = ['@blackwidow0138_bot','@Thor0138_bot','@Captainamerica0138_bot','@Hawkeye0138_bot','@Ironman0138_bot','@Blackpanther0138_bot','@Drstrange0138_bot','@Hulk0138_bot','@Spiderman0138_bot','@Groot0138_bot']
        if e.sender_id in SUDO_USERS:
            outer_msg = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
            ok = await e.reply("Joining.....")
            if len(outer_msg[0]) >= 1 :
                if outer_msg[0][1:].isdigit() :
                    await ok.edit(join_text)
                    try:    
                        await e.client(InviteToChannelRequest(int(outer_msg[0]),users_list))
                    except Exception as s:
                        await ok.edit(str(s))   
                else :
                    await ok.edit(join_text)                   
                    try:
                        await e.client(InviteToChannelRequest(outer_msg[0],users_list))
                    except Exception as s:
                        await ok.edit(str(s)) 
            else:
                await ok.edit(module[3] + usage[3]['join'], parse_mode=None, link_preview=None )  
