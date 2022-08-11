import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


PHOTO = "https://telegra.ph/file/38513d13b5f772f2a36bd.jpg"

@register(pattern=("/fpfpfp"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Officer Jenny.** \n\n"
  TEXT += "❍ **I'm Working Properly** \n\n"
  TEXT += f"❍ **Hexa owner : [FATHER PRIEST](tg://user?id=202146102)** \n\n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("Father priest", "tg://user?id=202146102"), Button.url("Hexa", "https://t.me/hexamonbot")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
