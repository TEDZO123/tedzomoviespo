import requests
from io import BytesIO
from pyrogram import filters as Bot
from pyrogram import idle
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

JSON_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('⚙ Join Updates Channel ⚙', url='https://telegram.me/FayasNoushad')
        ]
    ]
)
@Bot.on_message(filters.private & (filters.text | filters.media | filters.service) & ~filters.reply)
async def private(bot, update):
    await reply_file(bot, update)


@Bot.on_message((filters.group | filters.private) & filters.command(["json"]))
async def group(bot, update):
    await reply_file(bot, update.reply_to_message)


async def reply_file(bot, update):
    with BytesIO(str.encode(str(update))) as file:
        file.name = "json.txt"
        await update.reply_document(
            document=file,
            quote=True,
            reply_markup=JSON_BUTTON
        )
        try:
            os.remove(file)
        except:
            pass


@Bot.on_inline_query()
async def inline(bot, update):
    await update.answer(
        results=[],
        switch_pm_text="Your json was sent to pm",
        switch_pm_parameter="start"
    )
    with BytesIO(str.encode(str(update))) as file:
        file.name = "json.txt"
        await bot.send_document(
            chat_id=update.from_user.id,
            document=file,
            reply_markup=JSON_BUTTON
        )
        try:
            os.remove(file)
        except:
            pass
