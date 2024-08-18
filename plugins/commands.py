from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_MSG = """**Hi {}
  
I am a Media Editor bot ...

You can edit/relace the documents,videos,gifs,audios,photos etc… Of Your Channels easily By Using Me**

`For More Info On Usage Hit ➟` /help 

"""


HELP_MSG = """
Follow the steps...

First Send Me A Media That You Need To Edit/Replace The Other One

Send The Link Of The Media That Will Be Replaced/Edited

NB: Note both you & the bot must be an admin in the targert channel 

"""


@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    # Use chat.id instead of message.message_id
    await message.reply_text(
        text=START_MSG.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="HELPER", url="t.me/DarkPhew")]]),
        # Choose either markdown or HTML formatting
        parse_mode="HTML"
    )

@Client.on_message(filters.command('help') & filters.private)
async def help(client, message):
    # Use chat.id instead of message.message_id
    await message.reply_text(
        text=HELP_MSG,
        disable_web_page_preview=True,
        # Choose either markdown or HTML formatting
        parse_mode="HTML"
    )
