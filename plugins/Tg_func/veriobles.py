import requests
from bot import bot
from pyrogram import filters, idle
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from info import GITHUB_TEXT, SITHIJATD_BUTTONS

@bot.on_message(filters.regex("@tedzo01"))
async def bak(bot, msg):
    await msg.reply(text="<b>Enter Your FeedBack OR Request, I Will Give It To My Boss</b>")
        await asyncio.sleep(0.2)
        await msg.message.edit("|( ͡❛ ͜ʖ ͡❛)")
        await asyncio.sleep(0.2)
        await asyncio.sleep(0.2)
        await msg.message.edit("||っ ͡❛ ͜ʖ ͡❛|っ🧠")
        await asyncio.sleep(0.2)
        await msg.message.edit("| |っ ͡❛ ͜ʖ ͡❛|っ🧠")
        await asyncio.sleep(0.2)
        await msg.message.edit("|  |っ ͡❛ ͜ʖ ͡❛|っ🧠")
        await asyncio.sleep(0.2)
        await msg.message.edit("|   |っ ͡❛ ͜ʖ ͡❛|っ🧠")
        await asyncio.sleep(0.2)
        await msg.message.edit("|    |っ ͡❛ ͜ʖ ͡❛|っ🧠")
        await asyncio.sleep(0.2)
        await msg.message.edit("|     |っ ͡❛ ͜ʖ ͡❛|っ🧠")
        await asyncio.sleep(0.2)
        await msg.message.edit("|      |っ ͡❛ ͜ʖ ͡❛|っ🧠")
        await asyncio.sleep(0.2)
        await msg.message.edit("|       |っ ͡❛ ͜ʖ ͡❛|っ🧠") 
        await msg.message.edit("|        |っ ͡❛ ͜ʖ ͡❛|っ🧠\n                  🗑")
        await asyncio.sleep(0.2)
        await msg.message.edit("|        |っ ͡❛ ͜ʖ ͡❛|っ  \n                  🗑")
        await asyncio.sleep(0.2)
        await msg.message.edit("|        |っ ͡❛ ͜ʖ ͡❛|っ  \n                  💩")
        await asyncio.sleep(0.2)
       await message.reply_text(
        text="Hᴇʀᴇ Is Yᴏᴜ'ʀᴇ Mᴇɴᴜ",
        reply_markup=InlineKeyboardMarkup(MENU_BUTTON)
        disable_web_page_preview=True
)
    # await m.delete()
@bot.on_message(filters.regex("REQUEST/FEEDBACK"))
async def bak(bot, msg):
    await msg.reply(text="<b>Enter Your FeedBack OR Request, I Will Give It To My Boss</b>")
        await asyncio.sleep(0.2)
        await msg.message.edit("○○○○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●○○○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●○○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●●○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●●●○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●●●●")
        await asyncio.sleep(0.2)
        await msg.message.edit(
            text="Hᴇʀᴇ Is Yᴏᴜ'ʀᴇ Mᴇɴᴜ",
            reply_markup=InlineKeyboardMarkup(MENU_BUTTON)
        )
