import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Shikimori.events import register
from Shikimori import telethn as tbot


PHOTO = "https://telegra.ph/file/23db949e5f1aaf1b44889.jpg"

@register(pattern=("/gamma"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}).** \n\n"
  TEXT += "❍ **TEAM GAMMA ** \n\n"
  TEXT += f"❍ **CAPTAIN : [VIKING VECTOR](https://t.me/The_Viking_khilji)** \n\n"
  TEXT += f"❍ **VICE CAP : [TARUN](https://t.me/NagandlaTarunChowdary)** \n\n"
  TEXT += f"❍ **IF U WANT TO JOIN TEAM GAMMA USE THE BUTTON BELOW\n\n"
  BUTTON = [
      [
          Button.url("『CAPTAIN』", "https://t.me/The_Viking_khilji"),
          Button.url("『VICE CAP』", "https://t.me/NagandlaTarunChowdary")
      ],
      [
          Button.url("『TEAM GAMMA』", "https://t.me/GammaFamily")
      ],
      [
          Button.url("『 HOW TO JOIN GAMMA 』", "https://t.me/GammaRegistration_bot")
      ]
    ]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
