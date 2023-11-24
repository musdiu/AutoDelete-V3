import asyncio
from os import environ
from pyrogram import *
from pyrogram.types import *
import time

API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
# SESSION = environ.get("SESSION")
TIME = int(environ.get("TIME"))
#ADMIN = int(environ.get("ADMIN"))
GROUPS = [int(grp) for grp in environ.get("GROUPS").split()]
ADMINS = [int(usr) for usr in environ.get("ADMINS").split()]

START_MSG = "<b>Hᴇʟʟᴏ {}\n\nI ᴏɴʟʏ sᴜᴘᴘᴏʀᴛ ᴛʜᴇ</b> <a href='http://t.me/Cinimalokham'><b>Cɪɴɪᴍᴀʟᴏᴋʜᴀᴍ</b></a> <b>ɢʀᴏᴜᴘ\n\nI ᴅᴏ ɢʀᴏᴜᴘ ᴀᴜᴛᴏᴍᴀᴛɪᴄ ᴄʟᴇᴀɴɪɴɢ ᴇᴠᴇʀʏ 30 ᴍɪɴᴜᴛᴇs</b>"
#reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("button name", url="http://t.me/@Cinimalokham")]])

app = Client("auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)


@app.on_message(filters.command('start') & filters.private)
async def start(__, m: Message):
    await m.reply(START_MSG.format(m.from_user.mention))

@app.on_message(filters.chat(GROUPS))
async def delete(__, m: Message):
    try:
        if m.from_user.id in ADMINS:
            return
        else:
            await asyncio.sleep(TIME)
            await m.delete()
    except Exception as e:
        print(e)
       
app.run()
print("Bot Started..")
