import asyncio
import sys
from sys import argv
import glob
import logging
from pathlib import Path
from telethon import events
from MCUSPAM.utils import load_plugins
from . import BOT, LOGGER
  
path = "MCUSPAM/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

deployed = "🎉 Successfully Deployed MCU SpamBot 🎉 @MCU_SPAM_BOT Enjoy!"
LOGGER("MCUSPAM ").info(deployed[0: ])

for i in range(len(BOT)):
    if __name__ == "__main__":
        BOT[i].run_until_disconnected()



