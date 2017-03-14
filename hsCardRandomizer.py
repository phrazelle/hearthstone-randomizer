# *******************************************************
# Hearthstone Card Randomizer v0.8
# by Robbie Frazelle 2016
#
# ** This code was written for a Raspberry Pi B+ with an
#    Adafruit 16x2 Negative LCD + Keypad Shield, and was
#    created as a companion to a hardcopy Hearthstone
#    set. This program includes all cards through the
#    League of Explorers set.
#
#    The menu structure is laid out as follows:
#    
#    Minions
#      - Summon a Random Minion
#      - Beasts Menu
#      	* Summon a Random Beast
#      	* Summon a Random Beast Companion
#      - Summon a Random Deathrattle Minion
#      - Summon a Random Demon
#      - Summon a Random Legendary Minion
#      - Mechs Menu
#      	* Summon a Random Mech
#      	* Enchance-O Mechano Effect
#      - Summon a Random Murloc
#      - Totems Menu
#      	* Hero Power Totem Summon
#      	* Summon a Random Totem
#      - X-Cost Minion Menu
#      	* Summon a 0 Cost Minion
#      	* Summon a 1 Cost Minion
#      	* Summon a 2 Cost Minion
#      	* Summon a 3 Cost Minion
#      	* Summon a 4 Cost Minion
#      	* Summon a 5 Cost Minion
#      	* Summon a 6 Cost Minion
#      	* Summon a 7 Cost Minion
#      	* Summon a 8 Cost Minion
#      	* Summon a 9 Cost Minion
#      	* Summon a 10 Cost Minion
#    
#    Spells
#      - Summon a Random Spell
#      - Summon a Spell by Class
#      	* Summon a Random Druid Spell
#      	* Summon a Random Hunter Spell
#      	* Summon a Random Mage Spell
#      	* Summon a Random Paladin Spell
#      	* Summon a Random Priest Spell
#      	* Summon a Random Rogue Spell
#      	* Summon a Random Shaman Spell
#      	* Summon a Random Warlock Spell
#      	* Summon a Random Warrior Spell
#    
#    Class Cards
#      - Select a Random Druid Card
#      - Select a Random Hunter Card
#      - Select a Random Mage Card
#      - Select a Random Paladin Card
#      - Select a Random Priest Card
#      - Select a Random Rogue Card
#      - Select a Random Shaman Card
#      - Select a Random Warlock Card
#      - Select a Random Warrior Card
#    
#    Weapons
#      - Select a Random Weapon
#      - Select a Weapon by ATK/DUR
#        * Select a 1/3 Weapon
#        * Select a 2/2 Weapon
#    
#    X-Cost Cards
#      - Select a 1 Cost Card
#      - Select a 3 Cost Card
#    
#    Other
#      - Select a Random Hero Power
#      - Select a Random Spare Part
#      - Select a Random Invention
#      - Select a Random Power Chord Card
#    
# *******************************************************

# *******************************************************
# import modules
# *******************************************************

import Adafruit_CharLCD as LCD
import random
import time

# *******************************************************
# Initialize the LCD using the pins
# *******************************************************

lcd = LCD.Adafruit_CharLCDPlate()

# *******************************************************
# RPi pin configuration
# *******************************************************

lcd_rs        = 27
lcd_en        = 22
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 4

# *******************************************************
# Display initial text on LCD
# *******************************************************

lcd.message('Hearthstone    ∧\nRandomizer     ∨')

# *******************************************************
# Define arrays
# *******************************************************

oneCostCard = ["Abusive Sergeant","Angry Chicken","Arcane Blast","Arcane Missiles","Arcane Shot","Argent Squire","Avenge","Bestial Wrath","Blessing of Might","Blessing of Wisdom","Blood Imp","Bloodsail Corsair","Brave Archer","Buccaneer","Claw","Clockwork Gnome","Cogmaster","Cold Blood","Competitive Spirit","Conceal","Corruption","Cursed Blade","Deadly Poison","Dragon Egg","Dust Devil","Earth Shock","Elven Archer","Execute","Eye for an Eye","Flame Imp","Flash Heal","Forked Lightning","Frost Shock","Gadgetzan Jouster","Goldshire Footman","Grimscale Oracle","Hand of Protection","Holy Smite","Humility","Hungry Crab","Hunter's Mark","Ice Lance","Injured Kvaldir","Inner Fire","Leper Gnome","Light of the Naaru","Light's Justice","Lightning Bolt","Lightwarden","Living Roots","Lowly Squire","Mana Wyrm","Mind Vision","Mirror Image","Mortal Coil","Murloc Raider","Murloc Tidecaller","Naturalize","Noble Sacrifice","Northshire Cleric","Pit Snake","Power Overwhelming","Power Word: Glory","Power Word: Shield","Raven Idol","Redemption","Reliquary Seeker","Repentance","Rockbiter Weapon","Sacred Trial","Savagery","Secretkeeper","Shadowbomber","Shield Slam","Shieldbearer","Sinister Strike","Sir Finley Mrrgglton","Soulfire","Southsea Deckhand","Stonetusk Boar","Timber Wolf","Tournament Attendee","Tracking","Tunnel Trogg","Twilight Whelp","Undertaker","Upgrade!","Voidwalker","Voodoo Doctor","Warbot","Webspinner","Whirlwind","Worgen Infiltrator","Young Dragonhawk","Young Priestess","Zombie Chow"]
threeCostCard = ["Acolyte of Pain","Alarm-o-Bot","Aldor Peacekeeper","Animal Companion","Arcane Golem","Arcane Intellect","Argent Horserider","Bash","Beneath the Grounds","Blackwing Technician","Blood Knight","Bouncing Blade","Brann Bronzebeard","Burgle","Charge","Coghammer","Cogmaster's Wrench","Coldlight Oracle","Coldlight Seer","Coliseum Manager","Counterspell","Dalaran Mage","Dancing Swords","Dark Cultist","Deadly Shot","Deathlord","Demolisher","Demonwrath","Desert Camel","Divine Favor","Dragonhawk Rider","Drain Life","Dreadscale","Druid of the Flame","Duplicate","Eaglehorn Bow","Earthen Ring Farseer","Edwin VanCleef","Effigy","Elemental Destruction","Emperor Cobra","Eydis Darkbane","Fan of Knives","Far Sight","Felguard","Fencing Coach","Feral Spirit","Fierce Monkey","Fjola Lightbane","Flamewaker","Flesheating Ghoul","Flying Machine","Forgotten Torch","Frost Nova","Frothing Berserker","Gnomeregan Infantry","Gnomish Experimenter","Goblin Sapper","Grove Tender","Harvest Golem","Headcrack","Healing Touch","Healing Wave","Hex","Hobgoblin","Ice Barrier","Ice Block","Ice Rager","Illuminator","Imp Gang Boss","Imp Master","Injured Blademaster","Iron Sensei","Ironbeak Owl","Ironforge Rifleman","Ironfur Grizzly","Jungle Panther","Kill Command","King Mukla","King's Defender","Kirin Tor Mage","Lava Burst","Light's Champion","Lightning Storm","Lil' Exorcist","Magma Rager","Mana Tide Totem","Mark of Nature","Master of Ceremonies","Metaltooth Leaper","Mind Control Tech","Mirror Entity","Mounted Raptor","Mulch","Murloc Warleader","Muster for Battle","Ogre Brute","Ogre Warmaul","Orgrimmar Aspirant","Perdition's Blade","Polymorph: Boar","Powermace","Powershot","Questing Adventurer","Raging Worgen","Raid Leader","Razorfen Hunter","Saboteur","Savage Roar","Scarlet Crusader","Scarlet Purifier","Seal of Champions","Sense Demons","Shade of Naxxramas","Shadow Bolt","Shadow Word: Death","Shadowfiend","Shadowform","Shady Dealer","Shattered Sun Cleric","Shield Block","SI:7 Agent","Silent Knight","Silver Hand Regent","Silverback Patriarch","Soot Spewer","Southsea Captain","Spellbender","Spellslinger","Spider Tank","Stablemaster","Stoneskin Gargoyle","Sword of Justice","Tauren Warrior","Thoughtsteal","Thrallmar Farseer","Tinkertown Technician","Tinkmaster Overspark","Tuskarr Totemic","Unbound Elemental","Unearthed Raptor","Unleash the Hounds","Vaporize","Velen's Chosen","Void Terror","Warhorse Trainer","Warsong Commander","Wolfrider"]

heroPowers = ["Hunter","Mage","Warrior","Warlock","Shaman","Paladin","Rogue","Priest","Druid"]

legendaryMinions =["Aviana","Cenarius","Malorne","Acidmaw","Dreadscale","Gahz'rilla","King Krush","Archmage Antonidas","Flame Leviathan","Rhonin","Alexstrasza","Arch-Thief Rafaam","Baron Geddon","Baron Rivendare","Blingtron 3000","Bloodmage Thalnos","Bolf Ramshield","Brann Bronzebeard","Cairne Bloodhoof","Captain Greenskin","Chillmaw","Chromaggus","Deathwing","Dr. Boom","Elise Starseeker","Elite Tauren Chieftain","Emperor Thaurissan","Eydis Darkbane","Feugen","Fjola Lightbane","Foe Reaper 4000","Gazlowe","Gelbin Mekkatorque","Gormok the Impaler","Gruul","Harrison Jones","Hemet Nesingwary","Hogger","Icehowl","Illidan Stormrage","Justicar Trueheart","Kel'Thuzad","King Mukla","Leeroy Jenkins","Loatheb","Lorewalker Cho","Maexxna","Majordomo Executus","Malygos","Mekgineer Thermaplugg","Millhouse Manastorm","Mimiron's Head","Mogor the Ogre","Nat Pagle","Nefarian","Nexus-Champion Saraad","Nozdormu","Old Murk-Eye","Onyxia","Ragnaros the Firelord","Reno Jackson","Sir Finley Mrrgglton","Skycap'n Kragg","Sneed's Old Shredder","Stalagg","Sylvanas Windrunner","The Beast","The Black Knight","The Skeleton Knight","Tinkmaster Overspark","Toshley","Troggzor the Earthinator","Ysera","Bolvar Fordragon","Eadric the Pure","Tirion Fordring","Confessor Paletress","Prophet Velen","Vol'jin","Anub'arak","Edwin VanCleef","Trade Prince Gallywix","Al'Akir the Windlord","Neptulon","The Mistcaller","Lord Jaraxxus","Mal'Ganis","Wilfred Fizzlebang","Grommash Hellscream","Iron Juggernaut","Varian Wrynn"]

allMinions = ["Abomination","Abusive Sergeant","Acidic Swamp Ooze","Acidmaw","Acolyte of Pain","Al'Akir the Windlord","Alarm-o-Bot","Aldor Peacekeeper","Alexstrasza","Alexstrasza's Champion","Amani Berserker","Ancient Brewmaster","Ancient Mage","Ancient of Lore","Ancient of War","Ancient Shade","Ancient Watcher","Angry Chicken","Anima Golem","Animated Armor","Annoy-o-Tron","Anodized Robo Cub","Antique Healbot","Anub'ar Ambusher","Anub'arak","Anubisath Sentinel","Arathi Weaponsmith","Arcane Golem","Arcane Nullifier X-21","Arch-Thief Rafaam","Archmage","Archmage Antonidas","Argent Commander","Argent Horserider","Argent Protector","Argent Squire","Argent Watchman","Armored Warhorse","Armorsmith","Auchenai Soulpriest","Aviana","Axe Flinger","Azure Drake","Baron Geddon","Baron Rivendare","Big Game Hunter","Blackwing Corruptor","Blackwing Technician","Blingtron 3000","Blood Imp","Blood Knight","Bloodfen Raptor","Bloodmage Thalnos","Bloodsail Corsair","Bloodsail Raider","Bluegill Warrior","Bolf Ramshield","Bolvar Fordragon","Bomb Lobber","Boneguard Lieutenant","Booty Bay Bodyguard","Boulderfist Ogre","Brann Bronzebeard","Brave Archer","Buccaneer","Burly Rockjaw Trogg","Cabal Shadow Priest","Cairne Bloodhoof","Captain Greenskin","Captain's Parrot","Captured Jormungar","Cenarius","Chillmaw","Chillwind Yeti","Chromaggus","Clockwork Giant","Clockwork Gnome","Clockwork Knight","Cobalt Guardian","Cogmaster","Coldarra Drake","Coldlight Oracle","Coldlight Seer","Coliseum Manager","Confessor Paletress","Core Hound","Core Rager","Crazed Alchemist","Crowd Favorite","Cruel Taskmaster","Cult Master","Cutpurse","Dalaran Aspirant","Dalaran Mage","Dancing Swords","Dark Cultist","Dark Iron Dwarf","Dark Iron Skulker","Dark Peddler","Darkscale Healer","Darnassus Aspirant","Deathlord","Deathwing","Defender of Argus","Defias Ringleader","Demolisher","Desert Camel","Dire Wolf Alpha","Djinni of Zephyrs","Doomguard","Doomsayer","Dr. Boom","Draenei Totemcarver","Dragon Consort","Dragon Egg","Dragon's Breath","Dragonhawk Rider","Dragonkin Sorcerer","Dragonling Mechanic","Drakonid Crusher","Dread Corsair","Dread Infernal","Dreadscale","Dreadsteed","Druid of the Claw","Druid of the Fang","Druid of the Flame","Druid of the Saber","Dunemaul Shaman","Dust Devil","Eadric the Pure","Earth Elemental","Earthen Ring Farseer","Echoing Ooze","Edwin VanCleef","Eerie Statue","Elise Starseeker","Elite Tauren Chieftain","Elven Archer","Emperor Cobra","Emperor Thaurissan","Enhance-o Mechano","Ethereal Arcanist","Ethereal Conjurer","Evil Heckler","Explosive Sheep","Eydis Darkbane","Faceless Manipulator","Faerie Dragon","Fallen Hero","Fearsome Doomguard","Fel Cannon","Fel Reaver","Felguard","Fen Creeper","Fencing Coach","Feugen","Fierce Monkey","Fire Elemental","Fireguard Destroyer","Fjola Lightbane","Flame Imp","Flame Juggler","Flame Leviathan","Flametongue Totem","Flamewaker","Flesheating Ghoul","Floating Watcher","Flying Machine","Foe Reaper 4000","Force-Tank MAX","Fossilized Devilsaur","Frigid Snobold","Frost Elemental","Frost Giant","Frostwolf Grunt","Frostwolf Warlord","Frothing Berserker","Gadgetzan Auctioneer","Gadgetzan Jouster","Gahz'rilla","Garrison Commander","Gazlowe","Gelbin Mekkatorque","Gilblin Stalker","Gnomeregan Infantry","Gnomish Experimenter","Gnomish Inventor","Goblin Auto-Barber","Goblin Blastmage","Goblin Sapper","Goldshire Footman","Gorillabot A-3","Gormok the Impaler","Grand Crusader","Grim Patron","Grimscale Oracle","Grommash Hellscream","Grove Tender","Gruul","Guardian of Kings","Gurubashi Berserker","Harrison Jones","Harvest Golem","Haunted Creeper","Hemet Nesingwary","Hobgoblin","Hogger","Holy Champion","Houndmaster","Huge Toad","Hungry Crab","Hungry Dragon","Ice Rager","Icehowl","Illidan Stormrage","Illuminator","Imp Gang Boss","Imp Master","Injured Blademaster","Injured Kvaldir","Iron Juggernaut","Iron Sensei","Ironbark Protector","Ironbeak Owl","Ironforge Rifleman","Ironfur Grizzly","Jeeves","Jeweled Scarab","Jungle Moonkin","Jungle Panther","Junkbot","Justicar Trueheart","Keeper of the Grove","Keeper of Uldaman","Kel'Thuzad","Kezan Mystic","Kidnapper","King Krush","King Mukla","King of Beasts","King's Elekk","Kirin Tor Mage","Knife Juggler","Knight of the Wild","Kobold Geomancer","Kodorider","Kor'Kron Elite","Kvaldir Raider","Lance Carrier","Leeroy Jenkins","Leper Gnome","Light's Champion","Lightspawn","Lightwarden","Lightwell","Lil' Exorcist","Loatheb","Loot Hoarder","Lord Jaraxxus","Lord of the Arena","Lorewalker Cho","Lost Tallstrider","Lowly Squire","Mad Bomber","Mad Scientist","Madder Bomber","Maexxna","Magma Rager","Magnataur Alpha","Maiden of the Lake","Majordomo Executus","Mal'Ganis","Malorne","Malygos","Mana Addict","Mana Tide Totem","Mana Wraith","Mana Wyrm","Master Jouster","Master of Ceremonies","Master of Disguise","Master Swordsmith","Mech-Bear-Cat","Mechanical Yeti","Mechwarper","Mekgineer Thermaplugg","Metaltooth Leaper","Micro Machine","Millhouse Manastorm","Mimiron's Head","Mind Control Tech","Mini-Mage","Mistress of Pain","Mogor the Ogre","Mogor's Champion","Mogu'shan Warden","Molten Giant","Mountain Giant","Mounted Raptor","Mukla's Champion","Murloc Knight","Murloc Raider","Murloc Tidecaller","Murloc Tidehunter","Murloc Tinyfin","Murloc Warleader","Museum Curator","Mysterious Challenger","Naga Sea Witch","Nat Pagle","Nefarian","Neptulon","Nerub'ar Weblord","Nerubian Egg","Nexus-Champion Saraad","Nightblade","North Sea Kraken","Northshire Cleric","Novice Engineer","Nozdormu","Oasis Snapjaw","Obsidian Destroyer","Ogre Brute","Ogre Magi","Ogre Ninja","Ogre Warmaul","Old Murk-Eye","One-Eyed Cheat","Onyxia","Orgrimmar Aspirant","Patient Assassin","Piloted Shredder","Piloted Sky Golem","Pint-Sized Summoner","Pit Fighter","Pit Lord","Pit Snake","Priestess of Elune","Prophet Velen","Puddlestomper","Quartermaster","Questing Adventurer","Raging Worgen","Ragnaros the Firelord","Raid Leader","Ram Wrangler","Raven Idol","Ravenholdt Assassin","Razorfen Hunter","Reckless Rocketeer","Recombobulator","Recruiter","Refreshment Vendor","Reliquary Seeker","Rend Blackhand","Reno Jackson","Rhonin","River Crocolisk","Rumbling Elemental","Saboteur","Salty Dog","Savage Combatant","Savannah Highmane","Scarlet Crusader","Scarlet Purifier","Scavenging Hyena","Screwjank Clunker","Sea Giant","Sea Reaver","Secretkeeper","Sen'jin Shieldmasta","Shade of Naxxramas","Shado-Pan Rider","Shadowbomber","Shadowboxer","Shadowfiend","Shady Dealer","Shattered Sun Cleric","Shieldbearer","Shielded Minibot","Shieldmaiden","Ship's Cannon","Shrinkmeister","SI:7 Agent","Sideshow Spelleater","Siege Engine","Silent Knight","Siltfin Spiritwalker","Silver Hand Knight","Silver Hand Regent","Silverback Patriarch","Silvermoon Guardian","Sir Finley Mrrgglton","Skycap'n Kragg","Sludge Belcher","Sneed's Old Shredder","Snowchugger","Solemn Vigil","Soot Spewer","Sorcerer's Apprentice","Southsea Captain","Southsea Deckhand","Sparring Partner","Spawn of Shadows","Spectral Knight","Spellbreaker","Spellslinger","Spider Tank","Spiteful Smith","Stablemaster","Stalagg","Stampeding Kodo","Starving Buzzard","Steamwheedle Sniper","Stoneskin Gargoyle","Stonesplinter Trogg","Stonetusk Boar","Stormpike Commando","Stormwind Champion","Stormwind Knight","Stranglethorn Tiger","Succubus","Summoning Stone","Sunfury Protector","Sunwalker","Sylvanas Windrunner","Target Dummy","Tauren Warrior","Temple Enforcer","The Beast","The Black Knight","The Mistcaller","The Skeleton Knight","Thrallmar Farseer","Thunder Bluff Valiant","Timber Wolf","Tinkertown Technician","Tinkmaster Overspark","Tiny Knight of Evil","Tirion Fordring","Tomb Pillager","Tomb Spider","Toshley","Totem Golem","Tournament Attendee","Tournament Medic","Trade Prince Gallywix","Troggzor the Earthinator","Truesilver Champion","Tundra Rhino","Tunnel Trogg","Tuskarr Jouster","Tuskarr Totemic","Twilight Drake","Twilight Guardian","Twilight Whelp","Unbound Elemental","Undercity Valiant","Undertaker","Unearthed Raptor","Unstable Ghoul","Upgraded Repair Bot","Varian Wrynn","Venture Co. Mercenary","Violet Teacher","Vitality Totem","Void Crusher","Void Terror","Voidcaller","Voidwalker","Vol'jin","Volcanic Drake","Volcanic Lumberer","Voodoo Doctor","Wailing Soul","War Golem","Warbot","Warhorse Trainer","Warsong Commander","Water Elemental","Webspinner","Wee Spellstopper","Whirling Zap-o-matic","Wild Pyromancer","Wildwalker","Wilfred Fizzlebang","Windfury Harpy","Windspeaker","Wisp","Wobbling Runts","Wolfrider","Worgen Infiltrator","Wrathguard","Wyrmrest Agent","Young Dragonhawk","Young Priestess","Youthful Brewmaster","Ysera","Zombie Chow"]
zeroCostMinion = ["Murloc Tinyfin","Target Dummy","Wisp"]
oneCostMinion = ["Abusive Sergeant","Angry Chicken","Argent Squire","Blood Imp","Bloodsail Corsair","Brave Archer","Buccaneer","Clockwork Gnome","Cogmaster","Dragon Egg","Dust Devil","Elven Archer","Flame Imp","Gadgetzan Jouster","Goldshire Footman","Grimscale Oracle","Hungry Crab","Injured Kvaldir","Leper Gnome","Lightwarden","Lowly Squire","Mana Wyrm","Murloc Raider","Murloc Tidecaller","Northshire Cleric","Pit Snake","Raven Idol","Reliquary Seeker","Secretkeeper","Shadowbomber","Shieldbearer","Sir Finley Mrrgglton","Southsea Deckhand","Stonetusk Boar","Timber Wolf","Tournament Attendee","Tunnel Trogg","Twilight Whelp","Undertaker","Voidwalker","Voodoo Doctor","Warbot","Webspinner","Worgen Infiltrator","Young Dragonhawk","Young Priestess","Zombie Chow"]
twoCostMinion =["Acidic Swamp Ooze","Alexstrasza's Champion","Amani Berserker","Ancient Watcher","Annoy-o-Tron","Anodized Robo Cub","Argent Protector","Argent Watchman","Armorsmith","Bloodfen Raptor","Bloodmage Thalnos","Bloodsail Raider","Bluegill Warrior","Boneguard Lieutenant","Captain's Parrot","Crazed Alchemist","Cruel Taskmaster","Cutpurse","Dark Peddler","Darnassus Aspirant","Defias Ringleader","Dire Wolf Alpha","Doomsayer","Druid of the Saber","Echoing Ooze","Explosive Sheep","Faerie Dragon","Fallen Hero","Flame Juggler","Flametongue Totem","Frostwolf Grunt","Garrison Commander","Gilblin Stalker","Goblin Auto-Barber","Haunted Creeper","Huge Toad","Jeweled Scarab","King's Elekk","Knife Juggler","Kobold Geomancer","Lance Carrier","Lightwell","Loot Hoarder","Lorewalker Cho","Mad Bomber","Mad Scientist","Mana Addict","Mana Wraith","Master Swordsmith","Mechwarper","Micro Machine","Millhouse Manastorm","Mistress of Pain","Murloc Tidehunter","Museum Curator","Nat Pagle","Nerub'ar Weblord","Nerubian Egg","Novice Engineer","One-Eyed Cheat","Patient Assassin","Pint-Sized Summoner","Puddlestomper","Recombobulator","River Crocolisk","Scavenging Hyena","Shadowboxer","Shielded Minibot","Ship's Cannon","Shrinkmeister","Snowchugger","Sorcerer's Apprentice","Sparring Partner","Steamwheedle Sniper","Stonesplinter Trogg","Succubus","Sunfury Protector","Tiny Knight of Evil","Totem Golem","Undercity Valiant","Unstable Ghoul","Vitality Totem","Whirling Zap-o-matic","Wild Pyromancer","Wrathguard","Wyrmrest Agent","Youthful Brewmaster"]
threeCostMinion = ["Acolyte of Pain","Alarm-o-Bot","Aldor Peacekeeper","Arcane Golem","Argent Horserider","Blackwing Technician","Blood Knight","Brann Bronzebeard","Coldlight Oracle","Coldlight Seer","Coliseum Manager","Dalaran Mage","Dancing Swords","Dark Cultist","Deathlord","Demolisher","Desert Camel","Dragonhawk Rider","Dreadscale","Druid of the Flame","Earthen Ring Farseer","Edwin VanCleef","Emperor Cobra","Eydis Darkbane","Felguard","Fencing Coach","Fierce Monkey","Fjola Lightbane","Flamewaker","Flesheating Ghoul","Flying Machine","Frothing Berserker","Gnomeregan Infantry","Gnomish Experimenter","Goblin Sapper","Grove Tender","Harvest Golem","Hobgoblin","Ice Rager","Illuminator","Imp Gang Boss","Imp Master","Injured Blademaster","Iron Sensei","Ironbeak Owl","Ironforge Rifleman","Ironfur Grizzly","Jungle Panther","King Mukla","Kirin Tor Mage","Light's Champion","Lil' Exorcist","Magma Rager","Mana Tide Totem","Master of Ceremonies","Metaltooth Leaper","Mind Control Tech","Mounted Raptor","Murloc Warleader","Ogre Brute","Ogre Warmaul","Orgrimmar Aspirant","Questing Adventurer","Raging Worgen","Raid Leader","Razorfen Hunter","Saboteur","Scarlet Crusader","Scarlet Purifier","Shade of Naxxramas","Shadowfiend","Shady Dealer","Shattered Sun Cleric","SI:7 Agent","Silent Knight","Silver Hand Regent","Silverback Patriarch","Soot Spewer","Southsea Captain","Spellslinger","Spider Tank","Stablemaster","Stoneskin Gargoyle","Tauren Warrior","Thrallmar Farseer","Tinkertown Technician","Tinkmaster Overspark","Tuskarr Totemic","Unbound Elemental","Unearthed Raptor","Void Terror","Warhorse Trainer","Warsong Commander","Wolfrider"]
fourCostMinion = ["Ancient Brewmaster","Ancient Mage","Ancient Shade","Animated Armor","Anub'ar Ambusher","Arathi Weaponsmith","Arcane Nullifier X-21","Armored Warhorse","Auchenai Soulpriest","Axe Flinger","Baron Rivendare","Burly Rockjaw Trogg","Chillwind Yeti","Core Rager","Crowd Favorite","Cult Master","Dalaran Aspirant","Dark Iron Dwarf","Defender of Argus","Draenei Totemcarver","Dragonkin Sorcerer","Dragonling Mechanic","Dread Corsair","Dreadsteed","Dunemaul Shaman","Eerie Statue","Elise Starseeker","Enhance-o Mechano","Ethereal Arcanist","Evil Heckler","Fel Cannon","Fireguard Destroyer","Frigid Snobold","Gnomish Inventor","Goblin Blastmage","Gorillabot A-3","Gormok the Impaler","Holy Champion","Houndmaster","Hungry Dragon","Jeeves","Jungle Moonkin","Keeper of the Grove","Keeper of Uldaman","Kezan Mystic","Kor'Kron Elite","Lightspawn","Lost Tallstrider","Magnataur Alpha","Maiden of the Lake","Master of Disguise","Mechanical Yeti","Mini-Mage","Mogu'shan Warden","Murloc Knight","Oasis Snapjaw","Ogre Magi","Old Murk-Eye","Piloted Shredder","Pit Lord","Refreshment Vendor","Rumbling Elemental","Savage Combatant","Screwjank Clunker","Sen'jin Shieldmasta","Siltfin Spiritwalker","Silvermoon Guardian","Spawn of Shadows","Spellbreaker","Stormwind Knight","Tomb Pillager","Tomb Spider","Tournament Medic","Truesilver Champion","Twilight Drake","Twilight Guardian","Violet Teacher","Voidcaller","Wailing Soul","Water Elemental","Wee Spellstopper","Wildwalker","Windspeaker"]
fiveCostMinion = ["Abomination","Antique Healbot","Anubisath Sentinel","Azure Drake","Big Game Hunter","Blackwing Corruptor","Blingtron 3000","Bolvar Fordragon","Bomb Lobber","Booty Bay Bodyguard","Captain Greenskin","Clockwork Knight","Cobalt Guardian","Dark Iron Skulker","Darkscale Healer","Djinni of Zephyrs","Doomguard","Dragon Consort","Dragon's Breath","Druid of the Claw","Druid of the Fang","Earth Elemental","Elite Tauren Chieftain","Ethereal Conjurer","Faceless Manipulator","Fel Reaver","Fen Creeper","Feugen","Floating Watcher","Frostwolf Warlord","Grim Patron","Gurubashi Berserker","Harrison Jones","Hemet Nesingwary","Junkbot","King of Beasts","Kvaldir Raider","Leeroy Jenkins","Loatheb","Madder Bomber","Mimiron's Head","Mukla's Champion","Naga Sea Witch","Nexus-Champion Saraad","Nightblade","Ogre Ninja","Pit Fighter","Quartermaster","Ram Wrangler","Recruiter","Salty Dog","Shado-Pan Rider","Siege Engine","Silver Hand Knight","Sludge Belcher","Solemn Vigil","Spectral Knight","Spiteful Smith","Stalagg","Stampeding Kodo","Starving Buzzard","Stormpike Commando","Stranglethorn Tiger","Summoning Stone","Thunder Bluff Valiant","Tundra Rhino","Tuskarr Jouster","Upgraded Repair Bot","Venture Co. Mercenary","Vol'jin"]
sixCostMinion = ["Anima Golem","Archmage","Argent Commander","Bolf Ramshield","Boulderfist Ogre","Cabal Shadow Priest","Cairne Bloodhoof","Coldarra Drake","Drakonid Crusher","Dread Infernal","Emperor Thaurissan","Fire Elemental","Frost Elemental","Gadgetzan Auctioneer","Gazlowe","Gelbin Mekkatorque","Grand Crusader","Hogger","Illidan Stormrage","Iron Juggernaut","Justicar Trueheart","Kidnapper","Kodorider","Lord of the Arena","Maexxna","Master Jouster","Mech-Bear-Cat","Mogor the Ogre","Mogor's Champion","Mysterious Challenger","Piloted Sky Golem","Priestess of Elune","Reckless Rocketeer","Reno Jackson","Savannah Highmane","Sea Reaver","Shieldmaiden","Sideshow Spelleater","Sunwalker","Sylvanas Windrunner","Temple Enforcer","The Beast","The Black Knight","The Mistcaller","The Skeleton Knight","Toshley","Trade Prince Gallywix","Void Crusher","Volcanic Drake","Wilfred Fizzlebang","Windfury Harpy","Wobbling Runts"]
sevenCostMinion = ["Acidmaw","Ancient of Lore","Ancient of War","Archmage Antonidas","Baron Geddon","Captured Jormungar","Chillmaw","Confessor Paletress","Core Hound","Dr. Boom","Eadric the Pure","Fearsome Doomguard","Flame Leviathan","Gahz'rilla","Guardian of Kings","Knight of the Wild","Malorne","Neptulon","Obsidian Destroyer","Prophet Velen","Ravenholdt Assassin","Rend Blackhand","Skycap'n Kragg","Stormwind Champion","Troggzor the Earthinator","War Golem"]
eightCostMinion = ["Al'Akir the Windlord","Chromaggus","Foe Reaper 4000","Force-Tank MAX","Fossilized Devilsaur","Grommash Hellscream","Gruul","Ironbark Protector","Kel'Thuzad","Ragnaros the Firelord","Rhonin","Sneed's Old Shredder","Tirion Fordring"]
nineCostMinion = ["Alexstrasza","Anub'arak","Arch-Thief Rafaam","Aviana","Cenarius","Icehowl","King Krush","Lord Jaraxxus","Majordomo Executus","Mal'Ganis","Malygos","Mekgineer Thermaplugg","Nefarian","North Sea Kraken","Nozdormu","Onyxia","Volcanic Lumberer","Ysera"]
tenCostMinion = ["Deathwing","Frost Giant","Sea Giant","Varian Wrynn"]

allBeasts = ["Angry Chicken","Armored Warhorse","Bloodfen Raptor","Captain's Parrot","Captured Jormungar","Core Hound","Core Rager","Desert Camel","Dire Wolf Alpha","Dreadscale","Emperor Cobra","Fierce Monkey","Gahz'rilla","Haunted Creeper","Huge Toad","Hungry Crab","Ironbeak Owl","Ironfur Grizzly","Jeweled Scarab","Jungle Moonkin","Jungle Panther","King Krush","King Mukla","King of Beasts","King's Elekk","Lost Tallstrider","Maexxna","Malorne","Mounted Raptor","Mukla's Champion","Oasis Snapjaw","Pit Snake","River Crocolisk","Savage Combatant","Savannah Highmane","Scavenging Hyena","Silverback Patriarch","Stampeding Kodo","Starving Buzzard","Stonetusk Boar","Stranglethorn Tiger","The Beast","Timber Wolf","Tomb Spider","Webspinner","Young Dragonhawk"]
beastCompanion = ["Huffer","Misha","Leokk"]

allTotems = ["Flametongue Totem","Healing Totem","Mana Tide Totem","Searing Totem","Stoneclaw Totem","Totem Golem","Vitality Totem","Wrath of Air Totem"]
heroTotems = ["Healing Totem","Searing Totem","Stoneclaw Totem","Wrath of Air Totem"]

allMechs = ["Alarm-o-Bot","Anima Golem","Annoy-o-Tron","Anodized Robo Cub","Antique Healbot","Arcane Nullifier X-21","Blingtron 3000","Clockwork Giant","Clockwork Gnome","Clockwork Knight","Cobalt Guardian","Demolisher","Enhance-o Mechano","Explosive Sheep","Fel Cannon","Fel Reaver","Flame Leviathan","Flying Machine","Foe Reaper 4000","Force-Tank MAX","Goblin Auto-Barber","Gorillabot A-3","Harvest Golem","Iron Juggernaut","Iron Sensei","Jeeves","Junkbot","Mech-Bear-Cat","Mechanical Yeti","Mechwarper","Mekgineer Thermaplugg","Metaltooth Leaper","Micro Machine","Mimiron's Head","Piloted Shredder","Piloted Sky Golem","Screwjank Clunker","Shadowbomber","Shielded Minibot","Siege Engine","Sneed's Old Shredder","Snowchugger","Soot Spewer","Spider Tank","Target Dummy","Upgraded Repair Bot","Warbot","Whirling Zap-o-matic"]
enhanceO =["Divine Shield","Windfury","Taunt"]

allMurlocs =["Bluegill Warrior","Coldlight Oracle","Coldlight Seer","Grimscale Oracle","Murloc Knight","Murloc Raider","Murloc Tidecaller","Murloc Tidehunter","Murloc Tinyfin","Murloc Warleader","Old Murk-Eye","Puddlestomper","Siltfin Spiritwalker","Sir Finley Mrrgglton"]

allDemons = ["Blood Imp","Doomguard","Dread Infernal","Dreadsteed","Fearsome Doomguard","Felguard","Flame Imp","Floating Watcher","Illidan Stormrage","Imp Gang Boss","Lord Jaraxxus","Mal'Ganis","Mistress of Pain","Pit Lord","Succubus","Tiny Knight of Evil","Void Crusher","Void Terror","Voidcaller","Voidwalker","Wrathguard"]

allDeathrattle = ["Abomination","Anub'ar Ambusher","Anub'arak","Anubisath Sentinel","Bloodmage Thalnos","Cairne Bloodhoof","Charged Hammer","Chillmaw","Clockwork Gnome","Dancing Swords","Dark Cultist","Darnassus Aspirant","Death's Bite","Deathlord","Dreadsteed","Explosive Sheep","Feugen","Harvest Golem","Haunted Creeper","Huge Toad","Leper Gnome","Loot Hoarder","Mad Scientist","Majordomo Executus","Malorne","Mechanical Yeti","Mounted Raptor","Nerubian Egg","Piloted Shredder","Piloted Sky Golem","Powermace","Rhonin","Savannah Highmane","Sludge Belcher","Sneed's Old Shredder","Stalagg","Sylvanas Windrunner","The Beast","The Skeleton Knight","Tirion Fordring","Tomb Pillager","Toshley","Unstable Ghoul","Voidcaller","Webspinner","Wobbling Runts","Zombie Chow"]

allSpells = ["Ancestor's Call","Ancestral Healing","Ancestral Knowledge","Ancestral Spirit","Animal Companion","Anyfin Can Happen","Arcane Blast","Arcane Explosion","Arcane Intellect","Arcane Missiles","Arcane Shot","Assassinate","Astral Communion","Avenge","Avenging Wrath","Backstab","Ball of Spiders","Bane of Doom","Bash","Battle Rage","Bear Trap","Beneath the Grounds","Bestial Wrath","Betrayal","Bite","Blade Flurry","Blessed Champion","Blessing of Kings","Blessing of Might","Blessing of Wisdom","Blizzard","Bloodlust","Bolster","Bouncing Blade","Brawl","Burgle","Call Pet","Charge","Circle of Healing","Claw","Cleave","Cobra Shot","Cold Blood","Commanding Shout","Competitive Spirit","Conceal","Cone of Cold","Confuse","Consecration","Convert","Corruption","Counterspell","Crackle","Crush","Curse of Rafaam","Dark Bargain","Dark Wispers","Darkbomb","Dart Trap","Deadly Poison","Deadly Shot","Demonfire","Demonfuse","Demonheart","Demonwrath","Divine Favor","Divine Spirit","Drain Life","Duplicate","Earth Shock","Echo of Medivh","Effigy","Elemental Destruction","Enter the Coliseum","Entomb","Equality","Everyfin is Awesome","Eviscerate","Excavated Evil","Execute","Explorer's Hat","Explosive Shot","Explosive Trap","Eye for an Eye","Fan of Knives","Far Sight","Feign Death","Feral Spirit","Fireball","Fist of Jaraxxus","Flame Lance","Flamecannon","Flamestrike","Flare","Flash Heal","Force of Nature","Forgotten Torch","Forked Lightning","Freezing Trap","Frost Nova","Frost Shock","Frostbolt","Gang Up","Hand of Protection","Headcrack","Healing Touch","Healing Wave","Hellfire","Heroic Strike","Hex","Holy Fire","Holy Light","Holy Nova","Holy Smite","Holy Wrath","Humility","Hunter's Mark","Ice Barrier","Ice Block","Ice Lance","Imp-losion","Inner Fire","Inner Rage","Innervate","Kill Command","Lava Burst","Lava Shock","Lay on Hands","Light of the Naaru","Lightbomb","Lightning Bolt","Lightning Storm","Living Roots","Lock and Load","Mark of Nature","Mark of the Wild","Mass Dispel","Mind Blast","Mind Control","Mind Vision","Mindgames","Mirror Entity","Mirror Image","Misdirection","Moonfire","Mortal Coil","Mortal Strike","Mulch","Multi-Shot","Muster for Battle","Naturalize","Noble Sacrifice","Nourish","Poison Seeds","Polymorph","Polymorph: Boar","Power of the Wild","Power Overwhelming","Power Word: Glory","Power Word: Shield","Powershot","Preparation","Pyroblast","Quick Shot","Rampage","Recycle","Redemption","Reincarnate","Repentance","Resurrect","Revenge","Sabotage","Sacred Trial","Sacrificial Pact","Sap","Savage Roar","Savagery","Seal of Champions","Seal of Light","Sense Demons","Shadow Bolt","Shadow Madness","Shadow Word: Death","Shadow Word: Pain","Shadowflame","Shadowform","Shadowstep","Shield Block","Shield Slam","Shiv","Silence","Sinister Strike","Siphon Soul","Slam","Snake Trap","Snipe","Soul of the Forest","Soulfire","Spellbender","Sprint","Starfall","Starfire","Summoning Portal","Swipe","Thoughtsteal","Tinker's Sharpsword Oil","Totemic Might","Tracking","Tree of Life","Twisting Nether","Unleash the Hounds","Unstable Portal","Upgrade!","Vanish","Vaporize","Velen's Chosen","Whirlwind","Wild Growth","Windfury","Wrath"]
mageSpells = ["Arcane Blast","Arcane Explosion","Arcane Intellect","Arcane Missiles","Blizzard","Cone of Cold","Counterspell","Duplicate","Echo of Medivh","Effigy","Fireball","Flame Lance","Flamecannon","Flamestrike","Forgotten Torch","Frost Nova","Frostbolt","Ice Barrier","Ice Block","Ice Lance","Mirror Entity","Mirror Image","Polymorph","Polymorph: Boar","Pyroblast","Spellbender","Unstable Portal","Vaporize"]
priestSpells = ["Circle of Healing","Confuse","Convert","Divine Spirit","Entomb","Excavated Evil","Flash Heal","Holy Fire","Holy Nova","Holy Smite","Inner Fire","Light of the Naaru","Lightbomb","Mass Dispel","Mind Blast","Mind Control","Mind Vision","Mindgames","Power Word: Glory","Power Word: Shield","Resurrect","Shadow Madness","Shadow Word: Death","Shadow Word: Pain","Shadowform","Silence","Thoughtsteal","Velen's Chosen"]
warriorSpells = ["Bash","Battle Rage","Bolster","Bouncing Blade","Brawl","Charge","Cleave","Commanding Shout","Crush","Execute","Heroic Strike","Inner Rage","Mortal Strike","Rampage","Revenge","Shield Block","Shield Slam","Slam","Upgrade!","Whirlwind"]
shamanSpells = ["Ancestor's Call","Ancestral Healing","Ancestral Knowledge","Ancestral Spirit","Bloodlust","Crackle","Earth Shock","Elemental Destruction","Everyfin is Awesome","Far Sight","Feral Spirit","Forked Lightning","Frost Shock","Healing Wave","Hex","Lava Burst","Lava Shock","Lightning Bolt","Lightning Storm","Reincarnate","Totemic Might","Windfury"]
warlockSpells = ["Bane of Doom","Corruption","Curse of Rafaam","Dark Bargain","Darkbomb","Demonfire","Demonfuse","Demonheart","Demonwrath","Drain Life","Fist of Jaraxxus","Hellfire","Imp-losion","Mortal Coil","Power Overwhelming","Sacrificial Pact","Sense Demons","Shadow Bolt","Shadowflame","Siphon Soul","Soulfire","Summoning Portal","Twisting Nether"]
paladinSpells = ["Anyfin Can Happen","Avenge","Avenging Wrath","Blessed Champion","Blessing of Kings","Blessing of Might","Blessing of Wisdom","Competitive Spirit","Consecration","Divine Favor","Enter the Coliseum","Equality","Eye for an Eye","Hand of Protection","Holy Light","Holy Wrath","Humility","Lay on Hands","Muster for Battle","Noble Sacrifice","Redemption","Repentance","Sacred Trial","Seal of Champions","Seal of Light"]
hunterSpells = ["Animal Companion","Arcane Shot","Ball of Spiders","Bear Trap","Bestial Wrath","Call Pet","Cobra Shot","Dart Trap","Deadly Shot","Explorer's Hat","Explosive Shot","Explosive Trap","Feign Death","Flare","Freezing Trap","Hunter's Mark","Kill Command","Lock and Load","Misdirection","Multi-Shot","Powershot","Quick Shot","Snake Trap","Snipe","Tracking","Unleash the Hounds"]
rogueSpells = ["Assassinate","Backstab","Beneath the Grounds","Betrayal","Blade Flurry","Burgle","Cold Blood","Conceal","Deadly Poison","Eviscerate","Fan of Knives","Gang Up","Headcrack","Preparation","Sabotage","Sap","Shadowstep","Shiv","Sinister Strike","Sprint","Tinker's Sharpsword Oil","Vanish"]
druidSpells = ["Astral Communion","Bite","Claw","Dark Wispers","Force of Nature","Healing Touch","Innervate","Living Roots","Mark of Nature","Mark of the Wild","Moonfire","Mulch","Naturalize","Nourish","Poison Seeds","Power of the Wild","Recycle","Savage Roar","Savagery","Soul of the Forest","Starfall","Starfire","Swipe","Tree of Life","Wild Growth","Wrath"]

classDruid = ["Ancient of Lore","Ancient of War","Anodized Robo Cub","Astral Communion","Aviana","Bite","Cenarius","Claw","Dark Wispers","Darnassus Aspirant","Druid of the Claw","Druid of the Fang","Druid of the Flame","Druid of the Saber","Force of Nature","Grove Tender","Healing Touch","Innervate","Ironbark Protector","Jungle Moonkin","Keeper of the Grove","Knight of the Wild","Living Roots","Malorne","Mark of Nature","Mark of the Wild","Mech-Bear-Cat","Moonfire","Mounted Raptor","Mulch","Naturalize","Nourish","Poison Seeds","Power of the Wild","Raven Idol","Recycle","Savage Combatant","Savage Roar","Savagery","Soul of the Forest","Starfall","Starfire","Swipe","Tree of Life","Volcanic Lumberer","Wild Growth","Wildwalker","Wrath"]
classHunter = ["Acidmaw","Animal Companion","Arcane Shot","Ball of Spiders","Bear Trap","Bestial Wrath","Brave Archer","Call Pet","Cobra Shot","Core Rager","Dart Trap","Deadly Shot","Desert Camel","Dreadscale","Eaglehorn Bow","Explorer's Hat","Explosive Shot","Explosive Trap","Feign Death","Flare","Freezing Trap","Gahz'rilla","Gladiator's Longbow","Glaivezooka","Houndmaster","Hunter's Mark","Kill Command","King Krush","King of Beasts","King's Elekk","Lock and Load","Metaltooth Leaper","Misdirection","Multi-Shot","Powershot","Quick Shot","Ram Wrangler","Savannah Highmane","Scavenging Hyena","Snake Trap","Snipe","Stablemaster","Starving Buzzard","Steamwheedle Sniper","Timber Wolf","Tracking","Tundra Rhino","Unleash the Hounds","Webspinner"]
classMage = ["Animated Armor","Arcane Blast","Arcane Explosion","Arcane Intellect","Arcane Missiles","Archmage Antonidas","Blizzard","Coldarra Drake","Cone of Cold","Counterspell","Dalaran Aspirant","Dragon's Breath","Duplicate","Echo of Medivh","Effigy","Ethereal Arcanist","Ethereal Conjurer","Fallen Hero","Fireball","Flame Lance","Flame Leviathan","Flamecannon","Flamestrike","Flamewaker","Forgotten Torch","Frost Nova","Frostbolt","Goblin Blastmage","Ice Barrier","Ice Block","Ice Lance","Kirin Tor Mage","Mana Wyrm","Mirror Entity","Mirror Image","Polymorph","Polymorph: Boar","Pyroblast","Rhonin","Snowchugger","Soot Spewer","Sorcerer's Apprentice","Spellbender","Spellslinger","Unstable Portal","Vaporize","Water Elemental","Wee Spellstopper"]
classPaladin = ["Aldor Peacekeeper","Anyfin Can Happen","Argent Lance","Argent Protector","Avenge","Avenging Wrath","Blessed Champion","Blessing of Kings","Blessing of Might","Blessing of Wisdom","Bolvar Fordragon","Cobalt Guardian","Coghammer","Competitive Spirit","Consecration","Divine Favor","Dragon Consort","Eadric the Pure","Enter the Coliseum","Equality","Eye for an Eye","Guardian of Kings","Hammer of Wrath","Hand of Protection","Holy Light","Holy Wrath","Humility","Keeper of Uldaman","Lay on Hands","Light's Justice","Murloc Knight","Muster for Battle","Mysterious Challenger","Noble Sacrifice","Quartermaster","Redemption","Repentance","Sacred Trial","Scarlet Purifier","Seal of Champions","Seal of Light","Shielded Minibot","Solemn Vigil","Sword of Justice","Tirion Fordring","Truesilver Champion","Tuskarr Jouster","Warhorse Trainer"]
classPriest = ["Auchenai Soulpriest","Cabal Shadow Priest","Circle of Healing","Confessor Paletress","Confuse","Convert","Dark Cultist","Divine Spirit","Entomb","Excavated Evil","Flash Heal","Holy Champion","Holy Fire","Holy Nova","Holy Smite","Inner Fire","Light of the Naaru","Lightbomb","Lightspawn","Lightwell","Mass Dispel","Mind Blast","Mind Control","Mind Vision","Mindgames","Museum Curator","Northshire Cleric","Power Word: Glory","Power Word: Shield","Prophet Velen","Resurrect","Shadow Madness","Shadow Word: Death","Shadow Word: Pain","Shadowbomber","Shadowboxer","Shadowfiend","Shadowform","Shrinkmeister","Silence","Spawn of Shadows","Temple Enforcer","Thoughtsteal","Twilight Whelp","Upgraded Repair Bot","Velen's Chosen","Vol'jin","Wyrmrest Agent"]
classRogue = ["Anub'ar Ambusher","Anub'arak","Assassin's Blade","Assassinate","Backstab","Beneath the Grounds","Betrayal","Blade Flurry","Buccaneer","Burgle","Cogmaster's Wrench","Cold Blood","Conceal","Cutpurse","Dark Iron Skulker","Deadly Poison","Defias Ringleader","Edwin VanCleef","Eviscerate","Fan of Knives","Gang Up","Goblin Auto-Barber","Headcrack","Iron Sensei","Kidnapper","Master of Disguise","Ogre Ninja","One-Eyed Cheat","Patient Assassin","Perdition's Blade","Pit Snake","Poisoned Blade","Preparation","Sabotage","Sap","Shado-Pan Rider","Shadowstep","Shady Dealer","Shiv","SI:7 Agent","Sinister Strike","Sprint","Tinker's Sharpsword Oil","Tomb Pillager","Trade Prince Gallywix","Undercity Valiant","Unearthed Raptor","Vanish"]
classShaman = ["Al'Akir the Windlord","Ancestor's Call","Ancestral Healing","Ancestral Knowledge","Ancestral Spirit","Bloodlust","Charged Hammer","Crackle","Doomhammer","Draenei Totemcarver","Dunemaul Shaman","Dust Devil","Earth Elemental","Earth Shock","Elemental Destruction","Everyfin is Awesome","Far Sight","Feral Spirit","Fire Elemental","Fireguard Destroyer","Flametongue Totem","Forked Lightning","Frost Shock","Healing Wave","Hex","Lava Burst","Lava Shock","Lightning Bolt","Lightning Storm","Mana Tide Totem","Neptulon","Powermace","Reincarnate","Rockbiter Weapon","Rumbling Elemental","Siltfin Spiritwalker","Stormforged Axe","The Mistcaller","Thunder Bluff Valiant","Totem Golem","Totemic Might","Tunnel Trogg","Tuskarr Totemic","Unbound Elemental","Vitality Totem","Whirling Zap-o-matic","Windfury","Windspeaker"]
classWarlock = ["Anima Golem","Bane of Doom","Blood Imp","Corruption","Curse of Rafaam","Dark Bargain","Dark Peddler","Darkbomb","Demonfire","Demonfuse","Demonheart","Demonwrath","Doomguard","Drain Life","Dread Infernal","Dreadsteed","Fearsome Doomguard","Fel Cannon","Felguard","Fist of Jaraxxus","Flame Imp","Floating Watcher","Hellfire","Imp Gang Boss","Imp-losion","Lord Jaraxxus","Mal'Ganis","Mistress of Pain","Mortal Coil","Pit Lord","Power Overwhelming","Reliquary Seeker","Sacrificial Pact","Sense Demons","Shadow Bolt","Shadowflame","Siphon Soul","Soulfire","Succubus","Summoning Portal","Tiny Knight of Evil","Twisting Nether","Void Crusher","Void Terror","Voidcaller","Voidwalker","Wilfred Fizzlebang","Wrathguard"]
classWarrior = ["Alexstrasza's Champion","Arathi Weaponsmith","Arcanite Reaper","Armorsmith","Axe Flinger","Bash","Battle Rage","Bolster","Bouncing Blade","Brawl","Charge","Cleave","Commanding Shout","Cruel Taskmaster","Crush","Cursed Blade","Death's Bite","Execute","Fierce Monkey","Fiery War Axe","Frothing Berserker","Gorehowl","Grommash Hellscream","Heroic Strike","Inner Rage","Iron Juggernaut","King's Defender","Kor'Kron Elite","Magnataur Alpha","Mortal Strike","Obsidian Destroyer","Ogre Warmaul","Orgrimmar Aspirant","Rampage","Revenge","Screwjank Clunker","Sea Reaver","Shield Block","Shield Slam","Shieldmaiden","Siege Engine","Slam","Sparring Partner","Upgrade!","Varian Wrynn","Warbot","Warsong Commander","Whirlwind"]

allWeapons = ["Arcanite Reaper","Argent Lance","Assassin's Blade","Battle Axe","Charged Hammer","Coghammer","Cogmaster's Wrench","Cursed Blade","Death's Bite","Doomhammer","Eaglehorn Bow","Fiery War Axe","Gladiator's Longbow","Glaivezooka","Gorehowl","Hammer of Wrath","Heavy Axe","King's Defender","Light's Justice","Perdition's Blade","Poisoned Blade","Powermace","Rockbiter Weapon","Rusty Hook","Stormforged Axe","Sword of Justice"]
oneThreeWeapons = ["Poisioned Blade","Heavy Axe","Rusty Hook"]
twoTwoWeapons = ["Argent Lance","Perdition's Blade","Battle Axe"]

spareParts = ["Armor Plating","Emergency Coolant","Finicky Cloakfield","Reversing Switch","Rusty Horn","Time Rewinder","Whirling Blades"]

inventions = ["Emboldener 3000","Homing Chicken","Poultryizer","Repair Bot"]

powerChords = ["I Am Murloc","Power of the Horde","Rogues Do It..."]

# *******************************************************
# Define buttons
# Make list of button value, text, and backlight color
# *******************************************************

buttons = ( (LCD.SELECT, 'Select', (0,0,1)),
            (LCD.LEFT,   'Left'  , (0,0,1)),
            (LCD.UP,     'Up'    , (0,0,1)),
            (LCD.DOWN,   'Down'  , (0,0,1)),
            (LCD.RIGHT,  'Right' , (0,0,1)) )

# *******************************************************
# Define functions
# *******************************************************

# ****** Main Menu ******

def minionsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Minions')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				allMinionsMenu()
				break
			if lcd.is_pressed(LCD.UP):
				otherMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				spellsMenu()
				break

def spellsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('     Spells')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				allSpellsMenu()
				break
			if lcd.is_pressed(LCD.UP):
				minionsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				classMenu()
				break

def classMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('  Class Cards')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				druidClassMenu()
				break
			if lcd.is_pressed(LCD.UP):
				spellsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				weaponsMenu()
				break

def weaponsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Weapons')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				allweaponsMenu()
				break
			if lcd.is_pressed(LCD.UP):
				classMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				xcostMenu()
				break

def xcostMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('  X-Cost Cards')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				oneCostMenu()
				break
			if lcd.is_pressed(LCD.UP):
				weaponsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				otherMenu()
				break

def otherMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('     Other')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				heroPowerMenu()
				break
			if lcd.is_pressed(LCD.UP):
				xcostMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				minionsMenu()
				break

# ****** Minions Submenu ******

def allMinionsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Summon a\n Random Minion')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranMinion = ('')
				ranMinion = random.choice(allMinions)
				lcd.message(ranMinion)
				break
			if lcd.is_pressed(LCD.UP):
				xCostMinionsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				beastMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				minionsMenu()
				break

def beastMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('     Beasts\n      Menu')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				allBeastsMenu()
				break
			if lcd.is_pressed(LCD.UP):
				allMinionsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				deathrattleMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				minionsMenu()
				break

def allBeastsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Summon a\n Random Beast')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranBeast = ('')
				ranBeast = random.choice(allBeasts)
				lcd.message(ranBeast)
				break
			if lcd.is_pressed(LCD.UP):
				beastCompanionMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				beastCompanionMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				beastMenu()
				break

def beastCompanionMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('Summon a Random\nBeast Companion')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranBeast = ('')
				ranBeast = random.choice(allBeasts)
				lcd.message(ranBeast)
				break
			if lcd.is_pressed(LCD.UP):
				allBeastsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				allBeastsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				beastMenu()
				break

def deathrattleMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('Summon a Random\nDthrattle Minion')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranDeathrattleMinion = ('')
				ranDeathrattleMinion = random.choice(allDeathrattle)
				lcd.message(ranDeathrattleMinion)
				break
			if lcd.is_pressed(LCD.UP):
				beastMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				demonsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				minionsMenu()
				break

def demonsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Summon a\n  Random Demon')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranDemon = ('')
				ranDemon = random.choice(allDemons)
				lcd.message(ranDemon)
				break
			if lcd.is_pressed(LCD.UP):
				deathrattleMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				legendaryMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				minionsMenu()
				break

def legendaryMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('Summon a Random\nLegendary Minion')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranLegend = ('')
				ranLegend = random.choice(legendaryMinions)
				lcd.message(ranLegend)
				break
			if lcd.is_pressed(LCD.UP):
				demonsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				mechMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				minionsMenu()
				break

def mechMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('     Mechs\n      Menu')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				allMechsMenu()
				break
			if lcd.is_pressed(LCD.UP):
				legendaryMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				murlocMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				minionsMenu()
				break

def allMechsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Summon a\n  Random Mech')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranMech = ('')
				ranMech = random.choice(allMechs)
				lcd.message(ranMech)
				break
			if lcd.is_pressed(LCD.UP):
				enchanceoMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				enchanceoMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				mechMenu()
				break

def enchanceoMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('   Enchance-O\nMechano Effects')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				enhanceoEffect = ('')
				enhanceoEffect = random.choice(enhanceO)
				lcd.message(enhanceoEffect)
				break
			if lcd.is_pressed(LCD.UP):
				allMechsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				allMechsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				mechMenu()
				break

def murlocMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Summon a\n Random Murloc')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranMurloc = ('')
				ranMurloc = random.choice(allMurlocs)
				lcd.message(ranMurloc)
				break
			if lcd.is_pressed(LCD.UP):
				mechMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				totemsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				minionsMenu()
				break

def totemsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('     Totems\n      Menu')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				heroTotemsMenu()
				break
			if lcd.is_pressed(LCD.UP):
				murlocMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				xCostMinionMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				minionsMenu()
				break

def allTotemsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('   Summon a\n  Random Totem')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranTotem = ('')
				ranTotem = random.choice(allTotems)
				lcd.message(ranTotem)
				break
			if lcd.is_pressed(LCD.UP):
				heroTotemsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				heroTotemsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				totemsMenu()
				break

def heroTotemsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('   Hero Power\n  Totem Summon')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranHeroTotem = ('')
				ranHeroTotem = random.choice(heroTotems)
				lcd.message(ranHeroTotem)
				break
			if lcd.is_pressed(LCD.UP):
				allTotemsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				allTotemsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				totemsMenu()
				break

def xCostMinionMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message(' X-Cost Minion\n      Menu')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				zeroCostMinionMenu()
				break
			if lcd.is_pressed(LCD.UP):
				totemsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				allMinionsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				minionsMenu()
				break

def zeroCostMinionMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Summon a\n 0 Cost Minion')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranZeroMinion = ('')
				ranZeroMinion = random.choice(zeroCostMinion)
				lcd.message(ranZeroMinion)
				break
			if lcd.is_pressed(LCD.UP):
				tenCostMinionMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				oneCostMinionMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				xCostMinionMenu()
				break

def oneCostMinionMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Summon a\n 1 Cost Minion')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranOneMinion = ('')
				ranOneMinion = random.choice(oneCostMinion)
				lcd.message(ranOneMinion)
				break
			if lcd.is_pressed(LCD.UP):
				zeroCostMinionMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				twoCostMinionMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				xCostMinionMenu()
				break

def twoCostMinionMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Summon a\n 2 Cost Minion')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranTwoMinion = ('')
				ranTwoMinion = random.choice(twoCostMinion)
				lcd.message(ranTwoMinion)
				break
			if lcd.is_pressed(LCD.UP):
				oneCostMinionMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				threeCostMinionMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				xCostMinionMenu()
				break

def threeCostMinionMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Summon a\n 3 Cost Minion')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranThreeMinion = ('')
				ranThreeMinion = random.choice(threeCostMinion)
				lcd.message(ranThreeMinion)
				break
			if lcd.is_pressed(LCD.UP):
				twoCostMinionMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				fourCostMinionMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				xCostMinionMenu()
				break

def fourCostMinionMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Summon a\n 4 Cost Minion')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranFourMinion = ('')
				ranFourMinion = random.choice(fourCostMinion)
				lcd.message(ranFourMinion)
				break
			if lcd.is_pressed(LCD.UP):
				threeCostMinionMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				fiveCostMinionMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				xCostMinionMenu()
				break

def fiveCostMinionMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Summon a\n 5 Cost Minion')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranFiveMinion = ('')
				ranFiveMinion = random.choice(fiveCostMinion)
				lcd.message(ranFiveMinion)
				break
			if lcd.is_pressed(LCD.UP):
				fourCostMinionMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				sixCostMinionMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				xCostMinionMenu()
				break

def sixCostMinionMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Summon a\n 6 Cost Minion')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranSixMinion = ('')
				ranSixMinion = random.choice(sixCostMinion)
				lcd.message(ranSixMinion)
				break
			if lcd.is_pressed(LCD.UP):
				fiveCostMinionMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				sevenCostMinionMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				xCostMinionMenu()
				break

def sevenCostMinionMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Summon a\n 7 Cost Minion')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranSevenMinion = ('')
				ranSevenMinion = random.choice(sevenCostMinion)
				lcd.message(ranSevenMinion)
				break
			if lcd.is_pressed(LCD.UP):
				sixCostMinionMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				eightCostMinionMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				xCostMinionMenu()
				break

def eightCostMinionMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('   Summon an\n 8 Cost Minion')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranEightMinion = ('')
				ranEightMinion = random.choice(eightCostMinion)
				lcd.message(ranEightMinion)
				break
			if lcd.is_pressed(LCD.UP):
				sevenCostMinionMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				nineCostMinionMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				xCostMinionMenu()
				break

def nineCostMinionMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Summon a\n 9 Cost Minion')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranNineMinion = ('')
				ranNineMinion = random.choice(nineCostMinion)
				lcd.message(ranNineMinion)
				break
			if lcd.is_pressed(LCD.UP):
				eightCostMinionMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				tenCostMinionMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				xCostMinionMenu()
				break

def tenCostMinionMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Summon a\n 10 Cost Minion')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranTenMinion = ('')
				ranTenMinion = random.choice(tenCostMinion)
				lcd.message(ranTenMinion)
				break
			if lcd.is_pressed(LCD.UP):
				nineCostMinionMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				zeroCostMinionMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				xCostMinionMenu()
				break

# ****** Spells Submenu ******

def allSpellsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Summon a\n  Random Spell')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranSpell = ('')
				ranSpell = random.choice(allSpells)
				lcd.message(ranSpell)
				break
			if lcd.is_pressed(LCD.UP):
				classSpellsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				classSpellsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				spellsMenu()
				break

def classSpellsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Summon a\n Spell by Class')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				druidSpellsMenu()
				break
			if lcd.is_pressed(LCD.UP):
				allSpellsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				allSpellsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				spellsMenu()
				break

def druidSpellsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('Summon a Random\n  Druid Spell')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranDruidSpell = ('')
				ranDruidSpell = random.choice(druidSpells)
				lcd.message(ranDruidSpell)
				break
			if lcd.is_pressed(LCD.UP):
				warriorSpellsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				hunterSpellsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				classSpellsMenu()
				break

def hunterSpellsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('Summon a Random\n  Hunter Spell')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranHunterSpell = ('')
				ranHunterSpell = random.choice(hunterSpells)
				lcd.message(ranHunterSpell)
				break
			if lcd.is_pressed(LCD.UP):
				druidSpellsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				mageSpellsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				classSpellsMenu()
				break

def mageSpellsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('Summon a Random\n  Mage Spell')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranMageSpell = ('')
				ranMageSpell = random.choice(mageSpells)
				lcd.message(ranMageSpell)
				break
			if lcd.is_pressed(LCD.UP):
				hunterSpellsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				paladinSpellsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				classSpellsMenu()
				break

def paladinSpellsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('Summon a Random\n Paladin Spell')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranPaladinSpell = ('')
				ranPaladinSpell = random.choice(paladinSpells)
				lcd.message(ranPaladinSpell)
				break
			if lcd.is_pressed(LCD.UP):
				mageSpellsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				priestSpellsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				classSpellsMenu()
				break

def priestSpellsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('Summon a Random\n  Priest Spell')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranPriestSpell = ('')
				ranPriestSpell = random.choice(priestSpells)
				lcd.message(ranPriestSpell)
				break
			if lcd.is_pressed(LCD.UP):
				paladinSpellsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				rogueSpellsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				classSpellsMenu()
				break

def rogueSpellsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('Summon a Random\n  Rogue Spell')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranRogueSpell = ('')
				ranRogueSpell = random.choice(rogueSpells)
				lcd.message(ranRogueSpell)
				break
			if lcd.is_pressed(LCD.UP):
				priestSpellsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				shamanSpellsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				classSpellsMenu()
				break

def shamanSpellsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('Summon a Random\n  Shaman Spell')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranShamanSpell = ('')
				ranShamanSpell = random.choice(shamanSpells)
				lcd.message(ranShamanSpell)
				break
			if lcd.is_pressed(LCD.UP):
				rogueSpellsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				warlockSpellsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				classSpellsMenu()
				break

def warlockSpellsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('Summon a Random\n Warlock Spell')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranWarlockSpell = ('')
				ranWarlockSpell = random.choice(warlockSpells)
				lcd.message(ranWarlockSpell)
				break
			if lcd.is_pressed(LCD.UP):
				shamanSpellsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				warriorSpellsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				classSpellsMenu()
				break

def warriorSpellsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('Summon a Random\n Warrior Spell')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranWarriorSpell = ('')
				ranWarriorSpell = random.choice(warriorSpells)
				lcd.message(ranWarriorSpell)
				break
			if lcd.is_pressed(LCD.UP):
				warlockSpellsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				druidSpellsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				classSpellsMenu()
				break

# ****** Classes Submenu ******

def druidClassMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Select a\n   Druid Card')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranDruidClass = ('')
				ranDruidClass = random.choice(classDruid)
				lcd.message(ranDruidClass)
				break
			if lcd.is_pressed(LCD.UP):
				warriorClassMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				hunterClassMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				classMenu()
				break

def hunterClassMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Select a\n  Hunter Card')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranHunterClass = ('')
				ranHunterClass = random.choice(classHunter)
				lcd.message(ranHunterClass)
				break
			if lcd.is_pressed(LCD.UP):
				druidClassMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				mageClassMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				classMenu()
				break

def mageClassMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Select a\n   Mage Card')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranMageClass = ('')
				ranMageClass = random.choice(classMage)
				lcd.message(ranMageClass)
				break
			if lcd.is_pressed(LCD.UP):
				hunterClassMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				paladinClassMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				classMenu()
				break

def paladinClassMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Select a\n  Paladin Card')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranPaladinClass = ('')
				ranPaladinClass = random.choice(classPaladin)
				lcd.message(ranPaladinClass)
				break
			if lcd.is_pressed(LCD.UP):
				mageClassMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				priestClassMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				classMenu()
				break

def priestClassMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Select a\n  Priest Card')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranPriestClass = ('')
				ranPriestClass = random.choice(classPriest)
				lcd.message(ranPriestClass)
				break
			if lcd.is_pressed(LCD.UP):
				paladinClassMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				rogueClassMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				classMenu()
				break

def rogueClassMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Select a\n   Rogue Card')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranRogueClass = ('')
				ranRogueClass = random.choice(classRogue)
				lcd.message(ranRogueClass)
				break
			if lcd.is_pressed(LCD.UP):
				priestClassMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				shamanClassMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				classMenu()
				break

def shamanClassMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Select a\n   Shaman Card')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranShamanClass = ('')
				ranShamanClass = random.choice(classShaman)
				lcd.message(ranShamanClass)
				break
			if lcd.is_pressed(LCD.UP):
				rogueClassMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				warlockClassMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				classMenu()
				break

def warriorClassMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Select a\n  Warrior Card')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranWarriorClass = ('')
				ranWarriorClass = random.choice(classWarrior)
				lcd.message(ranWarriorClass)
				break
			if lcd.is_pressed(LCD.UP):
				shamanClassMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				druidClassMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				classMenu()
				break

# ****** Weapons Submenu ******

def allWeaponsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Select a\n Random Weapon')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranWeapon = ('')
				ranWeapon = random.choice(allWeapons)
				lcd.message(ranWeapon)
				break
			if lcd.is_pressed(LCD.UP):
				attackDurMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				attackDurMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				weaponsMenu()
				break

def attackDurMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('Select Weapon by\n    ATK/DUR')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				oneThreeWeaponMenu()
				break
			if lcd.is_pressed(LCD.UP):
				allWeaponsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				allWeaponsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				weaponsMenu()
				break

def oneThreeWeaponMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Select a\n   1/3 Weapon')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranOneThreeWeapon = ('')
				ranOneThreeWeapon = random.choice(oneThreeWeapons)
				lcd.message(ranOneThreeWeapon)
				break
			if lcd.is_pressed(LCD.UP):
				twoTwoWeaponMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				twoTwoWeaponMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				attackDurMenu()
				break

def twoTwoWeaponMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Select a\n   2/2 Weapon')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranTwoTwoWeapon = ('')
				ranTwoTwoWeapon = random.choice(twoTwoWeapons)
				lcd.message(ranTwoTwoWeapon)
				break
			if lcd.is_pressed(LCD.UP):
				oneThreeWeaponMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				oneThreeWeaponMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				attackDurMenu()
				break

# ****** X-Cost Cards Submenu ******

def oneCostMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Select a\n  1 Cost Card')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				sumOneCostCard = ('')
				sumOneCostCard = random.choice(oneCostCard)
				lcd.message(sumOneCostCard)
				break
			if lcd.is_pressed(LCD.UP):
				threeCostMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				threeCostMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				xcostMenu()
				break

def threeCostMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('    Select a\n  3 Cost Card')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				sumThreeCostCard = ('')
				sumThreeCostCard = random.choice(threeCostCard)
				lcd.message(sumThreeCostCard)
				break
			if lcd.is_pressed(LCD.UP):
				oneCostMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				oneCostMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				xcostMenu()
				break

# ****** Other Submenu ******

def heroPowerMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('Select a Random\n   Hero Power')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranHeroPower = ('')
				ranHeroPower = random.choice(heroPowers)
				lcd.message(ranHeroPower)
				break
			if lcd.is_pressed(LCD.UP):
				powerChordsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				sparePartsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				otherMenu()
				break

def sparePartsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('Select a Random\n   Spare Part')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranSparePart = ('')
				ranSparePart = random.choice(spareParts)
				lcd.message(ranSparePart)
				break
			if lcd.is_pressed(LCD.UP):
				heroPowerMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				inventionsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				otherMenu()
				break

def inventionsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('Select a Random\n   Invention')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranInvention = ('')
				ranInvention = random.choice(inventions)
				lcd.message(ranInvention)
				break
			if lcd.is_pressed(LCD.UP):
				sparePartsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				powerChordsMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				otherMenu()
				break

def powerChordsMenu():
	time.sleep(0.2)
	lcd.clear()
	lcd.message('Select a Random\nPower Chord Card')
	while True:
		for button in buttons:
			if lcd.is_pressed(LCD.SELECT):
				lcd.clear()
				ranPowerChord = ('')
				ranPowerChord = random.choice(powerChords)
				lcd.message(ranPowerChord)
				break
			if lcd.is_pressed(LCD.UP):
				inventionsMenu()
				break
			if lcd.is_pressed(LCD.DOWN):
				heroPowerMenu()
				break
			if lcd.is_pressed(LCD.LEFT):
				otherMenu()
				break

# *******************************************************
# Check for button press from title and send to functions
# *******************************************************

while True:
	for button in buttons:
		if lcd.is_pressed(LCD.UP):
			otherMenu()
			break
		if lcd.is_pressed(LCD.DOWN):
			minionsMenu()
			break
