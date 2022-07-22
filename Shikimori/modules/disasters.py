"""
STATUS: Code is working. ✅
"""

"""
BSD 2-Clause License

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

Credits:-
    I don't know who originally wrote this code. If you originally wrote this code, please reach out to me. 

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
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
        message.reply_text("𝚃𝙷𝙸𝚂 𝙼𝙴𝙼𝙱𝙴𝚁 𝙸𝚂 𝙰 𝚉 𝙼𝙾𝙳")
        return ""

    if user_id in DEMONS:
        rt += "𝙿𝚁𝙾𝙼𝙾𝚃𝙴𝙳 𝚃𝙾 𝚉 𝙼𝙾𝙳"
        data["supports"].remove(user_id)
        DEMONS.remove(user_id)

    if user_id in WOLVES:
        rt += "𝙿𝚁𝙾𝙼𝙾𝚃𝙴𝙳 𝚃𝙾 𝚉 𝙼𝙾𝙳"
        data["whitelists"].remove(user_id)
        WOLVES.remove(user_id)

    data["sudos"].append(user_id)
    DRAGONS.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt
        + "\n𝙿𝚁𝙾𝙼𝙾𝚃𝙴𝙳 𝚃𝙾 {} 𝚉 𝙼𝙾𝙳!".format(
            user_member.first_name
        )
    )

    log_message = (
        f"#Friend\n"
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
        rt += "𝙳𝙴𝙼𝙾𝚃𝙴𝙳 𝚃𝙾 𝚇 𝙼𝙾𝙳 "
        data["sudos"].remove(user_id)
        DRAGONS.remove(user_id)

    if user_id in DEMONS:
        message.reply_text("𝚃𝙷𝙸𝚂 𝚄𝚂𝙴𝚁 𝙸𝚂 𝙰𝙻𝚁𝙴𝙰𝙳𝚈 𝙰 𝚉 𝙼𝙾𝙳")
        return ""

    if user_id in WOLVES:
        rt += "PROMOTED TO X MOD"
        data["whitelists"].remove(user_id)
        WOLVES.remove(user_id)

    data["supports"].append(user_id)
    DEMONS.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt + f"\n{user_member.first_name} 𝙿𝚁𝙾𝙼𝙾𝚃𝙴𝙳 𝚃𝙾 𝚇 𝙼𝙾𝙳!"
    )

    log_message = (
        f"#Servant\n"
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
        rt += "𝙳𝙴𝙼𝙾𝚃𝙴𝙳 𝚃𝙾 𝚃𝚁𝚄𝚂𝚃𝙴𝙳 "
        data["sudos"].remove(user_id)
        DRAGONS.remove(user_id)

    if user_id in DEMONS:
        rt += "𝙳𝙴𝙼𝙾𝚃𝙴𝙳 𝚃𝙾 𝚃𝚁𝚄𝚂𝚃𝙴𝙳 "
        data["supports"].remove(user_id)
        DEMONS.remove(user_id)

    if user_id in WOLVES:
        message.reply_text("𝚃𝙷𝙸𝚂 𝙼𝙴𝙼𝙱𝙴𝚁 𝙸𝚂 𝙰 𝚃𝚁𝚄𝚂𝚃𝙴𝙳 ")
        return ""

    data["whitelists"].append(user_id)
    WOLVES.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt + f"\n𝙿𝚁𝙾𝙼𝙾𝚃𝙴𝙳 {user_member.first_name} 𝚃𝙾 𝚃𝚁𝚄𝚂𝚃𝙴𝙳 "
    )

    log_message = (
        f"#Slave\n"
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
        rt += "𝙳𝙴𝙼𝙾𝚃𝙴𝙳 𝚃𝙾 𝚈 𝙼𝙾𝙳."
        data["sudos"].remove(user_id)
        DRAGONS.remove(user_id)

    if user_id in DEMONS:
        rt += "𝙳𝙴𝙼𝙾𝚃𝙴𝙳 𝚃𝙾 𝚈 𝙼𝙾𝙳"
        data["supports"].remove(user_id)
        DEMONS.remove(user_id)

    if user_id in WOLVES:
        rt += "𝙿𝚁𝙾𝙼𝙾𝚃𝙴𝙳 𝚃𝙾 𝚈 𝙼𝙾𝙳 "
        data["whitelists"].remove(user_id)
        WOLVES.remove(user_id)

    if user_id in TIGERS:
        message.reply_text("𝚃𝙷𝙸𝚂 𝚄𝚂𝙴𝚁 𝙸𝚂 𝙰𝙻𝚁𝙴𝙰𝙳𝚈 𝙰 𝚈 𝙼𝙾𝙳")
        return ""

    data["tigers"].append(user_id)
    TIGERS.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt + f"\n𝙿𝚁𝙾𝙼𝙾𝚃𝙴𝙳 {user_member.first_name} 𝚈 𝙼𝙾𝙳"
    )

    log_message = (
        f"#Peasant\n"
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
        message.reply_text("𝚁𝙴𝙼𝙾𝚅𝙴𝙳 𝙵𝚁𝙾𝙼 𝚉 𝙼𝙾𝙳")
        DRAGONS.remove(user_id)
        data["sudos"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"#UNFriend\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = "<b>{}:</b>\n".format(html.escape(chat.title)) + log_message

        return log_message

    else:
        message.reply_text("𝚃𝙷𝙸𝚂 𝚄𝚂𝙴𝚁 𝚆𝙰𝚂 𝙽𝙾𝚃 𝚉 𝙼𝙾𝙳")
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
        message.reply_text("𝚁𝙴𝙼𝙾𝚅𝙴𝙳 𝙵𝚁𝙾𝙼 𝚇 𝙼𝙾𝙳")
        DEMONS.remove(user_id)
        data["supports"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"#UNServant\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

        return log_message

    else:
        message.reply_text("𝚃𝙷𝙸𝚂 𝚄𝚂𝙴𝚁 𝚆𝙰𝚂 𝙽𝙾𝚃 𝚇 𝙼𝙾𝙳")
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
        message.reply_text("𝚁𝙴𝙼𝙾𝚅𝙴𝙳 𝙵𝚁𝙾𝙼 𝚃𝚁𝚄𝚂𝚃𝙴𝙳")
        WOLVES.remove(user_id)
        data["whitelists"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"#UNSlave\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

        return log_message
    else:
        message.reply_text("𝚃𝙷𝙸𝚂 𝚄𝚂𝙴𝚁 𝚆𝙰𝚂 𝙽𝙾𝚃 𝚃𝚁𝚄𝚂𝚃𝙴𝙳")
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
        message.reply_text("𝚁𝙴𝙼𝙾𝚅𝙴𝙳 𝙵𝚁𝙾𝙼 𝚈 𝙼𝙾𝙳")
        TIGERS.remove(user_id)
        data["tigers"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"#UNPeasant\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

        return log_message
    else:
        message.reply_text("𝚃𝙷𝙸𝚂 𝚄𝚂𝙴𝚁 𝚆𝙰𝚂 𝙽𝙾𝚃 𝚈 𝙼𝙾𝙳")
        return ""



def whitelistlist(update: Update, context: CallbackContext):
    reply = "<b>Known TRUSTED:</b>\n"
    m = update.effective_message.reply_text(
        "<code>Gathering intel..</code>", parse_mode=ParseMode.HTML
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



def tigerlist(update: Update, context: CallbackContext):
    reply = "<b>Known Y MODS:</b>\n"
    m = update.effective_message.reply_text(
        "<code>Gathering intel..</code>", parse_mode=ParseMode.HTML
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



def supportlist(update: Update, context: CallbackContext):
    bot = context.bot
    m = update.effective_message.reply_text(
        "<code>Gathering intel..</code>", parse_mode=ParseMode.HTML
    )
    reply = "<b>Known X MODS:</b>\n"
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
        "<code>Gathering intel..</code>", parse_mode=ParseMode.HTML
    )
    true_sudo = list(set(DRAGONS) - set(DEV_USERS))
    reply = "<b>Known Z MODS:</b>\n"
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
        "<code>Gathering intel..</code>", parse_mode=ParseMode.HTML
    )
    true_dev = list(set(DEV_USERS) - {OWNER_ID})
    reply = "<b>Best Friends:</b>\n"
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

*List all special users:*
 ❍ `/dragons`*:* Lists all Dragon disasters
 ❍ `/demons`*:* Lists all Demon disasters
 ❍ `/tigers`*:* Lists all Tigers disasters
 ❍ `/wolves`*:* Lists all Wolf disasters
 ❍ `/devs`*:* Lists all Dev members
 ❍ `/adddragon`*:* Adds a user to Dragon
 ❍ `/adddemon`*:* Adds a user to Demon
 ❍ `/addtiger`*:* Adds a user to Tiger
 ❍ `/addwolf`*:* Adds a user to Wolf
 ❍ `Add dev doesnt exist, devs should know how to add themselves. AKA, why are you even dev if you don't have access to the bot vars.`

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

SUDO_HANDLER = CommandHandler(("addfriend", "addzmod", "adddragon"), addsudo, run_async=True)
SUPPORT_HANDLER = CommandHandler(("addsupport", "addxmod", "adddemon"), addsupport, run_async=True)
TIGER_HANDLER = CommandHandler(("addymod", "addtiger"), addtiger, run_async=True)
WHITELIST_HANDLER = CommandHandler(("addwhitelist", "addtrusted", "addwolf"), addwhitelist, run_async=True)
UNSUDO_HANDLER = CommandHandler(("removesudo", "removezmod", "removedragon"), removesudo, run_async=True)
UNSUPPORT_HANDLER = CommandHandler(("removesupport", "removexmod", "removedemon"), removesupport, run_async=True)
UNTIGER_HANDLER = CommandHandler(("removepeasant", "removeymod"), removetiger, run_async=True)
UNWHITELIST_HANDLER = CommandHandler(("removewhitelist", "removetrusted", "removewolf"), removewhitelist, run_async=True)

WHITELISTLIST_HANDLER = CommandHandler(["slavelist", "listtrusted", "wolves", "wolflist"], whitelistlist, run_async=True)
TIGERLIST_HANDLER = CommandHandler(["peasantlist", "listymods", "tigers", "tigerlist"], tigerlist, run_async=True)
SUPPORTLIST_HANDLER = CommandHandler(["servantlist", "listxmods", "demons", "demonlist"], supportlist, run_async=True)
SUDOLIST_HANDLER = CommandHandler(["friendlist", "listzmods", "sudos", "dragons", "sudolist", "dragonlist"], sudolist, run_async=True)
DEVLIST_HANDLER = CommandHandler(["devlist", "bestfriends", "devs"], devlist, run_async=True)

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
