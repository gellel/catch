#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

###########################
### About #################
###########################

__author__ = "Lindsay Gelle (gellel)"

###########################
### Exports ###############
###########################

__all__ = [
	"ABSORB",
	"ACID",
	"ACID_ARMOUR",
	"AGILITY",
	"AMNESIA",
	"AURORA_BEAM",
	"BARRAGE",
	"BARRIER",
	"BIDE",
	"BIND",
	"BITE",
	"BLIZZARD",
	"BODY_SLAM",
	"BONEMERANG",
	"BONE_CLUB",
	"BUBBLE",
	"BUBBLE_BEAM",
	"CLAMP",
	"COMET_PUNCH",
	"CONFUSE_RAY",
	"CONFUSION",
	"CONSTRICT",
	"CONVERSION",
	"COUNTER",
	"CRABHAMMER",
	"CUT",
	"DEFENSE_CURL",
	"DIG",
	"DISABLE",
	"DIZZY_PUNCH",
	"DOUBLE_EDGE",
	"DOUBLE_KICK",
	"DOUBLE_SLAP",
	"DOUBLE_TEAM",
	"DRAGON_RAGE",
	"DREAM_EATER",
	"DRILL_PECK",
	"EARTHQUAKE",
	"EGG_BOMB",
	"EMBER",
	"EXPLOSION",
	"FIRE_BLAST",
	"FIRE_PUNCH",
	"FIRE_SPIN",
	"FISSURE",
	"FLAMETHROWER",
	"FLASH",
	"FLY",
	"FOCUS_ENERGY",
	"FURY_ATTACK",
	"FURY_SWIPES",
	"GLARE",
	"GROWL",
	"GROWTH",
	"GUILLOTINE",
	"GUST",
	"HARDEN",
	"HAZE",
	"HEADBUTT",
	"HORN_ATTACK",
	"HORN_DRILL",
	"HYDRO_PUMP",
	"HYPER_BEAM",
	"HYPER_Fang",
	"HYPNOSIS",
	"ICE_BEAM",
	"ICE_PUNCH",
	"JUMP_KICK",
	"KARATE_CHOP",
	"KINESIS",
	"LEECH_LIFE",
	"LEECH_SEED",
	"LEER",
	"LICK",
	"LIGHT_SCREEN",
	"LOVELY_KISS",
	"LOW_KICK",
	"MEDITATE",
	"MEGA_DRAIN",
	"MEGA_KICK",
	"MEGA_PUNCH",
	"METRONOME",
	"MIMIC",
	"MINIMIZE",
	"MIRROR_MOVE",
	"MIST",
	"NIGHT_SHADE",
	"PAY_DAY",
	"PECK",
	"PETAL_DANCE",
	"PIN_MISSILE",
	"POISON_GAS",
	"POISON_POWDER",
	"POISON_STING",
	"POUND",
	"PSYBEAM",
	"PSYCHIC",
	"PSYWAVE",
	"QUICK_ATTACK",
	"RAGE",
	"RAZOR_LEAF",
	"RAZOR_WIND",
	"RECOVER",
	"REFLECT",
	"REST",
	"ROAR",
	"ROCK_SLIDE",
	"ROCK_THROW",
	"ROLLING_KICK",
	"SAND_ATTACK",
	"SCRATCH",
	"SCREECH",
	"SEISMIC_TOSS",
	"SELF_DESTRUCT",
	"SHARPEN",
	"SING",
	"SKULL_BASH",
	"SKY_ATTACK",
	"SLAM",
	"SLASH",
	"SLEEP_POWDER",
	"SLUDGE",
	"SMOG",
	"SMOKESCREEN",
	"SOFT_BOILED",
	"SOLAR_BEAM",
	"SONIC_BOOM",
	"SPIKE_CANNON",
	"SPLASH",
	"SPORE",
	"STOMP",
	"STRENGTH",
	"STRING_SHOT",
	"STRUGGLE",
	"STUN_SPORE",
	"SUBMISSION",
	"SUBSTITUTE",
	"SUPERSONIC",
	"SUPER_FANG",
	"SURF",
	"SWIFT",
	"SWORDS_DANCE",
	"TACKLE",
	"TAIL_WHIP",
	"TAKE_DOWN",
	"TELEPORT",
	"THRASH",
	"THUNDER",
	"THUNDERBOLT",
	"THUNDER_PUNCH",
	"THUNDER_SHOCK",
	"THUNDER_WAVE",
	"TOXIC",
	"TRANSFORM",
	"TRI_ATTACK",
	"TWINEEDLE",
	"VICE_GRIP",
	"VINE_WHIP",
	"WATERFALL",
	"WATER_GUN",
	"WHIRLWIND",
	"WING_ATTACK",
	"WITHDRAW",
	"WATER"]

###########################
### Constants #############
###########################

ABSORB = dict(
	ELEMENT_TYPE = "GRASS",
	CATEGORY = "SPECIAL",
	POWER = 20,
	ACCURACY = 100,
	POWER_POINTS = 25,
	DESCRIPTION = "USER RECOVERS HALF THE HP INFLICTED ON OPPONENT.")

ACID = dict(
	ELEMENT_TYPE = "POISON",
	CATEGORY = "SPECIAL",
	POWER = 40,
	ACCURACY = 100,
	POWER_POINTS = 30,
	DESCRIPTION = "MAY LOWER OPPONENT'S SPECIAL DEFENSE.")

ACID_ARMOUR = dict(
	ELEMENT_TYPE = "POISON",
	CATEGORY = "STATUS",
	POWER = None, 
	ACCURACY = None,
	POWER_POINTS = 20,
	DESCRIPTION = "SHARPLY RAISES USER'S DEFENSE.")

AGILITY = dict(
	ELEMENT_TYPE = "PSYCHIC",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 30,
	DESCRIPTION = "SHARPLY RAISES USER'S SPEED.")

AMNESIA = dict(
	ELEMENT_TYPE = "PSYCHIC",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 20,
	DESCRIPTION = "SHARPLY RAISES USER'S SPECIAL DEFENSE.")

AURORA_BEAM = dict(
	ELEMENT_TYPE = "ICE",
	CATEGORY = "SPECIAL",
	POWER = 65, 
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "MAY LOWER OPPONENT'S ATTACK.")

BARRAGE = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 15,
	ACCURACY = 85,
	POWER_POINTS = 20,
	DESCRIPTION = "HITS 2-5 TIMES IN ONE TURN.")

BARRIER = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 20,
	DESCRIPTION = "SHARPLY RAISES USER'S DEFENSE.")

BIDE = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 10,
	DESCRIPTION = "USER TAKES DAMAGE FOR TWO TURNS THEN STRIKES BACK DOUBLE.")

BIND = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 15,
	ACCURACY = 85,
	POWER_POINTS = 20,
	DESCRIPTION = "TRAPS OPPONENT, DAMAGING THEM FOR 4-5 TURNS.")

BITE = dict(
 	ELEMENT_TYPE = "DARK",
	CATEGORY = "PHYSICAL",
	POWER = 60,
	ACCURACY = 100,
	POWER_POINTS = 25,
	DESCRIPTION = "MAY CAUSE FLINCHING.")

BLIZZARD = dict(
 	ELEMENT_TYPE = "ICE",
	CATEGORY = "SPECIAL",
	POWER = 110,
	ACCURACY = 70,
	POWER_POINTS = 5,
	DESCRIPTION = "MAY FREEZE OPPONENT.")

BODY_SLAM = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 85,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "MAY PARALYZE OPPONENT.")

BONE_CLUB = dict(
	ELEMENT_TYPE = "GROUND",
	CATEGORY = "PHYSICAL",
	POWER = 65,
	ACCURACY = 85,
	POWER_POINTS = 20,
	DESCRIPTION = "MAY CAUSE FLINCHING.")

BONEMERANG = dict(
 	ELEMENT_TYPE = "GROUND",
	CATEGORY = "PHYSICAL",
	POWER = 50,
	ACCURACY = 90,
	POWER_POINTS = 10,
	DESCRIPTION = "HITS TWICE IN ONE TURN.")

BUBBLE = dict(
 	ELEMENT_TYPE = "WATER",
	CATEGORY = "SPECIAL",
	POWER = 40,
	ACCURACY = 100,
	POWER_POINTS = 30,
	DESCRIPTION = "MAY LOWER OPPONENT'S SPEED.")

BUBBLE_BEAM = dict(
	ELEMENT_TYPE = "WATER",
	CATEGORY = "SPECIAL",
	POWER = 65, 
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "MAY LOWER OPPONENT'S SPEED.")

CLAMP = dict(
 	ELEMENT_TYPE = "WATER",
	CATEGORY = "PHYSICAL",
	POWER = 35,
	ACCURACY = 85,
	POWER_POINTS = 10,
	DESCRIPTION = "TRAPS OPPONENT, DAMAGING THEM FOR 4-5 TURNS.")

COMET_PUNCH = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 18,
	ACCURACY = 85,
	POWER_POINTS = 15,
	DESCRIPTION = "HITS 2-5 TIMES IN ONE TURN.")

CONFUSE_RAY = dict(
	ELEMENT_TYPE = "GHOST",
	CATEGORY = "STATUS",
	POWER = None, 
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "CONFUSES OPPONENT.")

CONFUSION = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	CATEGORY = "SPECIAL",
	POWER = 50,
	ACCURACY = 100,
	POWER_POINTS = 25,
	DESCRIPTION = "MAY CONFUSE OPPONENT.")

CONSTRICT = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 10,
	ACCURACY = 100,
	POWER_POINTS = 35,
	DESCRIPTION = "MAY LOWER OPPONENT'S SPEED BY ONE STAGE.")

CONVERSION = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 30,
	DESCRIPTION = "CHANGES USER'S TYPE TO THAT OF ITS FIRST MOVE.")

COUNTER = dict(
 	ELEMENT_TYPE = "FIGHTING",
	CATEGORY = "PHYSICAL",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "WHEN HIT BY A PHYSICAL ATTACK, USER STRIKES BACK WITH 2X POWER.")

CRABHAMMER = dict(
 	ELEMENT_TYPE = "WATER",
	CATEGORY = "PHYSICAL",
	POWER = 100,
	ACCURACY = 90,
	POWER_POINTS = 10,
	DESCRIPTION = "HIGH CRITICAL HIT RATIO.")

CUT = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 50,
	ACCURACY = 95,
	POWER_POINTS = 30,
	DESCRIPTION = None)

DEFENSE_CURL = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None, 
	ACCURACY = None,
	POWER_POINTS = 40,
	DESCRIPTION = "RAISES USER'S DEFENSE.")

DIG = dict(
 	ELEMENT_TYPE = "GROUND",
	CATEGORY = "PHYSICAL",
	POWER = 80,
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "DIGS UNDERGROUND ON FIRST TURN, ATTACKS ON SECOND. CAN ALSO ESCAPE FROM CAVES.")

DISABLE = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "OPPONENT CAN'T USE ITS LAST ATTACK FOR A FEW TURNS.")

DIZZY_PUNCH = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 70,
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "MAY CONFUSE OPPONENT.")

DOUBLE_KICK = dict(
	ELEMENT_TYPE = "FIGHTING",
	CATEGORY = "PHYSICAL",
	POWER = 30,
	ACCURACY = 100,
	POWER_POINTS = 30,
	DESCRIPTION = "HITS TWICE IN ONE TURN.")

DOUBLE_SLAP = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 15,
	ACCURACY = 85,
	POWER_POINTS = 10,
	DESCRIPTION = "HITS 2-5 TIMES IN ONE TURN.")

DOUBLE_TEAM = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None, 
	ACCURACY = None,
	POWER_POINTS = 15,
	DESCRIPTION = "RAISES USER'S EVASIVENESS.")

DOUBLE_EDGE = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 120, 
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "USER RECEIVES RECOIL DAMAGE.")

DRAGON_RAGE = dict(
	ELEMENT_TYPE = "DRAGON",
	CATEGORY = "SPECIAL",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "ALWAYS INFLICTS 40 HP.")

DREAM_EATER = dict(
	ELEMENT_TYPE = "PSYCHIC",
	CATEGORY = "SPECIAL",
	POWER = 100,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "USER RECOVERS HALF THE HP INFLICTED ON A SLEEPING OPPONENT.")

DRILL_PECK = dict(
	ELEMENT_TYPE = "FLYING",
	CATEGORY = "PHYSICAL",
	POWER = 80,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = None)

EARTHQUAKE = dict(
 	ELEMENT_TYPE = "GROUND",
	CATEGORY = "PHYSICAL",
	POWER = 100,
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "POWER IS DOUBLED IF OPPONENT IS UNDERGROUND FROM USING DIG.")

EGG_BOMB = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 100, 
	ACCURACY = 75,
	POWER_POINTS = 10,
	DESCRIPTION = None)

EMBER = dict(
 	ELEMENT_TYPE = "FIRE",
	CATEGORY = "SPECIAL",
	POWER = 40,
	ACCURACY = 100,
	POWER_POINTS = 25,
	DESCRIPTION = "MAY BURN OPPONENT.")

EXPLOSION = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 250,
	ACCURACY = 100,
	POWER_POINTS = 5,
	DESCRIPTION = "USER FAINTS.")

FIRE_BLAST = dict(
	ELEMENT_TYPE = "FIRE",
	CATEGORY = "SPECIAL",
	POWER = 110, 
	ACCURACY = 85,
	POWER_POINTS = 5,
	DESCRIPTION = "MAY BURN OPPONENT.")

FIRE_PUNCH = dict(
	ELEMENT_TYPE = "FIRE",
	CATEGORY = "PHYSICAL",
	POWER = 75,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "MAY BURN OPPONENT.")

FIRE_SPIN = dict(
	ELEMENT_TYPE = "FIRE",
	CATEGORY = "SPECIAL",
	POWER = 35, 
	ACCURACY = 85,
	POWER_POINTS = 15,
	DESCRIPTION = "TRAPS OPPONENT, DAMAGING THEM FOR 4-5 TURNS.")

FISSURE = dict(
 	ELEMENT_TYPE = "GROUND",
	CATEGORY = "PHYSICAL",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 5,
	DESCRIPTION = "ONE-HIT-KO, IF IT HITS.")

FLAMETHROWER = dict(
 	ELEMENT_TYPE = "FIRE",
	CATEGORY = "SPECIAL",
	POWER = 90,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "MAY BURN OPPONENT.")

FLASH = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "LOWERS OPPONENT'S ACCURACY.")

FLY = dict(
 	ELEMENT_TYPE = "FLYING",
	CATEGORY = "PHYSICAL",
	POWER = 90,
	ACCURACY = 95,
	POWER_POINTS = 15,
	DESCRIPTION = "FLIES UP ON FIRST TURN, ATTACKS ON SECOND TURN.")

FOCUS_ENERGY = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None, 
	ACCURACY = None,
	POWER_POINTS = 30,
	DESCRIPTION = "INCREASES CRITICAL HIT RATIO.")

FURY_ATTACK = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 15,
	ACCURACY = 85,
	POWER_POINTS = 20,
	DESCRIPTION = "HITS 2-5 TIMES IN ONE TURN.")

FURY_SWIPES = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 18,
	ACCURACY = 80,
	POWER_POINTS = 15,
	DESCRIPTION = "HITS 2-5 TIMES IN ONE TURN.")

GLARE = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 30,
	DESCRIPTION = "PARALYZES OPPONENT.")

GROWL = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 40,
	DESCRIPTION = "LOWERS OPPONENT'S ATTACK.")

GROWTH = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 40,
	DESCRIPTION = "RAISES USER'S ATTACK AND SPECIAL ATTACK.")

GUILLOTINE = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 5,
	DESCRIPTION = "ONE-HIT-KO, IF IT HITS.")

GUST = dict(
 	ELEMENT_TYPE = "FLYING",
	CATEGORY = "SPECIAL",
	POWER = 40,
	ACCURACY = 100,
	POWER_POINTS = 35,
	DESCRIPTION = "HITS POKEMON USING FLY/BOUNCE WITH DOUBLE POWER.")

HARDEN = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 30,
	DESCRIPTION = "RAISES USER'S DEFENSE.")

HAZE = dict(
 	ELEMENT_TYPE = "ICE",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 30,
	DESCRIPTION = "RESETS ALL STAT CHANGES.")

HEADBUTT = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 70,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "MAY CAUSE FLINCHING.")

HIGH_JUMP_KICK = dict(
	ELEMENT_TYPE = "FIGHTING",
	CATEGORY = "PHYSICAL",
	POWER = 130, 
	ACCURACY = 90,
	POWER_POINTS = 10,
	DESCRIPTION = "IF IT MISSES, THE USER LOSES HALF THEIR HP.")

HORN_ATTACK = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 65,
	ACCURACY = 100,
	POWER_POINTS = 25,
	DESCRIPTION = None)

HORN_DRILL = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 5,
	DESCRIPTION = "ONE-HIT-KO, IF IT HITS.")

HYDRO_PUMP = dict(
	ELEMENT_TYPE = "WATER",
	CATEGORY = "SPECIAL",
	POWER = 110, 
	ACCURACY = 80,
	POWER_POINTS = 5,
	DESCRIPTION = None)

HYPER_BEAM = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "SPECIAL",
	POWER = 150, 
	ACCURACY = 90,
	POWER_POINTS = 5,
	DESCRIPTION = "USER MUST RECHARGE NEXT TURN.")

HYPER_FANG = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 80,
	ACCURACY = 90,
	POWER_POINTS = 15,
	DESCRIPTION = "MAY CAUSE FLINCHING.")

HYPNOSIS = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = 60,
	POWER_POINTS = 20,
	DESCRIPTION = "PUTS OPPONENT TO SLEEP.")

ICE_BEAM = dict(
	ELEMENT_TYPE = "ICE",
	CATEGORY = "SPECIAL",
	POWER = 90, 
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "MAY FREEZE OPPONENT.")

ICE_PUNCH = dict(
	ELEMENT_TYPE = "ICE",
	CATEGORY = "PHYSICAL",
	POWER = 75,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "MAY FREEZE OPPONENT.")

JUMP_KICK = dict(
	ELEMENT_TYPE = "FIGHTING",
	CATEGORY = "PHYSICAL",
	POWER = 100, 
	ACCURACY = 95,
	POWER_POINTS = 10,
	DESCRIPTION = "IF IT MISSES, THE USER LOSES HALF THEIR HP.")

KARATE_CHOP = dict(
	ELEMENT_TYPE = "FIGHTING",
	CATEGORY = "PHYSICAL",
	POWER = 50,
	ACCURACY = 100,
	POWER_POINTS = 25,
	DESCRIPTION = "HIGH CRITICAL HIT RATIO.")

KINESIS = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = 80,
	POWER_POINTS = 15,
	DESCRIPTION = "LOWERS OPPONENT'S ACCURACY.")

LEECH_LIFE = dict(
	ELEMENT_TYPE = "BUG",
	CATEGORY = "PHYSICAL",
	POWER = 80,
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "USER RECOVERS HALF THE HP INFLICTED ON OPPONENT.")

LEECH_SEED = dict(
	ELEMENT_TYPE = "GRASS",
	CATEGORY = "STATUS",
	POWER = None, 
	ACCURACY = 90,
	POWER_POINTS = 10,
	DESCRIPTION = "USER STEALS HP FROM OPPONENT EACH TURN.")

LEER = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 30,
	DESCRIPTION = "LOWERS OPPONENT'S DEFENSE.")

LICK = dict(
 	ELEMENT_TYPE = "GHOST",
	CATEGORY = "PHYSICAL",
	POWER = 30,
	ACCURACY = 100,
	POWER_POINTS = 30,
	DESCRIPTION = "MAY PARALYZE OPPONENT.")

LIGHT_SCREEN = dict(
	ELEMENT_TYPE = "PSYCHIC",
	CATEGORY = "STATUS",
	POWER = None, 
	ACCURACY = None,
	POWER_POINTS = 30,
	DESCRIPTION = "HALVES DAMAGE FROM SPECIAL ATTACKS FOR 5 TURNS.")

LOVELY_KISS = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None, 
	ACCURACY = 75,
	POWER_POINTS = 10,
	DESCRIPTION = "PUTS OPPONENT TO SLEEP.")

LOW_KICK = dict(
	ELEMENT_TYPE = "FIGHTING",
	CATEGORY = "PHYSICAL",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "THE HEAVIER THE OPPONENT, THE STRONGER THE ATTACK.")

MEDITATE = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 40,
	DESCRIPTION = "RAISES USER'S ATTACK.")

MEGA_DRAIN = dict(
	ELEMENT_TYPE = "GRASS",
	CATEGORY = "SPECIAL",
	POWER = 40, 
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "USER RECOVERS HALF THE HP INFLICTED ON OPPONENT.")

MEGA_KICK = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 120, 
	ACCURACY = 75,
	POWER_POINTS = 5,
	DESCRIPTION = None)

MEGA_PUNCH = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 80,
	ACCURACY = 85,
	POWER_POINTS = 20,
	DESCRIPTION = None)

METRONOME = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 10,
	DESCRIPTION = "USER PERFORMS ANY MOVE IN THE GAME AT RANDOM.")

MIMIC = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 10,
	DESCRIPTION = "COPIES THE OPPONENT'S LAST MOVE.")

MINIMIZE = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 10,
	DESCRIPTION = "SHARPLY RAISES USER'S EVASIVENESS.")

MIRROR_MOVE = dict(
	ELEMENT_TYPE = "FLYING",
	CATEGORY = "STATUS",
	POWER = None, 
	ACCURACY = None,
	POWER_POINTS = 20,
	DESCRIPTION = "USER PERFORMS THE OPPONENT'S LAST MOVE.")

MIST = dict(
 	ELEMENT_TYPE = "ICE",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 30,
	DESCRIPTION = "USER'S STATS CANNOT BE CHANGED FOR A PERIOD OF TIME.")

NIGHT_SHADE = dict(
	ELEMENT_TYPE = "GHOST",
	CATEGORY = "SPECIAL",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "INFLICTS DAMAGE EQUAL TO USER'S LEVEL.")

PAY_DAY = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 40,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "A SMALL AMOUNT OF MONEY IS GAINED AFTER THE BATTLE RESOLVES.")

PECK = dict(
 	ELEMENT_TYPE = "FLYING",
	CATEGORY = "PHYSICAL",
	POWER = 35,
	ACCURACY = 100,
	POWER_POINTS = 35,
	DESCRIPTION = None)

PETAL_DANCE = dict(
	ELEMENT_TYPE = "GRASS",
	CATEGORY = "SPECIAL",
	POWER = 120, 
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "USER ATTACKS FOR 2-3 TURNS BUT THEN BECOMES CONFUSED.")

PIN_MISSILE = dict(
	ELEMENT_TYPE = "BUG",
	CATEGORY = "PHYSICAL",
	POWER = 25,
	ACCURACY = 95,
	POWER_POINTS = 20,
	DESCRIPTION = "HITS 2-5 TIMES IN ONE TURN.")

POISON_GAS = dict(
	ELEMENT_TYPE = "POISON",
	CATEGORY = "STATUS",
	POWER = None, 
	ACCURACY = 90,
	POWER_POINTS = 40,
	DESCRIPTION = "POISONS OPPONENT.")

POISON_POWDER = dict(
	ELEMENT_TYPE = "POISON",
	CATEGORY = "STATUS",
	POWER = None, 
	ACCURACY = 75,
	POWER_POINTS = 35,
	DESCRIPTION = "POISONS OPPONENT.")

POISON_STING = dict(
	ELEMENT_TYPE = "POISON",
	CATEGORY = "PHYSICAL",
	POWER = 15,
	ACCURACY = 100,
	POWER_POINTS = 35,
	DESCRIPTION = "MAY POISON THE OPPONENT.")

POUND = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 40,
	ACCURACY = 100,
	POWER_POINTS = 35,
	DESCRIPTION = None)

PSYBEAM = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	CATEGORY = "SPECIAL",
	POWER = 65,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "MAY CONFUSE OPPONENT.")

PSYCHIC = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	CATEGORY = "SPECIAL",
	POWER = 90,
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "MAY LOWER OPPONENT'S SPECIAL DEFENSE.")

PSYWAVE = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	CATEGORY = "SPECIAL",
	POWER = None,
	ACCURACY = 80,
	POWER_POINTS = 15,
	DESCRIPTION = "INFLICTS DAMAGE 50-150% OF USER'S LEVEL.")

QUICK_ATTACK = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 40,
	ACCURACY = 100,
	POWER_POINTS = 30,
	DESCRIPTION = "USER ATTACKS FIRST.")

RAGE = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 20,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "RAISES USER'S ATTACK WHEN HIT.")

RAZOR_LEAF = dict(
	ELEMENT_TYPE = "GRASS",
	CATEGORY = "PHYSICAL",
	POWER = 55,
	ACCURACY = 95,
	POWER_POINTS = 25,
	DESCRIPTION = "HIGH CRITICAL HIT RATIO.")

RAZOR_WIND = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "SPECIAL",
	POWER = 80, 
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "CHARGES ON FIRST TURN, ATTACKS ON SECOND. HIGH CRITICAL HIT RATIO.")

RECOVER = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 10,
	DESCRIPTION = "USER RECOVERS HALF ITS MAX HP.")

REFLECT = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 20,
	DESCRIPTION = "HALVES DAMAGE FROM PHYSICAL ATTACKS FOR 5 TURNS.")

REST = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 10,
	DESCRIPTION = "USER SLEEPS FOR 2 TURNS, BUT USER IS FULLY HEALED.")

ROAR = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 20,
	DESCRIPTION = "IN BATTLES, THE OPPONENT SWITCHES. IN THE WILD, THE POKEMON RUNS.")

ROCK_SLIDE = dict(
	ELEMENT_TYPE = "ROCK",
	CATEGORY = "PHYSICAL",
	POWER = 75,
	ACCURACY = 90,
	POWER_POINTS = 10,
	DESCRIPTION = "MAY CAUSE FLINCHING.")

ROCK_THROW = dict(
	ELEMENT_TYPE = "ROCK",
	CATEGORY = "PHYSICAL",
	POWER = 50,
	ACCURACY = 90,
	POWER_POINTS = 15,
	DESCRIPTION = None)

ROLLING_KICK = dict(
	ELEMENT_TYPE = "FIGHTING",
	CATEGORY = "PHYSICAL",
	POWER = 60,
	ACCURACY = 85,
	POWER_POINTS = 15,
	DESCRIPTION = "MAY CAUSE FLINCHING.")

SAND_ATTACK = dict(
	ELEMENT_TYPE = "GROUND",
	CATEGORY = "STATUS",
	POWER = None, 
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "LOWERS OPPONENT'S ACCURACY.")

SCRATCH = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 40,
	ACCURACY = 100,
	POWER_POINTS = 35,
	DESCRIPTION = None)

SCREECH = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = 85,
	POWER_POINTS = 40,
	DESCRIPTION = "SHARPLY LOWERS OPPONENT'S DEFENSE.")

SEISMIC_TOSS = dict(
	ELEMENT_TYPE = "FIGHTING",
	CATEGORY = "PHYSICAL",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "INFLICTS DAMAGE EQUAL TO USER'S LEVEL.")

SELF_DESTRUCT = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 200, 
	ACCURACY = 100,
	POWER_POINTS = 5,
	DESCRIPTION = "USER FAINTS.")

SHARPEN = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 30,
	DESCRIPTION = "RAISES USER'S ATTACK.")

SING = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = 55,
	POWER_POINTS = 15,
	DESCRIPTION = "PUTS OPPONENT TO SLEEP.")

SKULL_BASH = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 130, 
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "RAISES DEFENSE ON FIRST TURN, ATTACKS ON SECOND.")

SKY_ATTACK = dict(
	ELEMENT_TYPE = "FLYING",
	CATEGORY = "PHYSICAL",
	POWER = 140, 
	ACCURACY = 90,
	POWER_POINTS = 5,
	DESCRIPTION = "CHARGES ON FIRST TURN, ATTACKS ON SECOND. MAY CAUSE FLINCHING.")

SLAM = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 80,
	ACCURACY = 75,
	POWER_POINTS = 20,
	DESCRIPTION = None)

SLASH = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 70,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "HIGH CRITICAL HIT RATIO.")

SLEEP_POWDER = dict(
	ELEMENT_TYPE = "GRASS",
	CATEGORY = "STATUS",
	POWER = None, 
	ACCURACY = 75,
	POWER_POINTS = 15,
	DESCRIPTION = "PUTS OPPONENT TO SLEEP.")

SLUDGE = dict(
 	ELEMENT_TYPE = "POISON",
	CATEGORY = "SPECIAL",
	POWER = 65,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "MAY POISON OPPONENT.")

SMOG = dict(
 	ELEMENT_TYPE = "POISON",
	CATEGORY = "SPECIAL",
	POWER = 30,
	ACCURACY = 70,
	POWER_POINTS = 20,
	DESCRIPTION = "MAY POISON OPPONENT.")

SMOKESCREEN = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "LOWERS OPPONENT'S ACCURACY.")

SOFT_BOILED = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None, 
	ACCURACY = None,
	POWER_POINTS = 10,
	DESCRIPTION = "USER RECOVERS HALF ITS MAX HP.")

SOLAR_BEAM = dict(
	ELEMENT_TYPE = "GRASS",
	CATEGORY = "SPECIAL",
	POWER = 120, 
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "CHARGES ON FIRST TURN, ATTACKS ON SECOND.")

SONIC_BOOM = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "SPECIAL",
	POWER = None,
	ACCURACY = 90,
	POWER_POINTS = 20,
	DESCRIPTION = "ALWAYS INFLICTS 20 HP.")

SPIKE_CANNON = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 20,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "HITS 2-5 TIMES IN ONE TURN.")

SPLASH = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 40,
	DESCRIPTION = "DOESN'T DO ANYTHING.")

SPORE = dict(
 	ELEMENT_TYPE = "GRASS",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "PUTS OPPONENT TO SLEEP.")

STOMP = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 65,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "MAY CAUSE FLINCHING.")

STRENGTH = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 80,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = None)

STRING_SHOT = dict(
	ELEMENT_TYPE = "BUG",
	CATEGORY = "STATUS",
	POWER = None, 
	ACCURACY = 95,
	POWER_POINTS = 40,
	DESCRIPTION = "SHARPLY LOWERS OPPONENT'S SPEED.")

STRUGGLE = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 50,
	ACCURACY = 100,
	POWER_POINTS = None,
	DESCRIPTION = "ONLY USABLE WHEN ALL PP ARE GONE. HURTS THE USER.")

STUN_SPORE = dict(
	ELEMENT_TYPE = "GRASS",
	CATEGORY = "STATUS",
	POWER = None, 
	ACCURACY = 75,
	POWER_POINTS = 30,
	DESCRIPTION = "PARALYZES OPPONENT.")

SUBMISSION = dict(
 	ELEMENT_TYPE = "FIGHTING",
	CATEGORY = "PHYSICAL",
	POWER = 80,
	ACCURACY = 80,
	POWER_POINTS = 20,
	DESCRIPTION = "USER RECEIVES RECOIL DAMAGE.")

SUBSTITUTE = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 10,
	DESCRIPTION = "USES HP TO CREATES A DECOY THAT TAKES HITS.")

SUPER_FANG = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = None,
	ACCURACY = 90,
	POWER_POINTS = 10,
	DESCRIPTION = "ALWAYS TAKES OFF HALF OF THE OPPONENT'S HP.")

SUPERSONIC = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = 55,
	POWER_POINTS = 20,
	DESCRIPTION = "CONFUSES OPPONENT.")

SURF = dict(
 	ELEMENT_TYPE = "WATER",
	CATEGORY = "SPECIAL",
	POWER = 90,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "HITS ALL ADJACENT POKEMON.")

SWIFT = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "SPECIAL",
	POWER = 60,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "IGNORES ACCURACY AND EVASIVENESS.")

SWORDS_DANCE = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None, 
	ACCURACY = None,
	POWER_POINTS = 20,
	DESCRIPTION = "SHARPLY RAISES USER'S ATTACK.")

TACKLE = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 40,
	ACCURACY = 100,
	POWER_POINTS = 35,
	DESCRIPTION = None)

TAIL_WHIP = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None, 
	ACCURACY = 100,
	POWER_POINTS = 30,
	DESCRIPTION = "LOWERS OPPONENT'S DEFENSE.")

TAKE_DOWN = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 90,
	ACCURACY = 85,
	POWER_POINTS = 20,
	DESCRIPTION = "USER RECEIVES RECOIL DAMAGE.")

TELEPORT = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 20,
	DESCRIPTION = "ALLOWS USER TO FLEE WILD BATTLES; ALSO WARPS PLAYER TO LAST POKECENTER.")

THRASH = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 120,
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "USER ATTACKS FOR 2-3 TURNS BUT THEN BECOMES CONFUSED.")

THUNDER = dict(
 	ELEMENT_TYPE = "ELECTRIC",
	CATEGORY = "SPECIAL",
	POWER = 110,
	ACCURACY = 70,
	POWER_POINTS = 10,
	DESCRIPTION = "MAY PARALYZE OPPONENT.")

THUNDER_PUNCH = dict(
	ELEMENT_TYPE = "ELECTRIC",
	CATEGORY = "PHYSICAL",
	POWER = 75,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "MAY PARALYZE OPPONENT.")

THUNDER_SHOCK = dict(
	ELEMENT_TYPE = "ELECTRIC",
	CATEGORY = "SPECIAL",
	POWER = 40, 
	ACCURACY = 100,
	POWER_POINTS = 30,
	DESCRIPTION = "MAY PARALYZE OPPONENT.")

THUNDER_WAVE = dict(
	ELEMENT_TYPE = "ELECTRIC",
	CATEGORY = "STATUS",
	POWER = None, 
	ACCURACY = 90,
	POWER_POINTS = 20,
	DESCRIPTION = "PARALYZES OPPONENT.")

THUNDERBOLT = dict(
 	ELEMENT_TYPE = "ELECTRIC",
	CATEGORY = "SPECIAL",
	POWER = 90,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "MAY PARALYZE OPPONENT.")

TOXIC = dict(
 	ELEMENT_TYPE = "POISON",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = 90,
	POWER_POINTS = 10,
	DESCRIPTION = "BADLY POISONS OPPONENT.")

TRANSFORM = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 10,
	DESCRIPTION = "USER TAKES ON THE FORM AND ATTACKS OF THE OPPONENT.")

TRI_ATTACK = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "SPECIAL",
	POWER = 80, 
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "MAY PARALYZE, BURN OR FREEZE OPPONENT.")

TWINEEDLE = dict(
 	ELEMENT_TYPE = "BUG",
	CATEGORY = "PHYSICAL",
	POWER = 25,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "HITS TWICE IN ONE TURN. MAY POISON OPPONENT.")

VICE_GRIP = dict(
	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 55,
	ACCURACY = 100,
	POWER_POINTS = 30,
	DESCRIPTION = None)

VINE_WHIP = dict(
	ELEMENT_TYPE = "GRASS",
	CATEGORY = "PHYSICAL",
	POWER = 45,
	ACCURACY = 100,
	POWER_POINTS = 25,
	DESCRIPTION = None)

WATER_GUN = dict(
	ELEMENT_TYPE = "WATER",
	CATEGORY = "SPECIAL",
	POWER = 40, 
	ACCURACY = 100,
	POWER_POINTS = 25,
	DESCRIPTION = None)

WATERFALL = dict(
 	ELEMENT_TYPE = "WATER",
	CATEGORY = "PHYSICAL",
	POWER = 80,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "MAY CAUSE FLINCHING.")

WHIRLWIND = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 20,
	DESCRIPTION = "IN BATTLES, THE OPPONENT SWITCHES. IN THE WILD, THE POKEMON RUNS.")

WING_ATTACK = dict(
	ELEMENT_TYPE = "FLYING",
	CATEGORY = "PHYSICAL",
	POWER = 60,
	ACCURACY = 100,
	POWER_POINTS = 35,
	DESCRIPTION = None)

WITHDRAW = dict(
 	ELEMENT_TYPE = "WATER",
	CATEGORY = "STATUS",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 40,
	DESCRIPTION = "RAISES USER'S DEFENSE.")

WRAP = dict(
 	ELEMENT_TYPE = "NORMAL",
	CATEGORY = "PHYSICAL",
	POWER = 15,
	ACCURACY = 90,
	POWER_POINTS = 20,
	DESCRIPTION = "TRAPS OPPONENT, DAMAGING THEM FOR 4-5 TURNS.")
