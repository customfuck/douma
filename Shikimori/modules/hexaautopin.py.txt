import asyncio

from telethon import events
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator

@client.on(events.NewMessage)
async def my_event_handler(event):
  if event.chat_id == -1001206009741:
    if event.sender_id == 572621020:
      if 'has challenged' in event.raw_text:
        pinable = await client.pin_message(event.chat_id, event.message_id, notify=True)
