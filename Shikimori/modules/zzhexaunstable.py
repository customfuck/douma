import html
import random
import time

import Shikimori.strings.ExtraGifs_strings as ExtraGifs_strings
from Shikimori import dispatcher
from Shikimori.modules.disable import DisableAbleCommandHandler
from Shikimori.modules.helper_funcs.chat_status import is_user_admin
from Shikimori.modules.helper_funcs.extraction import extract_user
from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext

def nexttour(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "COMING SOON",
    )

def prizepool(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Prize pool for dice tour\n\n1st- 15k + X MOD FOR A MONTH\n2nd- 10k\n3rd- 5k",
    )
    
NEXTTOUR_HANDLER = DisableAbleCommandHandler("nexttour", nexttour, run_async=True)
PRIZEPOOL_HANDLER = DisableAbleCommandHandler("prizepool", prizepool, run_async=True)

dispatcher.add_handler(NEXTTOUR_HANDLER)
dispatcher.add_handler(PRIZEPOOL_HANDLER)
