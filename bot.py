import asyncio
from os import environ
from pyrogram import *
from pyrogram.types import *

API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
# SESSION = environ.get("SESSION")
TIME = int(environ.get("TIME"))

GROUPS = []
for grp in environ.get("GROUPS").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("ADMINS").split():
    ADMINS.append(int(usr))

START_MSG = "<b>Hᴇʟʟᴏ {}\n\nI ᴏɴʟʏ sᴜᴘᴘᴏʀᴛ ᴛʜᴇ</b> <a href='http://t.me/Cinimalokham'><b>Cɪɴɪᴍᴀʟᴏᴋʜᴀᴍ</b></a> <b>ɢʀᴏᴜᴘ\n\nI ᴅᴏ ɢʀᴏᴜᴘ ᴀᴜᴛᴏᴍᴀᴛɪᴄ ᴄʟᴇᴀɴɪɴɢ ᴇᴠᴇʀʏ 30 ᴍɪɴᴜᴛᴇs</b>"
reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("button name", url="http://t.me/@Cinimalokham")]])

# user = Client(session_name=SESSION,
#               api_id=API_ID,
#               api_hash=API_HASH,
#               workers=300
#               )


app = Client(session_name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )

@app.on_message(filters.command('pin') & filters.private)
async def pin(bot, message):
    
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@app.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await app.delete_messages(message.chat.id, message.message_id)
    except Exception as e:
       print(e)
       
app.run()
print("Bot Started..")
