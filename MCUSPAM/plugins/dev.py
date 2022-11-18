import os
import asyncio
import requests
import sys
import time

# Changed root to MCUSPAM
from MCUSPAM import BOT,first_bot,OWNER_ID, SUDO_USERS,CMD_HNDLR as hl
from MCUSPAM.utils import linkbin
from telethon import events, version, Button
from telethon.tl.custom import button
from datetime import datetime

# from telegraph import upload_file as uf
# import Telegraph
# from PIL import Image

# # Used for Formatting Eval Code, if installed
# # try:
# #     import black
# # except ImportError:
# #     black = None
# from pprint import pprint

# try:
#     from yaml import safe_load
# except ImportError:
#     from pyUltroid.fns.tools import safe_load
# # try:
# #     from telegraph import upload_file as uf
# # except ImportError:
# #     uf = None

import inspect
import sys
import traceback
from io import BytesIO, StringIO
from os import remove
from random import choice

from telethon.utils import get_display_name
from telethon.tl import functions
fn = functions

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

@first_bot.on(events.NewMessage(incoming=True, pattern=r"\%stelegraph(?: |$)(.*)" % hl))
async def telegraph(event):
    links = "Links: \n"
    errors = []
    if not event.reply_to_msg_id:
        delete = 0
        non_media = 0
        async for message in first_bot.iter_messages(event.chat_id):
          getit = await first_bot.download_media(message)
          if getit:
            try:
                nn = f"https://graph.org{first_bot.upload_file(getit)[0]}"
                links += f"{nn}\n"
            except Exception as e:
                errors.append(f"{message.id} : {e}")
            # await asyncio.sleep(7)

            os.remove(getit) 
            delete += 1
          else:
            non_media += 1
        output = f"Total failed to Upload: {len(errors)}\n {errors}"
        output += f"Total Downloaded & Deleted: {delete}"
        output += f"Total Non-Media msg: {non_media}"

        await event.reply(output, link_preview = False)
        return await event.reply(links,link_preview = False)
    else:
        reply = await event.get_reply_message()
        getit = await reply.download_media()
        print(getit)
        if getit:
            try:
                nn = f"https://graph.org{await first_bot.upload_file(getit)}"
                links += f"{nn}\n"
            except Exception as e:
                nn = f"{mediainfo(reply.media)} : {e}"
            # await asyncio.sleep(7)
            await event.reply(nn, link_preview = False)
            os.remove(getit) 
        else:
            await event.reply("non-media", link_preview = False)

@first_bot.on(events.NewMessage(incoming=True, pattern=r"\%sbash(?: |$)(.*)" % hl))
async def bashcmd(event):
    carb, yamlf = None, False
    try:
        cmd = event.text.split(" ", maxsplit=1)[1]
        if cmd.split()[0] in ["-c", "--carbon"]:
            cmd = cmd.split(maxsplit=1)[1]
            carb = True
    except IndexError:
        return await event.reply("`No cmd given`", time=10)
    xx = await event.reply("`Processing...`")
    reply_to_id = event.reply_to_msg_id or event.id
    stdout, stderr = await bash(cmd, run_code=1)
    OUT = f"**☞ BASH\n\n• COMMAND:**\n`{cmd}` \n\n"
    err, out = "", ""
    if stderr:
        err = f"**• ERROR:** \n`{stderr}`\n\n"
    if stdout:
         ###### CARBON #####
        print(f"{carb} : {stderr}")
        if (carb) and not stderr and (event.is_private or event.chat.admin_rights or event.chat.creator
            or event.chat.default_banned_rights.embed_links ):
                print(f"inside {carb} : {stderr}")
                link = await linkbin(stdout)
                out = link
        else:
            if "pip" in cmd and all(":" in line for line in stdout.split("\n")):
                try:
                    load = safe_load(stdout)
                    stdout = ""
                    for data in list(load.keys()):
                        res = load[data] or ""
                        if res and "http" not in str(res):
                            res = f"`{res}`"
                        stdout += f"**{data}**  :  {res}\n"
                    yamlf = True
                except Exception as er:
                    stdout = f"`{stdout}`"
                    LOGS.exception(er)
            else:
                stdout = f"`{stdout}`"
            out = f"**• OUTPUT:**\n{stdout}"
    if not stderr and not stdout:
        out = "**• OUTPUT:**\n`Success`"
    OUT += err + out
    if len(OUT) > 4096:
        ultd = err + out
        with BytesIO(str.encode(ultd)) as out_file:
            out_file.name = "bash.txt"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
#                 thumb=ULTConfig.thumb,
                allow_cache=False,
                caption=f"`{cmd}`" if len(cmd) < 998 else None,
                reply_to=reply_to_id,
            )

            await xx.delete()
    else:
        await xx.edit(OUT, link_preview=not yamlf)


# pp = pprint  # ignore: pylint
bot = ultroid = ultroid_bot = first_bot

class u:
    ...

def _parse_eval(value=None):
    if not value:
        return value
    if hasattr(value, "stringify"):
        try:
            return value.stringify()
        except TypeError:
            pass
    elif isinstance(value, dict):
        try:
            return json_parser(value, indent=1)
        except BaseException:
            pass
    return str(value)

# @ultroid_cmd(pattern="eval", fullsudo=True, only_devs=True)
@first_bot.on(events.NewMessage(incoming=True, pattern=r"\%seval(?: |$)(.*)" % hl))
async def _(event):
    try:
        cmd = event.text.split(maxsplit=1)[1]
    except IndexError:
        return await event.reply("`Give some python cmd`", time=5)
    silent, gsource, xx = False, False, None
    spli = cmd.split()

    async def get_():
        try:
            cm = cmd.split(maxsplit=1)[1]
        except IndexError:
            cm = None
        return cm

    if spli[0] in ["-s", "--silent"]:
        await event.delete()
        silent = True
        cmd = await get_()
    elif spli[0] in ["-n", "-noedit"]:
        cmd = await get_()
        xx = await event.reply("`Processing...`")
    elif spli[0] in ["-gs", "--source"]:
        gsource = True
        cmd = await get_()
    if not cmd:
        xx = await event.reply("->> Wrong Format <<-")
        return
    if not silent:
        xx = await event.reply("`Processing...`")
    # if black:
    #     try:
    #         cmd = black.format_str(cmd, mode=black.Mode())
    #     except BaseException:
    #         # Consider it as Code Error, and move on to be shown ahead.
    #         pass
    reply_to_id = event.reply_to_msg_id or event
    
    # if any(item in cmd for item in KEEP_SAFE().All) and (
    #     not (event.out or event.sender_id == first_bot.uid)
    # ):
    #     warning = await event.forward_to(udB.get_key("LOG_CHANNEL"))
    #     await warning.reply(
    #         f"Malicious Activities suspected by {inline_mention(await event.get_sender())}"
    #     )
    #     _ignore_eval.append(event.sender_id)
    #     return await xx.edit(
    #         "`Malicious Activities suspected⚠️!\nReported to owner. Aborted this request!`"
    #     )
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc, timeg = None, None, None, None
    tima = time.time()
    try:
        value = await aexec(cmd, event)
    except Exception:
        value = None
        exc = traceback.format_exc()
    tima = time.time() - tima
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    if value and gsource:
        try:
            exc = inspect.getsource(value)
        except Exception:
            exc = traceback.format_exc()
    evaluation = exc or stderr or stdout or _parse_eval(value) or "Success"
    if silent:
        if exc:
            msg = f"• <b>EVAL ERROR\n\n• CHAT:</b> <code>{get_display_name(event.chat)}</code> [<code>{event.chat_id}</code>]"
            msg += f"\n\n∆ <b>CODE:</b>\n<code>{cmd}</code>\n\n∆ <b>ERROR:</b>\n<code>{exc}</code>"
            # log_chat = udB.get_key("LOG_CHANNEL")
            if len(msg) > 4000:
                with BytesIO(msg.encode()) as out_file:
                    out_file.name = "Eval-Error.txt"
                return await event.client.send_message(
                    event.chat, f"`{cmd}`", file=out_file
                )
            await event.client.send_message(event.chat, msg, parse_mode="html")
        return
    tmt = tima * 1000
    timef = time_formatter(tmt)
    timeform = timef if not timef == "0s" else f"{tmt:.3f}ms"
    final_output = "**EVAL** (__in {}__)\n **OUTPUT**: \n```{}``` \n".format(
        timeform,
#         cmd, \n```{}``` \n
        evaluation,
    )
    if len(final_output) > 4096:
        final_output = evaluation
        with BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.txt"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                # thumb=ULTConfig.thumb,
                allow_cache=False,
#                 caption=f"```{cmd}```" if len(cmd) < 998 else None,
                reply_to=reply_to_id,
            )
        return await xx.delete()
    await xx.edit(final_output)


def _stringify(text=None, *args, **kwargs):
    if text:
        u._ = text
        text = _parse_eval(text)
    return print(text, *args, **kwargs)


async def aexec(code, event):
    exec(
        (
            "async def __aexec(e, client): "
            + "\n print = p = _stringify"
            + "\n message = event = e"
            + "\n u.r = reply = await event.get_reply_message()"
            + "\n chat = event.chat_id"
            + "\n u.lr = locals()"
        )
        + "".join(f"\n {l}" for l in code.split("\n"))
    )

    return await locals()["__aexec"](event, event.client)

# ------------------Some Small Funcs----------------


def time_formatter(milliseconds):
    minutes, seconds = divmod(int(milliseconds / 1000), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    tmp = (
        ((str(weeks) + "w:") if weeks else "")
        + ((str(days) + "d:") if days else "")
        + ((str(hours) + "h:") if hours else "")
        + ((str(minutes) + "m:") if minutes else "")
        + ((str(seconds) + "s") if seconds else "")
    )
    if not tmp:
        return "0s"

    if tmp.endswith(":"):
        return tmp[:-1]
    return tmp


def humanbytes(size):
    if not size:
        return "0 B"
    for unit in ["", "K", "M", "G", "T"]:
        if size < 1024:
            break
        size /= 1024
    if isinstance(size, int):
        size = f"{size}{unit}B"
    elif isinstance(size, float):
        size = f"{size:.2f}{unit}B"
    return size


def numerize(number):
    if not number:
        return None
    for unit in ["", "K", "M", "B", "T"]:
        if number < 1000:
            break
        number /= 1000
    if isinstance(number, int):
        number = f"{number}{unit}"
    elif isinstance(number, float):
        number = f"{number:.2f}{unit}"
    return number


No_Flood = {}

async def progress(current, total, event, start, type_of_ps, file_name=None):
    now = time.time()
    if No_Flood.get(event.chat_id):
        if No_Flood[event.chat_id].get(event.id):
            if (now - No_Flood[event.chat_id][event.id]) < 1.1:
                return
        else:
            No_Flood[event.chat_id].update({event.id: now})
    else:
        No_Flood.update({event.chat_id: {event.id: now}})
    diff = time.time() - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        time_to_completion = round((total - current) / speed) * 1000
        progress_str = "`[{0}{1}] {2}%`\n\n".format(
            "".join("●" for i in range(math.floor(percentage / 5))),
            "".join("" for i in range(20 - math.floor(percentage / 5))),
            round(percentage, 2),
        )

        tmp = (
            progress_str
            + "`{0} of {1}`\n\n`✦ Speed: {2}/s`\n\n`✦ ETA: {3}`\n\n".format(
                humanbytes(current),
                humanbytes(total),
                humanbytes(speed),
                time_formatter(time_to_completion),
            )
        )
        if file_name:
            await event.edit(
                "`✦ {}`\n\n`File Name: {}`\n\n{}".format(type_of_ps, file_name, tmp)
            )
        else:
            await event.edit("`✦ {}`\n\n{}".format(type_of_ps, tmp))
            
async def async_searcher(
    url: str,
    post: bool = None,
    headers: dict = None,
    params: dict = None,
    json: dict = None,
    data: dict = None,
    ssl=None,
    re_json: bool = False,
    re_content: bool = False,
    real: bool = False,
    *args,
    **kwargs,
):
    try:
        import aiohttp
    except ImportError:
        raise DependencyMissingError(
            "'aiohttp' is not installed!\nthis function requires aiohttp to be installed."
        )
    async with aiohttp.ClientSession(headers=headers) as client:
        if post:
            data = await client.post(
                url, json=json, data=data, ssl=ssl, *args, **kwargs
            )
        else:
            data = await client.get(url, params=params, ssl=ssl, *args, **kwargs)
        if re_json:
            return await data.json()
        if re_content:
            return await data.read()
        if real:
            return data
        return await data.text()
