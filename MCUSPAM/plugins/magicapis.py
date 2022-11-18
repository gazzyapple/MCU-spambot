from telethon import events
from telethon.tl.custom import Button
from telethon import TelegramClient
from decouple import config
from MCUSPAM import BOT,first_bot
import aiohttp
import re, os

@first_bot.on(events.NewMessage(pattern="^/search"))
async def search(event):
    msg = await event.respond("Searching...")
    async with aiohttp.ClientSession() as session:
        if event.text.split()[1:]:
            query = event.text.split()[1:]
            start = 1
            async with session.get(f"https://content-customsearch.googleapis.com/customsearch/v1?cx=ec8db9e1f9e41e65e&q={query}&key=AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM&start={start}", headers={"x-referer": "https://explorer.apis.google.com"}) as r:
                response = await r.json()
                result = ""

                if not response.get("items"):
                    return await msg.edit("No results found!")
                for item in response["items"]:
                    title = item["title"]
                    link = item["link"]
                    if "/s" in item["link"]:
                        link = item["link"].replace("/s", "")
                    elif re.search(r'\/\d', item["link"]):
                        link = re.sub(r'\/\d', "", item["link"])
                    if "?" in link:
                        link = link.split("?")[0]
                    if link in result:
                        # remove duplicates
                        continue
                    result += f"{title}\n{link}\n\n"
                prev_and_next_btns = [Button.inline("▶️Next▶️", data=f"next {start+10} {event.text.split()[1]}")]
                await msg.edit(result, link_preview=False, buttons=prev_and_next_btns)
                await session.close()
        else:
            await event.reply("Provide something to search")

@first_bot.on(events.CallbackQuery(data=re.compile(r"prev (.*) (.*)")))
async def prev(event):
    start = int(event.data.split()[1])
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://content-customsearch.googleapis.com/customsearch/v1?cx=ec8db9e1f9e41e65e&q={(event.data.split()[2]).decode('utf-8')}&key=AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM&start={start}", headers={"x-referer": "https://explorer.apis.google.com"}) as r:
            response = await r.json()
            if response.get("error"):
                return await event.answer("No more results!")
            result = ""            
            for item in response["items"]:
                title = item["title"]
                link = item["link"]
                if "/s" in item["link"]:
                    link = item["link"].replace("/s", "")
                elif re.search(r'\/\d', item["link"]):
                    link = re.sub(r'\/\d', "", item["link"])
                if "?" in link:
                    link = link.split("?")[0]
                if link in result:
                    # remove duplicates
                    continue
                result += f"{title}\n{link}\n\n"
            prev_and_next_btns = [Button.inline("◀️Prev◀️", data=f"prev {start-10} {event.data.split()[2].decode('utf-8')}"), Button.inline("▶️Next▶️", data=f"next {start+10} {event.data.split()[2].decode('utf-8')}")]
            await event.edit(result, link_preview=False, buttons=prev_and_next_btns)
            await session.close()

@first_bot.on(events.CallbackQuery(data=re.compile(r"next (.*) (.*)")))
async def next(event):
    start = int(event.data.split()[1])
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://content-customsearch.googleapis.com/customsearch/v1?cx=ec8db9e1f9e41e65e&q={(event.data.split()[2]).decode('utf-8')}&key=AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM&start={start}", headers={"x-referer": "https://explorer.apis.google.com"}) as r:
            response = await r.json()
            print(response["searchInformation"]["totalResults"])
            if response["searchInformation"]["totalResults"] == "0" or response.get("error"):
                return await event.answer("No more results!")
            result = ""
            for item in response["items"]:
                title = item["title"]
                link = item["link"]
                if "/s" in item["link"]:
                    link = item["link"].replace("/s", "")
                elif re.search(r'\/\d', item["link"]):
                    link = re.sub(r'\/\d', "", item["link"])
                if "?" in link:
                    link = link.split("?")[0]
                if link in result:
                    # remove duplicates
                    continue
                result += f"{title}\n{link}\n\n"
            prev_and_next_btns = [Button.inline("◀️Prev◀️", data=f"prev {start-10} {(event.data.split()[2]).decode('utf-8')}"), Button.inline("▶️Next▶️", data=f"next {start+10} {(event.data.split()[2]).decode('utf-8')}")]
            await event.edit(result, link_preview=False, buttons=prev_and_next_btns)
            await session.close()

# client.run_until_disconnected()
