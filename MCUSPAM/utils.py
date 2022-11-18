import sys
import logging
import importlib
from telethon import events
from pathlib import Path
import inspect
import re
import aiohttp
from MCUSPAM import LOG_FILE_NAME, LOGGER, OWNER_ID, SUDO_USERS, SAFE_USERS, SAFE_GROUPS
from MCUSPAM.strings import *

def load_plugins(plugin_name):
    path = Path(f"MCUSPAM/plugins/{plugin_name}.py")
    name = "MCUSPAM.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
#     load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["MCUSPAM.plugins." + plugin_name] = load
    LOGGER("MCUSPAM ").info("[INFO] Successfully Imported " + plugin_name)

async def edit_or_reply(event, text):
    if event.sender_id in SUDO_USERS:
        reply_to = await event.get_reply_message()
        if reply_to:
            return await reply_to.reply(text)
        return await event.reply(text)
    return await event.edit(text)
       
def check_restrictions(user_id):
    if user_id in SAFE_USERS:
        reply = safe_r_text
    elif user_id == OWNER_ID:
        reply = owner_r_text
    elif user_id in SUDO_USERS:
        reply = sudo_r_text
    elif user_id in SAFE_GROUPS:
        reply = safeg_r_text
    else:
        reply = None
    return reply


BASE = "https://batbin.me/"
async def post(url: str, *args, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, *args, **kwargs) as resp:
            try:
                data = await resp.json()
            except Exception:
                data = await resp.text()
        return data

async def linkbin(text):
    resp = await post(f"{BASE}api/v2/paste", data=text)
    if not resp["success"]:
        return
    link = BASE + resp["message"]
    return link
