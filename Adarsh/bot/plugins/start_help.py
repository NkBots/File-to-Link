#Aadhi000 
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

                      

buttonz=ReplyKeyboardMarkup(
            [
                ["start","help"],
                ["about","ping"],
                ["status"]        
            ],
            resize_keyboard=True
        )

START_TEXT = """
Hey {} 👋\n
<code>I am Telegram File To Link Bot</code>\n
<code>Use Help Command to Know how to Use me</code>\n
<code>By @NkBots</code>\n
**Maintained By @Tellybotzz**"""

HELP_TEXT = """
✮ Send Me Any File or Media\n
✮ I Will Provide You Instant Direct Download link as Well as Stream Link\n
✮ Add me in Your Channel as Admin To Get Direct Download link button and online Stream Link Button\n
"""


ABOUT_TEXT = """
🤖 My Name : Telly File Stream Bot\n
🚦 Version : <a href='https://telegram.me/Nkbots'>3.0</a>\n
💫 Source Code : <a href='https://t.me/tellybots_digital'>Click Here</a>\n
🗃️ Library : <a href='https://pyrogram.org'>Click Here</a>\n
👲 Developer : <a href='https://telegram.me/Nkbots'>NkBots</a>\n
📦 Last Updated : <a href='https://telegram.me/Nkbots'>[ 13-mar-23 ] 09:00 AM</a>"""

TEXT = """Just Send Me Any Telegram Media To Get Started\n\nOr Use Below Buttons to Interact With Me"""


INFO_TEXT = """
 💫 Telegram Information

 🤹 First Name : <b>{}</b>

 🚴‍♂️ Second Name : <b>{}</b>

 🧑🏻‍🎓 Username : <b>@{}</b>

 🆔 Telegram Id : <code>{}</code>

 📇 Profile Link : <b>{}</b>

 📡 Dc : <b>{}</b>

 📑 Language : <b>{}</b>

 👲 Status : <b>{}</b>
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🌷 Help', callback_data='help'),
        InlineKeyboardButton('💠 About', callback_data='about')
        ],[
        InlineKeyboardButton('📛 Close', callback_data='close')
        ]]
)
             

HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('💠 About', callback_data='about')
        ],[
        InlineKeyboardButton('📛 Close', callback_data='close')
        ]]
)
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('🌷 Help', callback_data='help')
        ],[
        InlineKeyboardButton('📛 Close', callback_data='close')
        ]]
)
 





        

@StreamBot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()
 
 #Recoded By Tellybots

@StreamBot.on_message((filters.command("about")) & filters.private)
async def about(bot, update):

    await update.reply_text(
        text=ABOUT_TEXT,
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    ) 
@StreamBot.on_message((filters.command("help")) & filters.private)
async def help(bot, update):

    await update.reply_text(
        text=HELP_TEXT,
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
    )

@StreamBot.on_message(filters.private & filters.command("info"))
async def info_handler(bot, update):


    if update.from_user.last_name:
        last_name = update.from_user.last_name
    else:
        last_name = "None"

  
    await update.reply_text(  
        text=INFO_TEXT.format(update.from_user.first_name, last_name, update.from_user.username, update.from_user.id, update.from_user.mention, update.from_user.dc_id, update.from_user.language_code, update.from_user.status),             
        disable_web_page_preview=True
    )
