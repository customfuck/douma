from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from Shikimori import pbot


@pbot.on_message(filters.command(["generation", "generations"]))
async def photo(client: pbot, message: Message):
    user_id = message.from_user.id
    client.send_message(
        chat_id=message.chat.id,
        text="SELECT FROM THE GENERATION U WANT TO SEE",
        reply_markup=InlineKeyboardMarkup(
           [
                    [
                        InlineKeyboardButton(text="GEN1", callback_data="gen1"),
                        InlineKeyboardButton(text="GEN2", callback_data="gen2"),
                        InlineKeyboardButton(text="GEN3", callback_data="gen3")
                    ],
                    [
                        InlineKeyboardButton(text="GEN4", callback_data="gen4"),
                        InlineKeyboardButton(text="GEN5", callback_data="gen5"),
                        InlineKeyboardButton(text="GEN6", callback_data="gen6")
                    ],
                    [
                        InlineKeyboardButton(text="GEN7", callback_data="gen7"),
                    ]
                ]
            ),
            reply_to_message_id=message.reply_to_message_id,
        )
    
@pbot.on_callback_query()
async def cb_handler(client: pbot, query: CallbackQuery):
        if query.data == "gen1":
            await query.message.edit_text(
                "HERE ARE THE LIST OF GENERATION 1 POKEMONS\n\n`🌟Bulbasaur |🌟Ivysaur`*\n`🌟Venusaur  |🌟Charmander`*\n`🌟Charmeleon|🌟Charizard`\n`🌟Squirtle  |🌟Wartortle`\n`🌟Blastoise |🌟Caterpie`\n`🌟Metapod   |🌟Butterfree`\n`🌟Weedle    |🌟Kakuna`\n`🌟Beedrill  |🌟Pidgey`\n`🌟Pidgeotto |🌟Pidgeot`\n`🌟Rattata   |🌟Raticate`\n`🌟Spearow   |🌟Fearow`\n`🌟Ekans     |🌟Arbok `\n`🌟Pikachu   |🌟Raichu`\n`🌟Sandshrew |🌟Sandslash`\n`🌟Nidoran♀  |🌟Nidorina`\n`🌟Nidoqueen |🌟Nidoran♂`\n`🌟Nidorino  |🌟Nidoking`\n`🌟Clefairy  |🌟Clefable`\n`🌟Vulpix    |🌟Ninetales`\n`🌟Jigglypuff|🌟Wigglytuff `\n`🌟Zubat     |🌟Golbat`\n`🌟Oddish    |🌟Gloom`\n`🌟Vileplume |🌟Paras`\n`🌟Parasect  |🌟Venonat`\n`🌟Venomoth  |🌟Diglett`\n`🌟Dugtrio   |🌟Meowth`\n`🌟Persian   |🌟Psyduck`\n`🌟Golduck   |🌟Mankey`\n`🌟Primeape  |🌟Growlithe`\n`🌟Arcanine  |🌟Poliwag`\n`🌟Poliwhirl |🌟Poliwrath`\n`🌟Abra      |🌟Kadabra`\n`🌟Alakazam  |🌟Machop`\n`🌟Machamp   |🌟Machoke`\n`🌟Farfetch'd|🌟Bellsprout`\n`🌟Weepinbell|🌟Victreebel`\n`🌟Tentacool |🌟Tentacruel`\n`🌟Geodude   |🌟Graveler`\n`🌟Golem     |🌟Ponyta`\n`🌟Rapidash  |🌟Slowpoke`\n`🌟Slowbro   |🌟Magnemite`\n`🌟Magneton  |🌟Doduo`\n`🌟Dodrio    |🌟Seel`\n`🌟Dewgong   |🌟Grimer`\n`🌟Muk       |🌟Shellder`\n`🌟Cloyster  |🌟Gastly`\n`🌟Haunter   |🌟Gengar`\n`🌟Onix      |🌟Drowzee`\n`🌟Hypno     |🌟Krabby`\n`🌟Kingler   |🌟Voltorb`\n`🌟Electrode |🌟Exeggcute`\n`🌟Exeggutor |🌟Cubone`\n`🌟Marowak   |🌟Hitmonlee`\n`🌟Hitmonchan|🌟Lickitung`\n`🌟Koffing   |🌟Weezing`\n`🌟Rhyhorn   |🌟Rhydon`\n`🌟Chansey   |🌟Tangela`\n`🌟Kangaskhan|🌟Horsea`\n`🌟Seadra    |🌟Goldeen`\n`🌟Seaking   |🌟Staryu`\n`🌟Starmie   |🌟Mr.Mime`\n`🌟Scyther   |🌟Jynx`\n`🌟Electabuzz|🌟Magmar`\n`🌟Pinsir    |🌟Tauros`\n`🌟Magikarp  |🌟Gyarados`\n`🌟Lapras    |🌟Ditto`\n`🌟Eevee     |🌟Vaporeon`\n`🌟Jolteon   |🌟Flareon`\n`🌟Porygon   |🌟Omanyte`\n`🌟Omastar   |🌟Kabuto`\n`🌟Kabutops  |🌟Aerodactyl`\n`🌟Snorlax   |🌟Articuno`\n`🌟Zapdos    |🌟Moltres`\n`🌟Dratini   |🌟Dragonair`\n`🌟Dragonite |🌟Mewtwo`\n`🌟Mewㅤㅤㅤㅤ",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="GEN2", callback_data="gen2"
                            ),
                            InlineKeyboardButton(
                                text="GEN3", callback_data="gen3"
                            ),
                            InlineKeyboardButton(
                                text="GEN4", callback_data="gen4"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                text="GEN5", callback_data="gen5"
                            ),
                            InlineKeyboardButton(
                                text="GEN6", callback_data="gen6"
                            ),
                            InlineKeyboardButton(
                                text="GEN7", callback_data="gen7"
                            )
                        ]
                    ]
                ),
            )
        elif query.data == "gen2":
            await query.message.edit(
                "HERE ARE THE LIST OF GENERATION 2 POKEMONS\n\n🌟 Chikorita\n🌟 Bayleef\n🌟 Meganium\n🌟 Cyndaquil\n🌟 Quilava\n🌟 Typhlosion\n🌟 Totodile\n🌟 Croconaw\n🌟 Feraligatr\n🌟 Sentret\n🌟 Furret\n🌟 Hoothoot\n🌟 Noctowl\n🌟 Ledyba\n🌟 Ledian\n🌟 Spinarak\n🌟 Ariados\n🌟 Crobat\n🌟 Chinchou\n🌟 Lanturn\n🌟 Pichu\n🌟 Cleffa\n🌟 Igglybuff\n🌟 Togepi\n🌟 Togetic\n🌟 Natu\n🌟 Xatu\n🌟 Mareep\n🌟 Flaaffy\n🌟 Ampharos\n🌟 Bellossom\n🌟 Marill\n🌟 Azumarill\n🌟 Sudowoodo\n🌟 Politoed\n🌟 Hoppip\n🌟 Skiploom\n🌟 Jumpluff\n🌟 Aipom\n🌟 Sunkern\n🌟 Sunflora\n🌟 Yanma\n🌟 Wooper\n🌟 Quagsire\n🌟 Espeon\n🌟 Umbreon\n🌟 Murkrow\n🌟 Slowking\n🌟 Misdreavus\n🌟 Unown\n🌟 Wobbuffet\n🌟 Girafarig\n🌟 Pineco\n🌟 Forretress\n🌟 Dunsparce\n🌟 Gligar\n🌟 Steelix\n🌟 Snubbull\n🌟 Granbull\n🌟 Qwilfish\n🌟 Scizor\n🌟 Shuckle\n🌟 Heracross\n🌟 Sneasel\n🌟 Teddiursa\n🌟 Ursaring\n🌟 Slugma\n🌟 Magcargo\n🌟 Swinub\n🌟 Piloswine\n🌟 Corsola\n🌟 Remoraid\n🌟 Octillery\n🌟 Delibird\n🌟 Mantine\n🌟 Skarmory\n🌟 Houndour\n🌟 Houndoom\n🌟 Kingdra\n🌟 Phanpy\n🌟 Donphan\n🌟 Porygon2\n🌟 Stantler\n🌟 Smeargle\n🌟 Tyrogue\n🌟 Hitmontop\n🌟 Smoochum\n🌟 Elekid\n🌟 Magby\n🌟 Miltank\n🌟 Blissey\n🌟 Raikou\n🌟 Entei\n🌟 Suicune\n🌟 Larvitar\n🌟 Pupitar\n🌟 Tyranitar\n🌟 Lugia\n🌟 Ho-Oh\n🌟 Celebi",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="GEN1", callback_data="gen1"),
                            InlineKeyboardButton(
                                text="GEN3", callback_data="gen3"
                            ),
                            InlineKeyboardButton(
                                text="GEN4", callback_data="gen4"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                text="GEN5", callback_data="gen5"
                            ),
                            InlineKeyboardButton(
                                text="GEN6", callback_data="gen6"
                            ),
                            InlineKeyboardButton(
                                text="GEN7", callback_data="gen7"
                            )
                        ]
                    ]
                ),
            )
        elif query.data == "gen3":
            await query.message.edit(
                "HERE ARE THE LIST OF GENERATION 3 POKEMONS\n\n🌟 Treecko\n🌟 Grovyle\n🌟 Sceptile\n🌟 Torchic\n🌟 Combusken\n🌟 Blaziken\n🌟 Mudkip\n🌟 Marshtomp\n🌟 Swampert\n🌟 Poochyena\n🌟 Mightyena\n🌟 Zigzagoon\n🌟 Linoone\n🌟 Wurmple\n🌟 Silcoon\n🌟 Beautifly\n🌟 Cascoon\n🌟 Dustox\n🌟 Lotad\n🌟 Lombre\n🌟 Ludicolo\n🌟 Seedot\n🌟 Nuzleaf\n🌟 Shiftry\n🌟 Taillow\n🌟 Swellow\n🌟 Wingull\n🌟 Pelipper\n🌟 Ralts\n🌟 Kirlia\n🌟 Gardevoir\n🌟 Surskit\n🌟 Masquerain\n🌟 Shroomish\n🌟 Breloom\n🌟 Slakoth\n🌟 Vigoroth\n🌟 Slaking\n🌟 Nincada\n🌟 Ninjask\n🌟 Shedinja\n🌟 Whismur\n🌟 Loudred\n🌟 Exploud\n🌟 Makuhita\n🌟 Hariyama\n🌟 Azurill\n🌟 Nosepass\n🌟 Skitty\n🌟 Delcatty\n🌟 Sableye\n🌟 Mawile\n🌟 Aron\n🌟 Lairon\n🌟 Aggron\n🌟 Meditite\n🌟 Medicham\n🌟 Electrike\n🌟 Manectric\n🌟 Plusle\n🌟 Minun\n🌟 Volbeat\n🌟 Illumise\n🌟 Roselia\n🌟 Gulpin\n🌟 Swalot\n🌟 Carvanha\n🌟 Sharpedo\n🌟 Wailmer\n🌟 Wailord\n🌟 Numel\n🌟 Camerupt\n🌟 Torkoal\n🌟 Spoink\n🌟 Grumpig\n🌟 Spinda\n🌟 Trapinch\n🌟 Vibrava\n🌟 Flygon\n🌟 Cacnea\n🌟 Cacturne\n🌟 Swablu\n🌟 Altaria\n🌟 Zangoose\n🌟 Seviper\n🌟 Lunatone\n🌟 Solrock\n🌟 Barboach\n🌟 Whiscash\n🌟 Corphish\n🌟 Crawdaught\n🌟 Baltoy\n🌟 Claydol\n🌟 Lileep\n🌟 Cradily\n🌟 Anorith\n🌟 Armaldo\n🌟 Feebas\n🌟 Milotic\n🌟 Castform\n🌟 Kecleon\n🌟 Shuppet\n🌟 Banette\n🌟 Duskull\n🌟 Dusclops\n🌟 Tropius\n🌟 Chimecho\n🌟 Absol\n🌟 Wynaut\n🌟 Snorunt\n🌟 Glalie\n🌟 Spheal\n🌟 Sealeo\n🌟 Walrein\n🌟 Clamperl\n🌟 Huntail\n🌟 Gorebyss\n🌟 Relicanth\n🌟 Luvdisc\n🌟 Bagon\n🌟 Shelgon\n🌟 Salamence\n🌟 Beldum\n🌟 Metang\n🌟 Metagross\n🌟 Regirock\n🌟 Regice\n🌟 Registeel\n🌟 Latias\n🌟 Latios\n🌟 Kyogre\n🌟 Groudon\n🌟 Rayquaza\n🌟 Jirachu\n🌟 Deoxys ",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="GEN1", callback_data="gen1"),
                            InlineKeyboardButton(
                                text="GEN2", callback_data="gen2"
                            ),
                            InlineKeyboardButton(
                                text="GEN4", callback_data="gen4"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                text="GEN5", callback_data="gen5"
                            ),
                            InlineKeyboardButton(
                                text="GEN6", callback_data="gen6"
                            ),
                            InlineKeyboardButton(
                                text="GEN7", callback_data="gen7"
                            )
                        ]
                    ]
                ),
            ) 
        elif query.data == "gen4":
            await query.message.edit(
                "HERE ARE THE LIST OF GENERATION 4 POKEMONS\n\n🌟 Turtwig\n🌟 Grotle\n🌟 Torterra\n🌟 Chimchar\n🌟 Monferno\n🌟 Infernape\n🌟 Piplup\n🌟 Prinplup\n🌟 Empoleon\n🌟 Starly\n🌟 Staravia\n🌟 Staraptor\n🌟 Bidoof\n🌟 Bibarel\n🌟 Kricketot\n🌟 Kricketune\n🌟 Shinx\n🌟 Luxio\n🌟 Luxray\n🌟 Budew\n🌟 Roserade\n🌟 Cranidos\n🌟 Rampardos\n🌟 Shieldon\n🌟 Bastiodon\n🌟 Burmy\n🌟 Wormadam\n🌟 Mothim\n🌟 Combee\n🌟 Vespiquen\n🌟 Pachirisu\n🌟 Buizel\n🌟 Floatzel\n🌟 Cherubi\n🌟 Cherrim\n🌟 Shellos\n🌟 Gastrodon\n🌟 Ambipom\n🌟 Drifloon\n🌟 Drifblim\n🌟 Buneary\n🌟 Lopunny\n🌟 Mismagius\n🌟 Honchkrow\n🌟 Glameow\n🌟 Purugly\n🌟 Chingling\n🌟 Stunky\n🌟 Skuntank\n🌟 Bronzor\n🌟 Bronzong\n🌟 Bonsly\n🌟 MimeJr.\n🌟 Happiny\n🌟 Chatot\n🌟 Spiritomb\n🌟 Gible\n🌟 Gabite\n🌟 Garchomp\n🌟 Munchlax\n🌟 Riolu\n🌟 Lucario\n🌟 Hippopotas\n🌟 Hippowdon\n🌟 Skorupi\n🌟 Drapion\n🌟 Croagunk\n🌟 Toxicroak\n🌟 Carnivine\n🌟 Finneon\n🌟 Lumineon\n🌟 Mantyke\n🌟 Snover\n🌟 Abomasnow\n🌟 Weavile\n🌟 Magnezone\n🌟 Lickilicky\n🌟 Rhyperior\n🌟 Tangrowth\n🌟 Electivire\n🌟 Magmortar\n🌟 Togekiss\n🌟 Yanmega\n🌟 Leafeon\n🌟 Glaceon\n🌟 Gliscor\n🌟 Mamoswine\n🌟 Porygon-Z\n🌟 Gallade\n🌟 Probopass\n🌟 Dusknoir\n🌟 Froslass\n🌟 Rotom\n🌟 Uxie\n🌟 Mesprit\n🌟 Azelf\n🌟 Dialga\n🌟 Palkia\n🌟 Heatran\n🌟 Regigigas\n🌟 Giratina\n🌟 Cresselia\n🌟 Phione\n🌟 Manaphy\n🌟 Darkrai\n🌟 Shaymin\n🌟 Arceus",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="GEN1", callback_data="gen1"),
                            InlineKeyboardButton(
                                text="GEN2", callback_data="gen2"
                            ),
                            InlineKeyboardButton(
                                text="GEN3", callback_data="gen3"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                text="GEN5", callback_data="gen5"
                            ),
                            InlineKeyboardButton(
                                text="GEN6", callback_data="gen6"
                            ),
                            InlineKeyboardButton(
                                text="GEN7", callback_data="gen7"
                            )
                        ]
                    ]
                ),
            )
        elif query.data == "gen5":
            await query.message.edit(
                "HERE ARE THE LIST OF GENERATION 5 POKEMONS\n\n🌟Victini\n🌟 Snivy\n🌟 Servine\n🌟 Serperior\n🌟 Tepig\n🌟 Pignite\n🌟 Emboar\n🌟 Oshawott\n🌟 Dewott\n🌟 Samurott\n🌟 Patrat\n🌟 Watchog\n🌟 Lillipup\n🌟 Herdier\n🌟 Stoutland\n🌟 Purrloin\n🌟 Liepard\n🌟 Pansage\n🌟 Simisage\n🌟 Pansear\n🌟 Simisear\n🌟 Panpour\n🌟 Simipour\n🌟 Munna\n🌟 Musharna\n🌟 Pidove\n🌟 Tranquill\n🌟 Unfezant\n🌟 Blitzle\n🌟 Zebstrika\n🌟 Roggenrola\n🌟 Boldore\n🌟 Gigalith\n🌟 Woobat\n🌟 Swoobat\n🌟 Drilbur\n🌟 Excadrill\n🌟 Audino\n🌟 Timburr\n🌟 Gurdurr\n🌟 Conkeldurr\n🌟 Tympole\n🌟 Palpitoad\n🌟 Seismitoad\n🌟 Throh\n🌟 Sawk\n🌟 Sewaddle\n🌟 Swadloon\n🌟 Leavanny\n🌟 Venipede\n🌟 Whirlipede\n🌟 Scolipede\n🌟 Cottonee\n🌟 Whimsicott\n🌟 Petilil\n🌟 Lilligant\n🌟 Basculin\n🌟 Sandile\n🌟 Krokorok\n🌟 Krookodile\n🌟 Darumaka\n🌟 Darmanitan\n🌟 Maractus\n🌟 Dwebble\n🌟 Crustle\n🌟 Scraggy\n🌟 Scrafty\n🌟 Sigilyph\n🌟 Yamask\n🌟 Cofagrigus\n🌟 Tirtouga\n🌟 Carracosta\n🌟 Archen\n🌟 Archeops\n🌟 Trubbish\n🌟 Garbodor\n🌟 Zorua\n🌟 Zoroark\n🌟 Minccino\n🌟 Cinccino\n🌟 Gothita\n🌟 Gothorita\n🌟 Gothitelle\n🌟 Solosis\n🌟 Duosion\n🌟 Reuniclus\n🌟 Ducklett\n🌟 Swanna\n🌟 Vanillite\n🌟 Vanillish\n🌟 Vanilluxe\n🌟 Deerling\n🌟 Sawsbuck\n🌟 Emolga\n🌟 Karrablast\n🌟 Escavalier\n🌟 Foongus\n🌟 Amoonguss\n🌟 Frillish\n🌟 Jellicent\n🌟 Alomomola\n🌟 Joltik\n🌟 Galvantula\n🌟 Ferroseed\n🌟 Ferrothorn\n🌟 Klink\n🌟 Klang\n🌟 Klinklang\n🌟 Tynamo\n🌟 Eelektrik\n🌟 Eelektross\n🌟 Elgyem\n🌟 Beheeyem\n🌟 Litwick\n🌟 Lampent\n🌟 Chandelure\n🌟 Axew\n🌟 Fraxure\n🌟 Haxorus\n🌟 Cubchoo\n🌟 Beartic\n🌟 Cryogonal\n🌟 Shelmet\n🌟 Accelgor\n🌟 Stunfisk\n🌟 Mienfoo\n🌟 Mienshao\n🌟 Druddigon\n🌟 Golett\n🌟 Golurk\n🌟 Pawniard\n🌟 Bisharp\n🌟 Bouffalant\n🌟 Rufflet\n🌟 Braviary\n🌟 Vullaby\n🌟 Mandibuzz\n🌟 Heatmor\n🌟 Durant\n🌟 Deino\n🌟 Zweilous\n🌟 Hydreigon\n🌟 Larvesta\n🌟 Volcarona\n🌟 Cobalion\n🌟 Terrakion\n🌟 Virizion\n🌟 Tornadus\n🌟 Thundurus\n🌟 Reshiram\n🌟 Zekrom\n🌟 Landorus\n🌟 Kyurem\n🌟 Keldeo\n🌟 Meloetta\n🌟 Genesect",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="GEN1", callback_data="gen1"),
                            InlineKeyboardButton(
                                text="GEN2", callback_data="gen2"
                            ),
                            InlineKeyboardButton(
                                text="GEN3", callback_data="gen3"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                text="GEN4", callback_data="gen4"
                            ),
                            InlineKeyboardButton(
                                text="GEN6", callback_data="gen6"
                            ),
                            InlineKeyboardButton(
                                text="GEN7", callback_data="gen7"
                            )
                        ]
                    ]
                ),
            )
        elif query.data == "gen6":
            await query.message.edit(
                "**HERE ARE THE LIST OF GENERATION 6 POKEMONS\n\n🌟Chespin\n🌟 Quilladin\n🌟 Chesnaught\n🌟 Fennekin\n🌟 Braixen\n🌟 Delphox\n🌟 Froakie\n🌟 Frogadier\n🌟 Greninja\n🌟 Bunnelby\n🌟 Diggersby\n🌟 Fletchling\n🌟 Fletchinder\n🌟 Talonflame\n🌟 Scatterbug\n🌟 Spewpa\n🌟 Vivillon\n🌟 Litleo\n🌟 Pyroar\n🌟 Flabébé\n🌟 Floette\n🌟 Florges\n🌟 Skiddo\n🌟 Gogoat\n🌟 Pancham\n🌟 Pangoro\n🌟 Furfrou\n🌟 Espurr\n🌟 Meowstic\n🌟 Honedge\n🌟 Doublade\n🌟 Aegislash\n🌟 Spritzee\n🌟 Aromatisse\n🌟 Swirlix\n🌟 Slurpuff\n🌟 Inkay\n🌟 Malamar\n🌟 Binacle\n🌟 Barbaracle\n🌟 Skrelp\n🌟 Dragalge\n🌟 Clauncher\n🌟 Clawitzer\n🌟 Helioptile\n🌟 Heliolisk\n🌟 Tyrunt\n🌟 Tyrantrum\n🌟 Amaura\n🌟 Aurorus\n🌟 Sylveon\n🌟 Hawlucha\n🌟 Dedenne\n🌟 Carbink\n🌟 Goomy\n🌟 Sliggoo\n🌟 Goodra\n🌟 Klefki\n🌟 Phantump\n🌟 Trevenant\n🌟 Pumpkaboo\n🌟 Gourgeist\n🌟 Bergmite\n🌟 Avalugg\n🌟 Noibat\n🌟 Noivern\n🌟 Xerneas\n🌟 Yveltal\n🌟 Zygarde\n🌟 Diancie\n🌟 Hoopa\n🌟 Volcanion",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="GEN1", callback_data="gen1"),
                            InlineKeyboardButton(
                                text="GEN2", callback_data="gen2"
                            ),
                            InlineKeyboardButton(
                                text="GEN3", callback_data="gen3"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                text="GEN4", callback_data="gen4"
                            ),
                            InlineKeyboardButton(
                                text="GEN5", callback_data="gen5"
                            ),
                            InlineKeyboardButton(
                                text="GEN7", callback_data="gen7"
                            )
                        ]
                    ]
                ),
            )
        elif query.data == "gen7":
            await query.message.edit(
                "HERE ARE THE LIST OF GENERATION 7 POKEMONS\n\n🌟 Alolan Rattata\n🌟 Alolan Raticate\n🌟 Alolan Raichu\n🌟 Alolan Sandshrew\n🌟 Alolan Sandslash\n🌟 Alolan Vulpix\n🌟 Alolan Ninetales\n🌟 Alolan Diglett\n🌟 Alolan Dugtrio\n🌟 Alolan Meowth\n🌟 Alolan Persian\n🌟 Alolan Geodude\n🌟 Alolan Graveler\n🌟 Alolan Golem\n🌟 Alolan Grimer\n🌟 Alolan Muk\n🌟 Alolan Exeggutor\n🌟 Alolan Marowak\n🌟 Rowlet\n🌟 Dartrix\n🌟 Decidueye\n🌟 Litten\n🌟 Torracat\n🌟 Incineroar\n🌟 Popplio\n🌟 Brionne\n🌟 Primarina\n🌟 Pikipek\n🌟 Trumbeak\n🌟 Toucannon\n🌟 Yungoos\n🌟 Gumshoos\n🌟 Grubbin\n🌟 Charjabug\n🌟 Vikavolt\n🌟 Crabrawler\n🌟 Crabominable\n🌟 Oricorio\n🌟 Cutiefly\n🌟 Ribombee\n🌟 Rockruff\n🌟 Lycanroc\n🌟 Wishiwashi\n🌟 Mareanie\n🌟 Toxapex\n🌟 Mudbray\n🌟 Mudsdale\n🌟 Dewpider\n🌟 Araquanid\n🌟 Fomantis\n🌟 Lurantis\n🌟 Morelull\n🌟 Shiinotic\n🌟 Salandit\n🌟 Salazzle\n🌟 Stufful\n🌟 Bewear\n🌟 Bounsweet\n🌟 Steenee\n🌟 Tsareena\n🌟 Comfey\n🌟 Oranguru\n🌟 Passimian\n🌟 Wimpod\n🌟 Golisopod\n🌟 Sandygast\n🌟 Palossand\n🌟 Pyukumuku\n🌟 Type:Null\n🌟 Silvally\n🌟 Minior\n🌟 Komala\n🌟 Turtonator\n🌟 Togedemaru\n🌟 Mimikyu\n🌟 Bruxish\n🌟 Drampa\n🌟 Dhelmise\n🌟 Jangmo-o\n🌟 Hakamo-o\n🌟 Kommo-o\n🌟 Tapu-Koko\n🌟 Tapu-Lele\n🌟 Tapu-Bulu\n🌟 Tapu-Fini\n🌟 Cosmog\n🌟 Cosmoem\n🌟 Solgaleo\n🌟 Lunala\n🌟 Nihilego\n🌟 Buzzwole\n🌟 Pheromosa\n🌟 Xurkitree\n🌟 Celesteela\n🌟 Kartana\n🌟 Guzzlord\n🌟 Necrozma\n🌟 Magearna\n🌟 Marshadow\n🌟 Poipole\n🌟 Naganadel\n🌟 Stakataka\n🌟 Blacephalon\n🌟 Zeraora\n🌟 Meltan\n🌟 Melmetal",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="GEN1", callback_data="gen1"),
                            InlineKeyboardButton(
                                text="GEN2", callback_data="gen2"
                            ),
                            InlineKeyboardButton(
                                text="GEN3", callback_data="gen3"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                text="GEN4", callback_data="gen4"
                            ),
                            InlineKeyboardButton(
                                text="GEN5", callback_data="gen5"
                            ),
                            InlineKeyboardButton(
                                text="GEN6", callback_data="gen6"
                            )
                        ]
                    ]
                ),
            )
            

__mod_name__ = "Generation"

__help__ = """
❍ `/edit` : To edit the image.
❍ `/editor` : To edit the imiage.
Note: Remove BG doesn't work, dev will fix it later.
"""
