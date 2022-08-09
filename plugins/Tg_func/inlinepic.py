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
    
    results = requests.get(
        API + requests.utils.requote_uri(update.query)
    ).json()["result"][:50]
    
    answers = []
    for result in results:
        answers.append(
            InlineQueryResultPhoto(
                title=update.query.capitalize(),
                description=result,
                caption="Made by @FayasNoushad",
                photo_url=result
            )
        )
    
    await update.answer(answers)
