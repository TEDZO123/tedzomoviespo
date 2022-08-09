import os
import requests
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InlineQueryResultPhoto
)

API = "https://apibu.herokuapp.com/api/y-images?query="

@Client.on_inline_query()
async def search(bot, update):
    
    
    answers = []
    for result in results:
    if update.query == "pic":
        answers.append(
            InlineQueryResultPhoto(
                title=update.query.capitalize(),
                description=result,
                caption="Made by @tedzosir",
                photo_url=requests.get(
        API + requests.utils.requote_uri(update.query)
    ).json()["result"][:50]
            )
        )
    
    await update.answer(answers)
