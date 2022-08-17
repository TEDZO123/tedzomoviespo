import requests
from bot import bot
from pyrogram import filters, idle
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from buttons import MENU_BUTTON

# await m.delete()
@bot.on_message(filters.regex("@tedzo01"))
async def bak(bot, msg):
    await msg.reply(text="<b>Enter Your FeedBack OR Request, I Will Give It To My Boss</b>")
        await msg.message.edit("○○○○○")
        await msg.message.edit("●○○○○")
        await msg.message.edit("●●○○○")
        await msg.message.edit("●●●○○")
        await msg.message.edit("●●●●○")
        await msg.message.edit("●●●●●")
        await msg.message.edit(
            text="Hᴇʀᴇ Is Yᴏᴜ'ʀᴇ Mᴇɴᴜ",
            reply_markup=InlineKeyboardMarkup(MENU_BUTTON)
        )
