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

import random

from Shikimori import dispatcher
from Shikimori.modules.disable import DisableAbleCommandHandler
from telegram import Update
from telegram.ext import CallbackContext

reactions = [
    "( ͡° ͜ʖ ͡°)",
    "( . •́ _ʖ •̀ .)",
    "( ಠ ͜ʖ ಠ)",
    "( ͡ ͜ʖ ͡ )",
    "(ʘ ͜ʖ ʘ)",
    "ヾ(´〇`)ﾉ♪♪♪",
    "ヽ(o´∀`)ﾉ♪♬",
    "♪♬((d⌒ω⌒b))♬♪",
    "└(＾＾)┐",
    "(￣▽￣)/♫•*¨*•.¸¸♪",
    "ヾ(⌐■_■)ノ♪",
    "乁( • ω •乁)",
    "♬♫♪◖(● o ●)◗♪♫♬",
    "(っ˘ڡ˘ς)",
    "( ˘▽˘)っ♨",
    "(　・ω・)⊃-[二二]",
    "(*´ー`)旦 旦(￣ω￣*)",
    "( ￣▽￣)[] [](≧▽≦ )",
    "(*￣▽￣)旦 且(´∀`*)",
    "(ノ ˘_˘)ノ　ζ|||ζ　ζ|||ζ　ζ|||ζ",
    "(ノ°∀°)ノ⌒･*:.｡. .｡.:*･゜ﾟ･*☆",
    "(⊃｡•́‿•̀｡)⊃━✿✿✿✿✿✿",
    "(∩` ﾛ ´)⊃━炎炎炎炎炎",
    "( ・∀・)・・・--------☆",
    "( -ω-)／占~~~~~",
    "○∞∞∞∞ヽ(^ー^ )",
    "(*＾＾)/~~~~~~~~~~◎",
    "((( ￣□)_／",
    "(ﾒ￣▽￣)︻┳═一",
    "ヽ( ･∀･)ﾉ_θ彡☆Σ(ノ `Д´)ノ",
    "(*`0´)θ☆(メ°皿°)ﾉ",
    "(; -_-)――――――C<―_-)",
    "ヽ(>_<ヽ) ―⊂|=0ヘ(^‿^ )",
    "(҂` ﾛ ´)︻デ═一 ＼(º □ º l|l)/",
    "/( .□.)＼ ︵╰(°益°)╯︵ /(.□. /)",
    "(`⌒*)O-(`⌒´Q)",
    "(っ•﹏•)っ ✴==≡눈٩(`皿´҂)ง",
    "ヾ(・ω・)メ(・ω・)ノ",
    "(*^ω^)八(⌒▽⌒)八(-‿‿- )ヽ",
    "ヽ( ⌒ω⌒)人(=^‥^= )ﾉ",
    "｡*:☆(・ω・人・ω・)｡:゜☆｡",
    "(°(°ω(°ω°(☆ω☆)°ω°)ω°)°)",
    "(っ˘▽˘)(˘▽˘)˘▽˘ς)",
    "(*＾ω＾)人(＾ω＾*)",
    r"＼(▽￣ \ (￣▽￣) / ￣▽)／",
    "(￣Θ￣)",
    "＼( ˋ Θ ´ )／",
    "( ´(00)ˋ )",
    "＼(￣(oo)￣)／",
    "／(≧ x ≦)＼",
    "／(=･ x ･=)＼",
    "(=^･ω･^=)",
    "(= ; ｪ ; =)",
    "(=⌒‿‿⌒=)",
    "(＾• ω •＾)",
    "ଲ(ⓛ ω ⓛ)ଲ",
    "ଲ(ⓛ ω ⓛ)ଲ",
    "(^◔ᴥ◔^)",
    "[(－－)]..zzZ",
    "(￣o￣) zzZZzzZZ",
    "(＿ ＿*) Z z z",
    "☆ﾐ(o*･ω･)ﾉ",
    "ε=ε=ε=ε=┌(;￣▽￣)┘",
    "ε===(っ≧ω≦)っ",
    "__φ(．．)",
    "ヾ( `ー´)シφ__",
    "( ^▽^)ψ__",
    "|･ω･)",
    "|д･)",
    "┬┴┬┴┤･ω･)ﾉ",
    "|･д･)ﾉ",
    "(*￣ii￣)",
    "(＾〃＾)",
    "m(_ _)m",
    "人(_ _*)",
    "(シ. .)シ",
    "(^_~)",
    "(>ω^)",
    "(^_<)〜☆",
    "(^_<)",
    "(づ￣ ³￣)づ",
    "(⊃｡•́‿•̀｡)⊃",
    "⊂(´• ω •`⊂)",
    "(*・ω・)ﾉ",
    "(^-^*)/",
    "ヾ(*'▽'*)",
    "(^０^)ノ",
    "(*°ｰ°)ﾉ",
    "(￣ω￣)/",
    "(≧▽≦)/",
    "w(°ｏ°)w",
    "(⊙_⊙)",
    "(°ロ°) !",
    "∑(O_O;)",
    "(￢_￢)",
    "(¬_¬ )",
    "(↼_↼)",
    "(￣ω￣;)",
    "┐('～`;)┌",
    "(・_・;)",
    "(＠_＠)",
    "(•ิ_•ิ)?",
    "ヽ(ー_ー )ノ",
    "┐(￣ヘ￣)┌",
    "┐(￣～￣)┌",
    "┐( ´ д ` )┌",
    "╮(︶▽︶)╭",
    "ᕕ( ᐛ )ᕗ",
    "(ノωヽ)",
    "(″ロ゛)",
    "(/ω＼)",
    "(((＞＜)))",
    "~(>_<~)",
    "(×_×)",
    "(×﹏×)",
    "(ノ_<。)",
    "(μ_μ)",
    "o(TヘTo)",
    "( ﾟ，_ゝ｀)",
    "( ╥ω╥ )",
    "(／ˍ・、)",
    "(つω`｡)",
    "(T_T)",
    "o(〒﹏〒)o",
    "(＃`Д´)",
    "(・`ω´・)",
    "( `ε´ )",
    "(ﾒ` ﾛ ´)",
    "Σ(▼□▼メ)",
    "(҂ `з´ )",
    "٩(╬ʘ益ʘ╬)۶",
    "↑_(ΦwΦ)Ψ",
    "(ﾉಥ益ಥ)ﾉ",
    "(＃＞＜)",
    "(；￣Д￣)",
    "(￢_￢;)",
    "(＾＾＃)",
    "(￣︿￣)",
    "ヾ( ￣O￣)ツ",
    "(ᗒᗣᗕ)՞",
    "(ノ_<。)ヾ(´ ▽ ` )",
    "ヽ(￣ω￣(。。 )ゝ",
    "(ﾉ_；)ヾ(´ ∀ ` )",
    "(´-ω-`( _ _ )",
    "(⌒_⌒;)",
    "(*/_＼)",
    "( ◡‿◡ *)",
    "(//ω//)",
    "(￣▽￣*)ゞ",
    "(„ಡωಡ„)",
    "(ﾉ´ з `)ノ",
    "(♡-_-♡)",
    "(─‿‿─)♡",
    "(´ ω `♡)",
    "(ღ˘⌣˘ღ)",
    "(´• ω •`) ♡",
    "╰(*´︶`*)╯♡",
    "(≧◡≦) ♡",
    "♡ (˘▽˘>ԅ( ˘⌣˘)",
    "σ(≧ε≦σ) ♡",
    "(˘∀˘)/(μ‿μ) ❤",
    "Σ>―(〃°ω°〃)♡→",
    "(* ^ ω ^)",
    "(o^▽^o)",
    "ヽ(・∀・)ﾉ",
    "(o･ω･o)",
    "(^人^)",
    "( ´ ω ` )",
    "(´• ω •`)",
    "╰(▔∀▔)╯",
    "(✯◡✯)",
    "(⌒‿⌒)",
    "(*°▽°*)",
    "(´｡• ᵕ •｡`)",
    "ヽ(>∀<☆)ノ",
    "＼(￣▽￣)／",
    "(o˘◡˘o)",
    "(╯✧▽✧)╯",
    "( ‾́ ◡ ‾́ )",
    "(๑˘︶˘๑)",
    "(´･ᴗ･ ` )",
    "( ͡° ʖ̯ ͡°)",
    "( ఠ ͟ʖ ఠ)",
    "( ಥ ʖ̯ ಥ)",
    "(≖ ͜ʖ≖)",
    "ヘ(￣ω￣ヘ)",
    "(ﾉ≧∀≦)ﾉ",
    "└(￣-￣└))",
    "┌(＾＾)┘",
    "(^_^♪)",
    "(〜￣△￣)〜",
    "(｢• ω •)｢",
    "( ˘ ɜ˘) ♬♪♫",
    "( o˘◡˘o) ┌iii┐",
    "♨o(>_<)o♨",
    "( ・・)つ―{}@{}@{}-",
    "(*´з`)口ﾟ｡ﾟ口(・∀・ )",
    "( *^^)o∀*∀o(^^* )",
    "-●●●-ｃ(・・ )",
    "(ﾉ≧∀≦)ﾉ ‥…━━━★",
    "╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ",
    "(∩ᄑ_ᄑ)⊃━☆ﾟ*･｡*･:≡( ε:)",
]


def react(update: Update, context: CallbackContext):
    message = update.effective_message
    react = random.choice(reactions)
    if message.reply_to_message:
        message.reply_to_message.reply_text(react)
    else:
        message.reply_text(react)
        
def natures(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Nature are a mechanic that influences how a Pokémon stats grow.\nNature effect is limited to only 10%.\nHere are the list of commands\n\n/hardy - About hardy natured pokemon.\n/lonely - About lonely natured pokemon.\n/brave - About brave natured pokemon.\n/adamant - About adamant natured pokemon.\n/naughty - About naughty natured pokemon.\n/bold - About bold natured pokemon.\n/docile - About docile natured pokemon.\n/relaxed - About relaxed natured pokemon.\n/impish - About impish natured pokemon.\n/lax - About lax natured pokemon.\n/modest - About modest natured pokemon.\n/mild - About mild natured pokemon.\n/serious - About serious natured pokemon.\n/quiet - About quiet natured pokemon.\n/rash - About rash natured pokemon.\n/calm - About calm natured pokemon.\n/gentle - About gentle natured pokemon.\n/sassy - About sassy natured pokemon.\n/bashful - About bashful natured pokemon.\n/careful - About careful natured pokemon.\n/timid - About timid natured pokemon.\n/hasty - About hasty natured pokemon.\n/jolly - About jolly natured pokemon.\n/naive - About naive natured pokemon.\n/quirky - About quirky natured pokemon",
    )


REACT_HANDLER = DisableAbleCommandHandler("react", react, run_async=True)
NATURES_HANDLER = DisableAbleCommandHandler("natures", natures, run_async=True)

dispatcher.add_handler(REACT_HANDLER)
dispatcher.add_handler(NATURES_HANDLER)

__command_list__ = ["react"]
__handlers__ = [REACT_HANDLER]

__mod_name__ = "Reactions"
__help__ = """
--> `/react` : To react to a message.
"""
