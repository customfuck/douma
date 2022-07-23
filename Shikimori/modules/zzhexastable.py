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

def lonely(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ LONELY Pokemons ⚡️\n\n👍 Lonely\n\n👉 Effects :\n👉 Stats increase⬆️  : Attack\n👉 Stats decrease⬇️ : Defense",
    )

def brave(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ BRAVE Pokemons ⚡️\n\n👍 Brave\n\n👉 Effects :\n👉 Stats increase⬆️  : Attack\n👉 Stats decrease⬇️ : Speed",
    )

def adamant(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ ADAMANT Pokemons ⚡️\n\n👍 Adamant\n\n👉 Effects :\n👉 Stats increase⬆️  : Attack\n👉 Stats decrease⬇️ : Sp. Attack",
    )

def naughty(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ NAUGHTY Pokemons ⚡️\n\n👍 Naughty\n\n👉 Effects :\n👉 Stats increase⬆️  : Attack\n👉 Stats decrease⬇️ : Sp. Defense",
    )

def bold(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ BOLD Pokemons ⚡️\n\n👍 Bold\n\n👉 Effects :\n👉 Stats increase⬆️  : Defence\n👉 Stats decrease⬇️ : Attack",
    )

def relaxed(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ RELAXED Pokemons ⚡️\n\n👍 Relaxed\n\n👉 Effects :\n👉 Stats increase⬆️  : Defence\n👉 Stats decrease⬇️ : Speed",
    )

def impish(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ IMPISH Pokemons ⚡️\n\n👍 Impish\n\n👉 Effects :\n👉 Stats increase⬆️  : Defence\n👉 Stats decrease⬇️ : Sp. Attack",
    )

def lax(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ LAX Pokemons ⚡️\n\n👍 Lax\n\n👉 Effects :\n👉 Stats increase⬆️  : Defence\n👉 Stats decrease⬇️ : Sp. Defense",
    )

def timid(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ TIMID Pokemons ⚡️\n\n👍 Timid\n\n👉 Effects :\n👉 Stats increase⬆️  : Speed\n👉 Stats decrease⬇️ : Attack",
    )

def hasty(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ HASTY Pokemons ⚡️\n\n👍 Hasty\n\n👉 Effects :\n👉 Stats increase⬆️  : Speed\n👉 Stats decrease⬇️ : Defense",
    )

def jolly(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ JOLLY Pokemons ⚡️\n\n👍 Jolly\n\n👉 Effects :\n👉 Stats increase⬆️  : Speed\n👉 Stats decrease⬇️ : Sp. Attack",
    )

def naive(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ NAIVE Pokemons ⚡️\n\n👍 Naive\n\n👉 Effects :\n👉 Stats increase⬆️  : Speed\n👉 Stats decrease⬇️ : Sp. Defense",
    )

def modest(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ MODEST Pokemons ⚡️\n\n👍 Modest\n\n👉 Effects :\n👉 Stats increase⬆️  : Sp. Attack\n👉 Stats decrease⬇️ : Attack",
    )

def mild(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ MILD Pokemons ⚡️\n\n👍 Mild\n\n👉 Effects :\n👉 Stats increase⬆️  : Sp. Attack\n👉 Stats decrease⬇️ : Defense",
    )

def quiet(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ Quiet Pokemons ⚡️\n\n👍 Quiet\n\n👉 Effects :\n👉 Stats increase⬆️  : Sp. Attack\n👉 Stats decrease⬇️ : Speed",
    )

def rash(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ RASH Pokemons ⚡️\n\n👍 Rash\n\n👉 Effects :\n👉 Stats increase⬆️  : Sp. Attack\n👉 Stats decrease⬇️ : Sp. Defense",
    )

def calm(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ CALM Pokemons ⚡️\n\n👍 Calm\n\n👉 Effects :\n👉 Stats increase⬆️  : Sp. Defense\n👉 Stats decrease⬇️ : Attack",
    )

def gentle(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ GENTLE Pokemons ⚡️\n\n👍 Gentle\n\n👉 Effects :\n👉 Stats increase⬆️  : Sp. Defense\n👉 Stats decrease⬇️ : Defense",
    )

def sassy(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ SASSY Pokemons ⚡️\n\n👍 Sassy\n\n👉 Effects :\n👉 Stats increase⬆️  : Sp. Defense\n👉 Stats decrease⬇️ : Speed",
    )

def careful(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ CAREFUL Pokemons ⚡️\n\n👍 Careful\n\n👉 Effects :\n👉 Stats increase⬆️  : Sp. Defense\n👉 Stats decrease⬇️ : Sp. Attack",
    )

def hardy(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ HARDY Pokemons ⚡️\n\n👍 Hardy\n\n👉 Effects :\n👉 Stats increase⬆️  : None\n👉 Stats decrease⬇️ : None",
    )

def docile(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ DOCILE Pokemons ⚡️\n\n👍 Docile\n\n👉 Effects :\n👉 Stats increase⬆️  : None\n👉 Stats decrease⬇️ : None",
    )

def serious(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ SERIOUS Pokemons ⚡️\n\n👍 Serious\n\n👉 Effects :\n👉 Stats increase⬆️  : None\n👉 Stats decrease⬇️ : None",
    )

def bashful(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ BASHFUL Pokemons ⚡️\n\n👍 Bashful\n\n👉 Effects :\n👉 Stats increase⬆️  : None\n👉 Stats decrease⬇️ : None",
    )

def quirky(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ QUIRKY Pokemons ⚡️\n\n👍 Quirky\n\n👉 Effects :\n👉 Stats increase⬆️  : None\n👉 Stats decrease⬇️ : None",
    )
    
def normal(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Normal\n\nStrong Against (Damage Given X2):\nNone\n\nWeak Against (Damage Given X1/2):\nRock, Steel\nGhost (Damage Given X0)\n\nResistant To (Damage Recived X0):\nGhost\n\nVulnerable To (Damage Recived X2):\nFighting",
    )

def fighting(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Fighting\n\nStrong Against (Damage Given X2):\nNormal, Rock, Steel, Ice, Dark\n\nWeak Against (Damage Given X1/2):\nFlying, Poison, Psychic, Bug, Fairy\nGhost (Damage Given X0)\n\nResistant To (Damage Recived X1/2):\nRock, Bug, Dark\n\nVulnerable To (Damage Recived X2):\nFlying, Psychic, Fairy",
    )

def flying(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Flying\n\nStrong Against (Damage Given X2):\nFighting, Bug, Grass\n\nWeak Against (Damage Given X1/2):\nRock, Steel, Electric\n\nResistant To (Damage Recived X1/2):\nFighting, Bug, Grass\nGround (Damage Recived X0)\n\nVulnerable To (Damage Recived X2):\nRock, Electric, Ice",
    )

def poison(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Poison\n\nStrong Against (Damage Given X2):\nGrass, Fairy\n\nWeak Against (Damage Given X1/2):\nPoison, Ground, Rock, Ghost\nSteel (Damage Given X0)\n\nResistant To (Damage Recived X1/2):\nFighting, Poison, Grass, Fairy, Bug\n\nVulnerable To (Damage Recived X2):\nGround, Psychic",
    )

def ground(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Ground\n\nStrong Against (Damage Given X2):\nPoison, Rock, Steel, Fire, Electric\n\nWeak Against (Damage Given X1/2):\nBug, Grass\nFlying (Damage Given X0)\n\nResistant To (Damage Recived X1/2):\nPoison, Rock\nElectric (Damage Recived X0)\n\nVulnerable To (Damage Recived X2):\nWater, Grass, Ice",
    )

def rock(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Rock\n\nStrong Against (Damage Given X2):\nFlying, Bug, Fire, Ice\n\nWeak Against (Damage Given X1/2):\nFighting, Ground, Steel\n\nResistant To (Damage Recived X1/2):\nNormal, Flying, Poison, Fire\n\nVulnerable To (Damage Recived X2):\nFighting, Ground, Steel, Water, Grass",
    )
def bug(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Bug\n\nStrong Against (Damage Given X2):\nGrass, Psychic, Dark\n\nWeak Against (Damage Given X1/2):\nFighting, Flying, Poison, Ghost, Steel, Fire, Fairy\n\nResistant To (Damage Recived X1/2):\nFighting, Ground, Grass\n\nVulnerable To (Damage Recived X2):\nFlying, Rock, Fire",
    )

def ghost(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Ghost\n\nStrong Against (Damage Given X2):\nGhost, Psychic\n\nWeak Against (Damage Given X1/2):\nDark\nNormal (Damage Given X0)\n\nResistant To (Damage Recived X1/2):\nPoison, Bug\nNormal, Fighting (Damage Recived X0)\n\nVulnerable To (Damage Recived X2):\nGhost, Dark",
    )

def steel(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Steel\n\nStrong Against (Damage Given X2):\nRock, Ice, Fairy\n\nWeak Against (Damage Given X1/2):\nSteel, Fire, Water, Electric\n\nResistant To (Damage Recived X1/2):\nNormal, Flying, Rock, Bug, Steel, Grass, Psychic, Ice, Dragon, Fairy\nPoison (Damage Recived X0)\n\nVulnerable To (Damage Recived X2):\nFighting, Ground, Fire",
    )

def fire(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Fire\n\nStrong Against (Damage Given X2):\nBug, Steel, Grass, Ice\n\nWeak Against (Damage Given X1/2):\nRock, Fire, Water, Dragon\n\nResistant To (Damage Recived X1/2):\nBug, Steel, Fire, Grass, Ice, Fairy\n\nVulnerable To (Damage Recived X2):\nGround, Rock, Water",
    )

def water(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Water\n\nStrong Against (Damage Given X2):\nGround, Rock, Fire\n\nWeak Against (Damage Given X1/2):\nWater, Grass, Dragon\n\nResistant To (Damage Recived X1/2):\nSteel, Fire, Water, Ice\n\nVulnerable To (Damage Recived X2):\nGrass, Electric",
    )

def grass(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Grass\n\nStrong Against (Damage Given X2):\nGround, Rock, Water\n\nWeak Against (Damage Given X1/2):\nFlying, Poison, Bug, Steel, Fire, Grass, Dragon\n\nResistant To (Damage Recived X1/2):\nGround, Water, Grass, Electric\n\nVulnerable To (Damage Recived X2):\nFlying, Poison, Bug, Fire, Ice",
    )

def electric(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Electric\n\nStrong Against (Damage Given X2):\nFlying, Water\n\nWeak Against (Damage Given X1/2):\nGrass, Electric, Dragon\nGround (Damage Given X0)\n\nResistant To (Damage Recived X1/2):\nFlying, Steel, Electric\n\nVulnerable To (Damage Recived X2):\nGround",
    )

def psychic(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Psychic\n\nStrong Against (Damage Given X2):\nFighting, Poison\n\nWeak Against (Damage Given X1/2):\nSteel, Psychic\nDark (Damage Given X0)\n\nResistant To (Damage Recived X1/2:)\nFighting, Psychic\n\nVulnerable To (Damage Recived X2):\nBug, Ghost, Dark",
    )

def ice(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Ice\n\nStrong Against (Damage Given X2):\nFlying, Ground, Grass, Dragon\n\nWeak Against (Damage Given X1/2):\nSteel, Fire, Water, Ice\n\nResistant To (Damage Recived X1/2):\nIce\n\nVulnerable To (Damage Recived X2):\nFighting, Rock, Steel, Fire",
    )

def dragon(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Dragon\n\nStrong Against (Damage Given X2):\nDragon\n\nWeak Against (Damage Given X1/2):\nSteel\nFairy (Damage Given X0)\n\nResistant To (Damage Recived X1/2):\nFire, Water, Grass, Electric\n\nVulnerable To (Damage Recived X2):\nIce, Dragon, Fairy",
    )

def dark(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Dark\n\nStrong Against (Damage Given X2):\nGhost, Psychic\n\nWeak Against (Damage Given X1/2):\nFighting, Dark, Fairy\n\nResistant To (Damage Recived X1/2):\nGhost, Dark\nPsychic (Damaged Recived X0)\n\nVulnerable To (Damage Recived X2):\nFighting, Bug, Fairy",
    )

def fairy(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Fairy\n\nStrong Against (Damage Given X2):\nFighting, Dragon, Dark\n\nWeak Against (Damage Given X1/2):\nPoison, Steel, Fire\n\nResistant To (Damage Recived X1/2):\nFighting, Bug, Dark\nDragon (Damage Recived X0)\n\nVulnerable To (Damage Recived X2):\nPoison, Steel",
    )
    
def gbam(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "This person has been succesfully gbammed. Took 1.8 sec to gbam",
    )
    
def natures(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Nature are a mechanic that influences how a Pokémon stats grow.\nNature effect is limited to only 10%.\nHere are the list of commands\n\n/hardy - About hardy natured pokemon.\n/lonely - About lonely natured pokemon.\n/brave - About brave natured pokemon.\n/adamant - About adamant natured pokemon.\n/naughty - About naughty natured pokemon.\n/bold - About bold natured pokemon.\n/docile - About docile natured pokemon.\n/relaxed - About relaxed natured pokemon.\n/impish - About impish natured pokemon.\n/lax - About lax natured pokemon.\n/modest - About modest natured pokemon.\n/mild - About mild natured pokemon.\n/serious - About serious natured pokemon.\n/quiet - About quiet natured pokemon.\n/rash - About rash natured pokemon.\n/calm - About calm natured pokemon.\n/gentle - About gentle natured pokemon.\n/sassy - About sassy natured pokemon.\n/bashful - About bashful natured pokemon.\n/careful - About careful natured pokemon.\n/timid - About timid natured pokemon.\n/hasty - About hasty natured pokemon.\n/jolly - About jolly natured pokemon.\n/naive - About naive natured pokemon.\n/quirky - About quirky natured pokemon",
    )
    
def attack(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "3 ATTACK POKEMONS\n\nNORMAL\n\n👉 Nidoking\n👉 Machamp\n👉 Victreebel\n👉 Dragonite\n👉 Tyranitar\n👉 Blaziken\n👉 Swampert\n👉 Shiftry\n👉 Salamence\n👉 Staraptor\n👉 Luxray\n👉 Garchomp\n👉 Rhyperior\n👉 Electivire\n👉 Mamoswine\n👉 Gallade\n👉 Emboar\n👉 Stoutland\n👉 Unfezant\n👉 Gigalith\n👉 Conkeldurr\n👉 Leavanny\n👉 Krookodile\n👉 Eelektross\n👉 Haxorus\n👉 Decidueye\n👉 Incineroar\n👉 Toucannon\n👉 Tsareena\n\nLEGENDARY\n\n👉 Groudon\n👉 Regigigas\n👉 Tornadus(Incarnate Forme)\n👉 Thundurus(Incarnate Forme)\n👉 Landorus(Therian Forme)\n👉 Terrakion\n👉 Zekrom\n👉 Kyurem(Black)\n👉 Tapu Bulu\n👉 Solgalao\n👉 Kartana\n👉 Necrozma Dusk mane\n👉 Melmetal",
    )

def defence(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "3 DEFENCE POKEMONS\n\nNORMAL\n\n👉 Poliwrath\n👉 Golem\n👉 Aggron\n👉 Metagross\n👉 Klinklang\n👉 Chesnaught\n👉 Kommo-o\n\nLEGENDARY\n\n👉 Regirock\n👉 Cobalion\n👉 Stakataka  ",
    )

def spa(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "3 SPECIAL ATTACK POKEMONS\n\nNORMAL\n\n👉 Charizard\n👉 Vileplume\n👉 Alakazam\n👉 Gengar\n👉 Typhlosion\n👉 Ampharos\n👉 Beautifly\n👉 Gardevoir\n👉 Empolion\n👉 Roserade\n👉 Magnezone\n👉 Magmortar\n👉 Porygon-Z \n👉 Samurott\n👉 Reuniclus\n👉 Vanilluxe\n👉 Chandelure\n👉 Hydreigon\n👉 Volcarona\n👉 Delphox\n👉 Primarina\n👉 Vikavolt\n\nLEGENDARY\n\n👉 Zapdos\n👉 Moltres\n👉 Mewtwo\n👉 Latios\n👉 Kyogre\n👉 Dialga\n👉 Palkia\n👉 Reshiram\n👉 Volcanion\n👉 Lunala\n👉 Xurkitree\n👉 Magearna\n👉 Naganadel\n👉 Blacephalon\n👉 Tapu Lele\n👉 Heatran\n👉 Thundurus(Therian Forme)\n👉 Landorus(Incarnate Forme)\n👉 Keldeo(Ordinary/Resolute)\n👉 Kyurem(White)\n👉 Hoopa(Confined/Unbound)\n👉 Necrozma Dawn Wings",
    )

def spd(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "3 SPECIAL DEFENCE POKEMONS\n\nNORMAL\n\n👉 Blastoise\n👉 Bellossom\n👉 Politoed\n👉 Dustox\n👉 Ludicolo\n👉 Gothitelle\n👉 Florges\n👉 Goodra\n\nLEGENDARY\n\n👉 Articuno\n👉 Lugia\n👉 Ho-oh\n👉 Regice\n👉 Latias\n👉 Cresselia\n👉 Virizion\n👉 Tapu Fini\n👉 Nihilego",
    )

def speed(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "3 SPEED POKEMONS\n\nNORMAL\n\n👉 Pidgeot\n👉 Raichu\n👉 Crobat\n👉 Jumpluff\n👉 Sceptile\n👉 Serperior\n👉 Greninja\n👉 Talonflame\n\nLEGENDARY\n\n👉 Shaymin\n👉 Scolipede\n👉 Pheromosa\n👉 Zeraora\n👉 Tapu Koko\n👉 Tornadus(Therian Forme)\n👉 Deoxys(Speed Forme)",
    )

    

LONELY_HANDLER = DisableAbleCommandHandler("lonely", lonely, run_async=True)
BRAVE_HANDLER = DisableAbleCommandHandler("brave", brave, run_async=True)
ADAMANT_HANDLER = DisableAbleCommandHandler("adamant", adamant, run_async=True)
NAUGHTY_HANDLER = DisableAbleCommandHandler("naughty", naughty, run_async=True)
BOLD_HANDLER = DisableAbleCommandHandler("bold", bold, run_async=True)
RELAXED_HANDLER = DisableAbleCommandHandler("relaxed", relaxed, run_async=True)
IMPISH_HANDLER = DisableAbleCommandHandler("impish", impish, run_async=True)
LAX_HANDLER = DisableAbleCommandHandler("lax", lax, run_async=True)
TIMID_HANDLER = DisableAbleCommandHandler("timid", timid, run_async=True)
HASTY_HANDLER = DisableAbleCommandHandler("hasty", hasty, run_async=True)
JOLLY_HANDLER = DisableAbleCommandHandler("jolly", jolly, run_async=True)
NAIVE_HANDLER = DisableAbleCommandHandler("naive", naive, run_async=True)
MODEST_HANDLER = DisableAbleCommandHandler("modest", modest, run_async=True)
MILD_HANDLER = DisableAbleCommandHandler("mild", mild, run_async=True)
QUIET_HANDLER = DisableAbleCommandHandler("quiet", quiet, run_async=True)
RASH_HANDLER = DisableAbleCommandHandler("rash", rash, run_async=True)
CALM_HANDLER = DisableAbleCommandHandler("calm", calm, run_async=True)
GENTLE_HANDLER = DisableAbleCommandHandler("gentle", gentle, run_async=True)
SASSY_HANDLER = DisableAbleCommandHandler("sassy", sassy, run_async=True)
CAREFUL_HANDLER = DisableAbleCommandHandler("careful", careful, run_async=True)
HARDY_HANDLER = DisableAbleCommandHandler("hardy", hardy, run_async=True)
DOCILE_HANDLER = DisableAbleCommandHandler("docile", docile, run_async=True)
SERIOUS_HANDLER = DisableAbleCommandHandler("serious", serious, run_async=True)
BASHFUL_HANDLER = DisableAbleCommandHandler("bashful", bashful, run_async=True)
QUIRKY_HANDLER = DisableAbleCommandHandler("quirky", quirky, run_async=True)
NORMAL_HANDLER = DisableAbleCommandHandler("normal", normal, run_async=True)
FIGHTING_HANDLER = DisableAbleCommandHandler("fighting", fighting, run_async=True)
FLYING_HANDLER = DisableAbleCommandHandler("flying", flying, run_async=True)
POISON_HANDLER = DisableAbleCommandHandler("poison", poison, run_async=True)
GROUND_HANDLER = DisableAbleCommandHandler("ground", ground, run_async=True)
ROCK_HANDLER = DisableAbleCommandHandler("rock", rock, run_async=True)
BUG_HANDLER = DisableAbleCommandHandler("bug", bug, run_async=True)
GHOST_HANDLER = DisableAbleCommandHandler("ghost", ghost, run_async=True)
STEEL_HANDLER = DisableAbleCommandHandler("steel", steel, run_async=True)
FIRE_HANDLER = DisableAbleCommandHandler("fire", fire, run_async=True)
WATER_HANDLER = DisableAbleCommandHandler("water", water, run_async=True)
GRASS_HANDLER = DisableAbleCommandHandler("grass", grass, run_async=True)
ELECTRIC_HANDLER = DisableAbleCommandHandler("electric", electric, run_async=True)
PSYCHIC_HANDLER = DisableAbleCommandHandler("psychic", psychic, run_async=True)
ICE_HANDLER = DisableAbleCommandHandler("ice", ice, run_async=True)
DRAGON_HANDLER = DisableAbleCommandHandler("dragon", dragon, run_async=True)
DARK_HANDLER = DisableAbleCommandHandler("dark", dark, run_async=True)
FAIRY_HANDLER = DisableAbleCommandHandler("fairy", fairy, run_async=True)
GBAM_HANDLER = DisableAbleCommandHandler("gbam", gbam, run_async=True)
NATURES_HANDLER = DisableAbleCommandHandler("natures", natures, run_async=True)
ATTACK_HANDLER = DisableAbleCommandHandler("attack", attack, run_async=True)
DEFENCE_HANDLER = DisableAbleCommandHandler("defence", defence, run_async=True)
SPA_HANDLER = DisableAbleCommandHandler("spa", spa, run_async=True)
SPD_HANDLER = DisableAbleCommandHandler("spd", spd, run_async=True)
SPEED_HANDLER = DisableAbleCommandHandler("speed", speed, run_async=True)

dispatcher.add_handler(LONELY_HANDLER)
dispatcher.add_handler(BRAVE_HANDLER)
dispatcher.add_handler(ADAMANT_HANDLER)
dispatcher.add_handler(NAUGHTY_HANDLER)
dispatcher.add_handler(BOLD_HANDLER)
dispatcher.add_handler(RELAXED_HANDLER)
dispatcher.add_handler(IMPISH_HANDLER)
dispatcher.add_handler(LAX_HANDLER)
dispatcher.add_handler(TIMID_HANDLER)
dispatcher.add_handler(HASTY_HANDLER)
dispatcher.add_handler(JOLLY_HANDLER)
dispatcher.add_handler(NAIVE_HANDLER)
dispatcher.add_handler(MODEST_HANDLER)
dispatcher.add_handler(MILD_HANDLER)
dispatcher.add_handler(QUIET_HANDLER)
dispatcher.add_handler(RASH_HANDLER)
dispatcher.add_handler(CALM_HANDLER)
dispatcher.add_handler(GENTLE_HANDLER)
dispatcher.add_handler(SASSY_HANDLER)
dispatcher.add_handler(CAREFUL_HANDLER)
dispatcher.add_handler(HARDY_HANDLER)
dispatcher.add_handler(DOCILE_HANDLER)
dispatcher.add_handler(SERIOUS_HANDLER)
dispatcher.add_handler(BASHFUL_HANDLER)
dispatcher.add_handler(QUIRKY_HANDLER)
dispatcher.add_handler(NORMAL_HANDLER)
dispatcher.add_handler(FIGHTING_HANDLER)
dispatcher.add_handler(FLYING_HANDLER)
dispatcher.add_handler(POISON_HANDLER)
dispatcher.add_handler(GROUND_HANDLER)
dispatcher.add_handler(ROCK_HANDLER)
dispatcher.add_handler(BUG_HANDLER)
dispatcher.add_handler(GHOST_HANDLER)
dispatcher.add_handler(STEEL_HANDLER)
dispatcher.add_handler(FIRE_HANDLER)
dispatcher.add_handler(WATER_HANDLER)
dispatcher.add_handler(GRASS_HANDLER)
dispatcher.add_handler(ELECTRIC_HANDLER)
dispatcher.add_handler(PSYCHIC_HANDLER)
dispatcher.add_handler(ICE_HANDLER)
dispatcher.add_handler(DRAGON_HANDLER)
dispatcher.add_handler(DARK_HANDLER)
dispatcher.add_handler(FAIRY_HANDLER)
dispatcher.add_handler(GBAM_HANDLER)
dispatcher.add_handler(NATURES_HANDLER)
dispatcher.add_handler(ATTACK_HANDLER)
dispatcher.add_handler(DEFENCE_HANDLER)
dispatcher.add_handler(SPA_HANDLER)
dispatcher.add_handler(SPD_HANDLER)
dispatcher.add_handler(SPEED_HANDLER)
