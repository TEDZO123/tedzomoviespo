import os
import io
import requests
from requests import get
from pyrogram.types import Message
from bs4 import *
from pyrogram import filters, Client
from PIL import Image
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@Client.on_message(filters.command(["test123", "myre"]))
async def wall(client, message):
    quew = get_text(message)
    if not quew:
        await client.send_message(
            message.chat.id, "😶 **ᴩʟᴇᴀsᴇ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ sᴇᴀʀᴄʜ ғᴏʀ ʟᴏɢᴏ !**"
        )
        return
    m = await client.send_message(message.chat.id, "⚙️ **ᴄʀᴇᴀᴛɪɴɢ.. ʟᴏɢᴏ...**")
    try:
        text = get_text(message)
        LOGO_API = f"https://api.safone.tech/qrcode?text={text}"
        randc = LOGO_API
        MY_NAME = "@tedzo01"
        murl = (
            requests.get(
                f"https://api.safone.tech/qrcode?text={text}"
            )
            .history[1]
            .url
        )
        img = Image.open(io.BytesIO(requests.get(randc).content))
        fname = "TeDzO.png"
        img.save(fname, "png")
        caption = f"""
💘 ʟᴏɢᴏ ɢᴇɴᴇʀᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ 
✨ **ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ :`{MY_NAME}`
🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}
❄ **ᴅᴏᴡɴʟᴏᴀᴅ :** `{murl}`
"""
        await m.delete()
        await client.send_photo(
            message.chat.id,
            photo=murl,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("• ʟɪɴᴋ •", url=f"{murl}")],
                ]
            ),
        )
        if os.path.exists(fname):
            os.remove(fname)
    except Exception as e:
        await client.send_message(
            message.chat.id,
            f"sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ.\nᴩʟᴇᴀsᴇ ʀᴇᴩᴏʀᴛ ᴛʜɪs ᴀᴛ @tzobotz\n\n**ᴇʀʀᴏʀ :** {e}",
        )
