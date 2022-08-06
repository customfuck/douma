"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

Credits:-
    I don't know who originally wrote this code. If you originally wrote this code, please reach out to me. 

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import html
import json
import os
from typing import Optional

from Shikimori import (
    DEV_USERS,
    OWNER_ID,
    DRAGONS,
    SUPPORT_CHAT,
    DEMONS,
    TIGERS,
    WOLVES,
    dispatcher,
)
from Shikimori.modules.helper_funcs.chat_status import (
    dev_plus,
    sudo_plus,
    whitelist_plus,
)
from Shikimori.modules.helper_funcs.extraction import extract_user
from Shikimori.modules.log_channel import gloggable
from telegram import ParseMode, TelegramError, Update
from telegram.ext import CallbackContext, CommandHandler
from telegram.utils.helpers import mention_html

ELEVATED_USERS_FILE = os.path.join(os.getcwd(), "Shikimori/elevated_users.json")


def check_user_id(user_id: int, context: CallbackContext) -> Optional[str]:
    bot = context.bot
    if not user_id:
        reply = "That...is a chat! baka ka omae?"

    elif user_id == bot.id:
        reply = "This does not work that way."

    else:
        reply = None
    return reply


# This can serve as a deeplink example.
# disasters =
# """ Text here """

# do not async, not a handler
# def send_disasters(update):
#    update.effective_message.reply_text(
#        disasters, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

### Deep link example ends



@dev_plus
@gloggable
def addsudo(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DRAGONS:
        message.reply_text("𝚃𝚑𝚒𝚜 𝚖𝚎𝚖𝚋𝚎𝚛 𝚒𝚜 𝚊𝚕𝚛𝚎𝚊𝚍𝚢 𝚊 𝙷𝙰𝚂𝙷𝙸𝚁𝙰. ")
        return ""

    if user_id in DEMONS:
        rt += "𝙳𝙴𝙼𝙾𝙽 𝙺𝙸𝙽𝙶 𝚙𝚛𝚘𝚖𝚘𝚝𝚎𝚍 𝚊 𝙻𝙾𝚆𝙴𝚁𝙼𝙾𝙾𝙽 𝚝𝚘 𝙷𝙰𝚂𝙷𝙸𝚁𝙰."
        data["supports"].remove(user_id)
        DEMONS.remove(user_id)

    if user_id in WOLVES:
        rt += "𝙳𝙴𝙼𝙾𝙽 𝙺𝙸𝙽𝙶 𝚙𝚛𝚘𝚖𝚘𝚝𝚎𝚍 𝚊 𝙳𝙴𝙼𝙾𝙽 𝚝𝚘 𝙷𝙰𝚂𝙷𝙸𝚁𝙰."
        data["whitelists"].remove(user_id)
        WOLVES.remove(user_id)

    data["sudos"].append(user_id)
    DRAGONS.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt
        + "\n𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝚙𝚛𝚘𝚖𝚘𝚝𝚎𝚍 {} 𝚝𝚘 𝙷𝙰𝚂𝙷𝙸𝚁𝙰.".format(
            user_member.first_name
        )
    )

    log_message = (
        f"#Hashira\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
    )

    if chat.type != "private":
        log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

    return log_message



@sudo_plus
@gloggable
def addsupport(
    update: Update,
    context: CallbackContext,
) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DRAGONS:
        rt += "𝙳𝙴𝙼𝙾𝙽 𝙺𝙸𝙽𝙶 𝚍𝚎𝚖𝚘𝚝𝚎𝚍 𝚝𝚑𝚒𝚜 𝙷𝙰𝚂𝙷𝙸𝚁𝙰 𝚝𝚘 𝙻𝙾𝚆𝙴𝚁𝙼𝙾𝙾𝙽. "
        data["sudos"].remove(user_id)
        DRAGONS.remove(user_id)

    if user_id in DEMONS:
        message.reply_text("𝚃𝚑𝚒𝚜 𝚞𝚜𝚎𝚛 𝚒𝚜 𝚊𝚕𝚛𝚎𝚊𝚍𝚢 𝚊 𝙻𝙾𝚆𝙴𝚁𝙼𝙾𝙾𝙽.")
        return ""

    if user_id in WOLVES:
        rt += "𝙳𝙴𝙼𝙾𝙽 𝙺𝙸𝙽𝙶 𝚙𝚛𝚘𝚖𝚘𝚝𝚎𝚍 𝚊 𝙳𝙴𝙼𝙾𝙽 𝚝𝚘 𝙻𝙾𝚆𝙴𝚁𝙼𝙾𝙾𝙽."
        data["whitelists"].remove(user_id)
        WOLVES.remove(user_id)

    data["supports"].append(user_id)
    DEMONS.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt + f"\n{user_member.first_name} 𝚠𝚊𝚜 𝚊𝚍𝚍𝚎𝚍 𝚊𝚜 𝚊 𝙻𝙾𝚆𝙴𝚁𝙼𝙾𝙾𝙽!"
    )

    log_message = (
        f"#Lowermoon\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
    )

    if chat.type != "private":
        log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

    return log_message



@sudo_plus
@gloggable
def addwhitelist(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DRAGONS:
        rt += "𝚃𝚑𝚒𝚜 𝚖𝚎𝚖𝚋𝚎𝚛 𝚒𝚜 𝚊  𝙷𝙰𝚂𝙷𝙸𝚁𝙰, 𝙳𝚎𝚖𝚘𝚝𝚒𝚗𝚐 𝚝𝚘 𝙳𝙴𝙼𝙾𝙽."
        data["sudos"].remove(user_id)
        DRAGONS.remove(user_id)

    if user_id in DEMONS:
        rt += "𝚃𝚑𝚒𝚜 𝚖𝚎𝚖𝚋𝚎𝚛 𝚒𝚜 𝚊  𝙻𝙾𝚆𝙴𝚁𝙼𝙾𝙾𝙽, 𝙳𝚎𝚖𝚘𝚝𝚒𝚗𝚐 𝚝𝚘 𝙳𝙴𝙼𝙾𝙽."
        data["supports"].remove(user_id)
        DEMONS.remove(user_id)

    if user_id in WOLVES:
        message.reply_text("𝚃𝚑𝚒𝚜 𝚞𝚜𝚎𝚛 𝚒𝚜 𝚊𝚕𝚛𝚎𝚊𝚍𝚢 𝚊 𝙳𝙴𝙼𝙾𝙽.")
        return ""

    data["whitelists"].append(user_id)
    WOLVES.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt + f"\n𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝚙𝚛𝚘𝚖𝚘𝚝𝚎𝚍 {user_member.first_name} 𝚝𝚘 𝚊 𝙳𝙴𝙼𝙾𝙽!"
    )

    log_message = (
        f"#Demon\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))} \n"
        f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
    )

    if chat.type != "private":
        log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

    return log_message



@sudo_plus
@gloggable
def addtiger(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DRAGONS:
        rt += "𝚃𝚑𝚒𝚜 𝚖𝚎𝚖𝚋𝚎𝚛 𝚒𝚜 𝚊  𝙷𝙰𝚂𝙷𝙸𝚁𝙰, 𝙳𝚎𝚖𝚘𝚝𝚒𝚗𝚐 𝚝𝚘 𝙳𝙴𝙼𝙾𝙽 𝚂𝙻𝙰𝚈𝙴𝚁."
        data["sudos"].remove(user_id)
        DRAGONS.remove(user_id)

    if user_id in DEMONS:
        rt += "𝚃𝚑𝚒𝚜 𝚖𝚎𝚖𝚋𝚎𝚛 𝚒𝚜 𝚊  𝙻𝙾𝚆𝙴𝚁𝙼𝙾𝙾𝙽, 𝙳𝚎𝚖𝚘𝚝𝚒𝚗𝚐 𝚝𝚘 𝙳𝙴𝙼𝙾𝙽 𝚂𝙻𝙰𝚈𝙴𝚁."
        data["supports"].remove(user_id)
        DEMONS.remove(user_id)

    if user_id in WOLVES:
        rt += "𝚃𝚑𝚒𝚜 𝚖𝚎𝚖𝚋𝚎𝚛 𝚒𝚜 𝚊 𝙳𝙴𝙼𝙾𝙽, 𝙿𝚛𝚘𝚖𝚘𝚝𝚒𝚗𝚐 𝚝𝚘 𝙳𝙴𝙼𝙾𝙽 𝚂𝙻𝙰𝚈𝙴𝚁."
        data["whitelists"].remove(user_id)
        WOLVES.remove(user_id)

    if user_id in TIGERS:
        message.reply_text("𝚃𝚑𝚒𝚜 𝚞𝚜𝚎𝚛 𝚒𝚜 𝚊𝚕𝚛𝚎𝚊𝚍𝚢 𝚊 𝙳𝙴𝙼𝙾𝙽 𝚂𝙻𝙰𝚈𝙴𝚁.")
        return ""

    data["tigers"].append(user_id)
    TIGERS.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt + f"\n𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝚙𝚛𝚘𝚖𝚘𝚝𝚎𝚍 {user_member.first_name} 𝚝𝚘 𝚊 𝙳𝙴𝙼𝙾𝙽 𝚂𝙻𝙰𝚈𝙴𝚁"
    )

    log_message = (
        f"#Demon slayer\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))} \n"
        f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
    )

    if chat.type != "private":
        log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

    return log_message



@dev_plus
@gloggable
def removesudo(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DRAGONS:
        message.reply_text("𝙳𝙴𝙼𝙾𝙽 𝙺𝙸𝙽𝙶 𝚝𝚘 𝚝𝚘𝚘𝚔 𝚊𝚠𝚊𝚢 𝚝𝚑𝚒𝚜 𝚑𝚊𝚜𝚑𝚒𝚛𝚊'𝚜 𝚗𝚒𝚌𝚑𝚒𝚛𝚒𝚗 𝚜𝚠𝚘𝚛𝚍.")
        DRAGONS.remove(user_id)
        data["sudos"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"#Remove_hashira\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = "<b>{}:</b>\n".format(html.escape(chat.title)) + log_message

        return log_message

    else:
        message.reply_text("𝚃𝚑𝚒𝚜 𝚞𝚜𝚎𝚛 𝚒𝚜 𝚗𝚘𝚝 𝚊 𝙷𝙰𝚂𝙷𝙸𝚁𝙰!")
        return ""



@sudo_plus
@gloggable
def removesupport(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DEMONS:
        message.reply_text("𝙳𝙴𝙼𝙾𝙽 𝙺𝙸𝙽𝙶 𝚝𝚘 𝚝𝚘𝚘𝚔 𝚊𝚠𝚊𝚢 𝚝𝚑𝚒𝚜 𝚕𝚘𝚠𝚎𝚛𝚖𝚘𝚘𝚗'𝚜 𝚋𝚕𝚘𝚘𝚍 𝚍𝚎𝚖𝚘𝚗 𝚊𝚛𝚝")
        DEMONS.remove(user_id)
        data["supports"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"#remove_lowermoon\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

        return log_message

    else:
        message.reply_text("𝚃𝚑𝚒𝚜 𝚞𝚜𝚎𝚛 𝚒𝚜 𝚗𝚘𝚝 𝚊 𝙻𝙾𝚆𝙴𝚁𝙼𝙾𝙾𝙽!")
        return ""



@sudo_plus
@gloggable
def removewhitelist(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in WOLVES:
        message.reply_text("𝙳𝙴𝙼𝙾𝙽 𝙺𝙸𝙽𝙶 𝚝𝚘𝚘𝚔 𝚊𝚠𝚊𝚢 𝚝𝚑𝚒𝚜 𝚍𝚎𝚖𝚘𝚗'𝚜 𝚋𝚕𝚘𝚘𝚍 𝚍𝚎𝚖𝚘𝚗 𝚊𝚛𝚝𝚜.")
        WOLVES.remove(user_id)
        data["whitelists"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"#removedemon\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

        return log_message
    else:
        message.reply_text("𝚃𝚑𝚒𝚜 𝚞𝚜𝚎𝚛 𝚒𝚜 𝚗𝚘𝚝 𝚊 𝙳𝙴𝙼𝙾𝙽!")
        return ""



@sudo_plus
@gloggable
def removetiger(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in TIGERS:
        message.reply_text("𝙳𝙴𝙼𝙾𝙽 𝙺𝙸𝙽𝙶 𝚝𝚘𝚘𝚔 𝚊𝚠𝚊𝚢 𝚝𝚑𝚒𝚜 𝚍𝚎𝚖𝚘𝚗 𝚜𝚕𝚊𝚢𝚎𝚛'𝚜 𝚗𝚒𝚌𝚑𝚒𝚛𝚒𝚗 𝚜𝚠𝚘𝚛𝚍")
        TIGERS.remove(user_id)
        data["tigers"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"#remove_slayer\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

        return log_message
    else:
        message.reply_text("𝚃𝚑𝚒𝚜 𝚞𝚜𝚎𝚛 𝚒𝚜 𝚗𝚘𝚝 𝚊 𝙳𝙴𝙼𝙾𝙽 𝚂𝙻𝙰𝚈𝙴𝚁!")
        return ""



@whitelist_plus
def whitelistlist(update: Update, context: CallbackContext):
    reply = "<b>𝙺𝚗𝚘𝚠𝚗 𝙳𝙴𝙼𝙾𝙽:</b>\n"
    m = update.effective_message.reply_text(
        "<code>𝙶𝚊𝚝𝚑𝚎𝚛𝚒𝚗𝚐 𝚒𝚗𝚝𝚎𝚕 𝚏𝚛𝚘𝚖 VOID..</code>", parse_mode=ParseMode.HTML
    )
    bot = context.bot
    for each_user in WOLVES:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)

            reply += f"• {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)



@whitelist_plus
def tigerlist(update: Update, context: CallbackContext):
    reply = "<b>𝙺𝚗𝚘𝚠𝚗 𝙳𝙴𝙼𝙾𝙽 𝚂𝙻𝙰𝚈𝙴𝚁:</b>\n"
    m = update.effective_message.reply_text(
        "<code>𝙶𝚊𝚝𝚑𝚎𝚛𝚒𝚗𝚐 𝚒𝚗𝚝𝚎𝚕 𝚏𝚛𝚘𝚖 VOID..</code>", parse_mode=ParseMode.HTML
    )
    bot = context.bot
    for each_user in TIGERS:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"• {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)



@whitelist_plus
def supportlist(update: Update, context: CallbackContext):
    bot = context.bot
    m = update.effective_message.reply_text(
        "<code>𝙶𝚊𝚝𝚑𝚎𝚛𝚒𝚗𝚐 𝚒𝚗𝚝𝚎𝚕 𝚏𝚛𝚘𝚖 VOID..</code>", parse_mode=ParseMode.HTML
    )
    reply = "<b>𝙺𝚗𝚘𝚠𝚗 𝙻𝙾𝚆𝙴𝚁𝙼𝙾𝙾𝙽:</b>\n"
    for each_user in DEMONS:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"• {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)



@whitelist_plus
def sudolist(update: Update, context: CallbackContext):
    bot = context.bot
    m = update.effective_message.reply_text(
        "<code>𝙶𝚊𝚝𝚑𝚎𝚛𝚒𝚗𝚐 𝚒𝚗𝚝𝚎𝚕 𝚏𝚛𝚘𝚖 VOID..</code>", parse_mode=ParseMode.HTML
    )
    true_sudo = list(set(DRAGONS) - set(DEV_USERS))
    reply = "<b>𝙺𝚗𝚘𝚠𝚗 𝙷𝙰𝚂𝙷𝙸𝚁𝙰:</b>\n"
    for each_user in true_sudo:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"• {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)



@whitelist_plus
def devlist(update: Update, context: CallbackContext):
    bot = context.bot
    m = update.effective_message.reply_text(
        "<code>𝙶𝚊𝚝𝚑𝚎𝚛𝚒𝚗𝚐 𝚒𝚗𝚝𝚎𝚕 𝚏𝚛𝚘𝚖 VOID..</code>", parse_mode=ParseMode.HTML
    )
    true_dev = list(set(DEV_USERS) - {OWNER_ID})
    reply = "<b>𝙺𝚗𝚘𝚠𝚗 𝚄𝙿𝙿𝙴𝚁𝙼𝙾𝙾𝙽:</b>\n"
    for each_user in true_dev:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"• {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)


__help__ = f"""
*⚠️ Notice:*
Commands listed here only work for users with special access are mainly used for troubleshooting, debugging purposes.
Group admins/group owners do not need these commands. 

 ╔ *List all special users:*
 ╠ `/hashiras`*:* 𝙻𝚒𝚜𝚝𝚜 𝚊𝚕𝚕 𝙷𝙰𝚂𝙷𝙸𝚁𝙰 
 ╠ `/lowermoons`*:* 𝙻𝚒𝚜𝚝𝚜 𝚊𝚕𝚕 𝙻𝙾𝚆𝙴𝚁𝙼𝙾𝙾𝙽
 ╠ `/demonslayers`*:* 𝙻𝚒𝚜𝚝𝚜 𝚊𝚕𝚕 𝙳𝙴𝙼𝙾𝙽 𝚂𝙻𝙰𝚈𝙴𝚁𝚂
 ╠ `/demons`*:* 𝙻𝚒𝚜𝚝𝚜 𝚊𝚕𝚕 𝙳𝙴𝙼𝙾𝙽
 ╠ `/uppermoons`*:* 𝙻𝚒𝚜𝚝𝚜 𝚊𝚕𝚕 𝙰𝚁𝙲𝙷𝙾𝙽
 ╠ `/addhashira`*:* 𝙰𝚍𝚍 𝚊 𝚞𝚜𝚎𝚛 𝚝𝚘 HASHIRA
 ╠ `/addlowermoon`*:* 𝙰𝚍𝚍 𝚊 𝚞𝚜𝚎𝚛 𝚝𝚘 𝙻𝙾𝚆𝙴𝚁𝙼𝙾𝙾𝙽
 ╠ `/adddemonslayer`*:* 𝙰𝚍𝚍 𝚊 𝚞𝚜𝚎𝚛 𝚝𝚘 𝙳𝙴𝙼𝙾𝙽 𝚂𝙻𝙰𝚈𝙴𝚁𝚂
 ╠ `/adddemons`*:* 𝙰𝚍𝚍 𝚊 𝚞𝚜𝚎𝚛 𝚝𝚘 𝙳𝙴𝙼𝙾𝙽
 ╚ `Add dev doesnt exist, devs should know how to add themselves`
 
*Ping:*
 ❍ `/ping`*:* gets ping time of bot to telegram server
 ❍ `/pingall`*:* gets all listed ping times

*Broadcast: (Bot owner only)*
*Note:* This supports basic markdown
 ❍ `/broadcastall`*:* Broadcasts everywhere
 ❍ `/broadcastusers`*:* Broadcasts too all users
 ❍ `/broadcastgroups`*:* Broadcasts too all groups

*Groups Info:*
 ❍ `/groups`*:* List the groups with Name, ID, members count as a txt
 ❍ `/leave` <ID>*:* Leave the group, ID must have hyphen
 ❍ `/stats`*:* Shows overall bot stats
 ❍ `/getchats`*:* Gets a list of group names the user has been seen in. Bot owner only
 ❍ `/ginfo` username/link/ID*:* Pulls info panel for entire group

*Access control:* 
 ❍ `/ignore`*:* Blacklists a user from using the bot entirely
 ❍ `/lockdown `<off/on>*:* Toggles bot adding to groups
 ❍ `/notice`*:* Removes user from blacklist
 ❍ `/ignoredlist`*:* Lists ignored users

*Speedtest:*
 ❍ `/speedtest`*:* Runs a speedtest and gives you 2 options to choose from, text or image output

*Module loading:*
 ❍ `/listmodules`*:* Lists names of all modules
 ❍ `/load modulename`*:* Loads the said module to memory without restarting.
 ❍ `/unload modulename`*:* Loads the said module frommemory without restarting memory without restarting the bot 

*Remote commands:*
 ❍ `/rban`*:* user group*:* Remote ban
 ❍ `/runban`*:* user group*:* Remote un-ban
 ❍ `/rpunch`*:* user group*:* Remote punch
 ❍ `/rmute`*:* user group*:* Remote mute
 ❍ `/runmute`*:* user group*:* Remote un-mute

*Windows self hosted only:*
 ❍ `/reboot`*:* Restarts the bots service
 ❍ `/gitpull`*:* Pulls the repo and then restarts the bots service

*Chatbot:* 
 ❍ `/listaichats`*:* Lists the chats the chatmode is enabled in
 
*Debugging and Shell:* 
 ❍ `/debug` <on/off>*:* Logs commands to updates.txt
 ❍ `/logs`*:* Run this in support group to get logs in pm
 ❍ `/eval`*:* Self explanatory
 ❍ `/sh`*:* Runs shell command
 ❍ `/shell`*:* Runs shell command
 ❍ `/clearlocals`*:* As the name goes
 ❍ `/dbcleanup`*:* Removes deleted accs and groups from db
 ❍ `/py`*:* Runs python code
 
*Global Bans:*
 ❍ `/gban` <id> <reason>*:* Gbans the user, works by reply too
 ❍ `/ungban`*:* Ungbans the user, same usage as gban
 ❍ `/gbanlist`*:* Outputs a list of gbanned users

*Global Blue Text*
 ❍ `/gignoreblue`*:* <word>*:* Globally ignorea bluetext cleaning of saved word across lunaBot.
 ❍ `/ungignoreblue`*:* <word>*:* Remove said command from global cleaning list

*luna Core*
*Owner only*
 ❍ `/send`*:* <module name>*:* Send module
 ❍ `/install`*:* <reply to a .py>*:* Install module 

*Heroku Settings*
*Owner only*
 ❍ `/usage`*:* Check your heroku dyno hours remaining.
 ❍ `/see var` <var>*:* Get your existing varibles, use it only on your private group!
 ❍ `/set var` <newvar> <vavariable>*:* Add new variable or update existing value variable.
 ❍ `/del var` <var>*:* Delete existing variable.
 ❍ `/logs` Get heroku dyno logs.

`⚠️ Read from top`
Visit @{SUPPORT_CHAT} for more information.
"""

SUDO_HANDLER = CommandHandler(("addhashira", "addsudo", "adddragon"), addsudo, run_async=True)
SUPPORT_HANDLER = CommandHandler(("addsupport", "addlowermoon", "adddemon"), addsupport, run_async=True)
TIGER_HANDLER = CommandHandler(("adddemonslayer", "addtiger"), addtiger, run_async=True)
WHITELIST_HANDLER = CommandHandler(("addwhitelist", "addslave", "addwolf"), addwhitelist, run_async=True)
UNSUDO_HANDLER = CommandHandler(("removesudo", "removehashira", "removedragon"), removesudo, run_async=True)
UNSUPPORT_HANDLER = CommandHandler(("removesupport", "removelowermoon", "removedemon"), removesupport, run_async=True)
UNTIGER_HANDLER = CommandHandler(("removedemonslayer", "removetiger"), removetiger, run_async=True)
UNWHITELIST_HANDLER = CommandHandler(("removedemon", "removeslave", "removewolf"), removewhitelist, run_async=True)

WHITELISTLIST_HANDLER = CommandHandler(["slavelist", "demons", "demons", "wolflist"], whitelistlist, run_async=True)
TIGERLIST_HANDLER = CommandHandler(["demonslayers", "demonslayer", "tigers", "tigerlist"], tigerlist, run_async=True)
SUPPORTLIST_HANDLER = CommandHandler(["lowermoon", "lowermoons"], supportlist, run_async=True)
SUDOLIST_HANDLER = CommandHandler(["hashira", "hashiras", "sudos", "dragons", "sudolist", "dragonlist"], sudolist, run_async=True)
DEVLIST_HANDLER = CommandHandler(["uppermoon", "uppermoons", "devs"], devlist, run_async=True)

dispatcher.add_handler(SUDO_HANDLER)
dispatcher.add_handler(SUPPORT_HANDLER)
dispatcher.add_handler(TIGER_HANDLER)
dispatcher.add_handler(WHITELIST_HANDLER)
dispatcher.add_handler(UNSUDO_HANDLER)
dispatcher.add_handler(UNSUPPORT_HANDLER)
dispatcher.add_handler(UNTIGER_HANDLER)
dispatcher.add_handler(UNWHITELIST_HANDLER)

dispatcher.add_handler(WHITELISTLIST_HANDLER)
dispatcher.add_handler(TIGERLIST_HANDLER)
dispatcher.add_handler(SUPPORTLIST_HANDLER)
dispatcher.add_handler(SUDOLIST_HANDLER)
dispatcher.add_handler(DEVLIST_HANDLER)

__mod_name__ = "ᴅᴇᴠ"
__handlers__ = [
    SUDO_HANDLER,
    SUPPORT_HANDLER,
    TIGER_HANDLER,
    WHITELIST_HANDLER,
    UNSUDO_HANDLER,
    UNSUPPORT_HANDLER,
    UNTIGER_HANDLER,
    UNWHITELIST_HANDLER,
    WHITELISTLIST_HANDLER,
    TIGERLIST_HANDLER,
    SUPPORTLIST_HANDLER,
    SUDOLIST_HANDLER,
    DEVLIST_HANDLER,
]
