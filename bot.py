idport asyncio
from os import environ
from pyrogram import *
from pyrogram.types import *

API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
# SESSION = environ.get("SESSION")
TIME = int(environ.get("TIME"))
#ADMIN = int(environ.get("ADMIN"))
GROUPS = []
for grp in environ.get("GROUPS").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("ADMINS").split():
    ADMINS.append(int(usr))

START_MSG = "<b>Hai {},\nI'm a simple bot to delete group messages after a specific time</b>"

reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("button name", url="http://t.me/@Cinimalokham")]])

# user = Client(session_name=SESSION,
#               api_id=API_ID,
#               api_hash=API_HASH,
#               workers=300
#               )


app = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )

#@app.on_message(filters.command('pin') & filters.private)
#async def pin(bot, message):
   # if message.from_user.id == ADMIN: 
               #if message.reply_to_message:
                                   # chatid=int(message.text.replace("/pin"," "))
                                    #p=await bot.copy_message(chat_id=chatid, from_chat_id=ADMIN, message_id=message.reply_to_message.message_id)
                                   #₹ await p.pin()
                                    #await message.reply_text("<b>✅ Message Successfully Send to the Group And pinned</b>")
              # else:
                    #await message.reply_text("<b>Use this command as the reply of any Message to Send in Group</b>")                         
    #else:
         #await message.reply_text("<b>That's not for you bruh 😅</b>")
            
@app.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@app.on_message(filters.chat(GROUPS))
async def delete(__, m: Message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await app.delete_messages(m.chat.id,m.id)
    except Exception as e:
       print(e)
       
app.run()
print("Bot Started..")
