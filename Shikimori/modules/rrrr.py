from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from time import sleep
from telethon.tl.types import MessageEntityCode
from telethon import TelegramClient, events, Button
import telethon.sync #lol copied from docs
import asyncio
from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
import logging #lol copied from docs
import asyncio
from telethon import events
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
import io
from datetime import datetime
import configparser
from pprint import pprint
import argparse
import sqlite3
import contextlib
import telethon
import telethon.sync
from PIL import 



@client.on(events.NewMessage(pattern=r'(?i).*pin'))
async def my_event_handler(event):
  if event.is_reply:
    message = await event.get_reply_message()
    tag = message.sender_id
    if tag == 572621020:
      mes = message.text
      if 'challenged' or 'turn' or 'Battle' or 'used' or 'switched' or 'Current' in mes:
        pinable = await client.pin_message(event.chat_id, message, notify=True)
        await asyncio.sleep(600)
        await client.unpin_message(event.chat_id, message)
