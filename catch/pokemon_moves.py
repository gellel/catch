#!/usr/bin/env python3

# -*- coding: utf-8 -*- 

# from collections import named tuple module.
from collections import namedtuple
# import random module
import random
# import regex module
import re
# import system module
import sys
# import pokemon types module
import pokemon_types

########################
### File information ###
########################

__author__  = "Lindsay Gelle (https://github.com/gellel)"

__version__ = "1.0"

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

########################
### Module constants ###
########################

ABSORB = dict(
	ELEMENT_TYPE = "GRASS",
	ATTRIBUTES = pokemon_types.GRASS,
	CATEGORY = "Special",
	POWER = 20,
	ACCURACY = 100,
	POWER_POINTS = 25,
	DESCRIPTION = "User recovers half the HP inflicted on opponent.")

ACID = dict(
	ELEMENT_TYPE = "POISON",
	ATTRIBUTES = pokemon_types.POISON,
	CATEGORY = "Special",
	POWER = 40,
	ACCURACY = 100,
	POWER_POINTS = 30,
	DESCRIPTION = "May lower opponent's Special Defense.")

ACID_ARMOUR = dict(
	ELEMENT_TYPE = "POISON",
	ATTRIBUTES = pokemon_types.POISON,
	CATEGORY = "Status",
	POWER = None, 
	ACCURACY = None,
	POWER_POINTS = 20,
	DESCRIPTION = "Sharply raises user's Defense.")

AGILITY = dict(
	ELEMENT_TYPE = "PSYCHIC",
	ATTRIBUTES = pokemon_types.PSYCHIC,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 30,
	DESCRIPTION = "Sharply raises user's Speed.")

AMNESIA = dict(
	ELEMENT_TYPE = "PSYCHIC",
	ATTRIBUTES = pokemon_types.PSYCHIC,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 20,
	DESCRIPTION = "Sharply raises user's Special Defense.")

AURORA_BEAM = dict(
	ELEMENT_TYPE = "ICE",
	ATTRIBUTES = pokemon_types.ICE,
	CATEGORY = "Special",
	POWER = 65, 
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "May lower opponent's Attack.")

BARRAGE = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 15,
	ACCURACY = 85,
	POWER_POINTS = 20,
	DESCRIPTION = "Hits 2-5 times in one turn.")

BARRIER = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	ATTRIBUTES = pokemon_types.PSYCHIC,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 20,
	DESCRIPTION = "Sharply raises user's Defense.")

BIDE = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 10,
	DESCRIPTION = "User takes damage for two turns then strikes back double.")

BIND = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 15,
	ACCURACY = 85,
	POWER_POINTS = 20,
	DESCRIPTION = "Traps opponent, damaging them for 4-5 turns.")

BITE = dict(
 	ELEMENT_TYPE = "DARK",
	ATTRIBUTES = pokemon_types.DARK,
	CATEGORY = "Physical",
	POWER = 60,
	ACCURACY = 100,
	POWER_POINTS = 25,
	DESCRIPTION = "May cause flinching.")

BLIZZARD = dict(
 	ELEMENT_TYPE = "ICE",
	ATTRIBUTES = pokemon_types.ICE,
	CATEGORY = "Special",
	POWER = 110,
	ACCURACY = 70,
	POWER_POINTS = 5,
	DESCRIPTION = "May freeze opponent.")

BODY_SLAM = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 85,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "May paralyze opponent.")

BONE_CLUB = dict(
	ELEMENT_TYPE = "GROUND",
	ATTRIBUTES = pokemon_types.GROUND,
	CATEGORY = "Physical",
	POWER = 65,
	ACCURACY = 85,
	POWER_POINTS = 20,
	DESCRIPTION = "May cause flinching.")

BONEMERANG = dict(
 	ELEMENT_TYPE = "GROUND",
	ATTRIBUTES = pokemon_types.GROUND,
	CATEGORY = "Physical",
	POWER = 50,
	ACCURACY = 90,
	POWER_POINTS = 10,
	DESCRIPTION = "Hits twice in one turn.")

BUBBLE = dict(
 	ELEMENT_TYPE = "WATER",
	ATTRIBUTES = pokemon_types.WATER,
	CATEGORY = "Special",
	POWER = 40,
	ACCURACY = 100,
	POWER_POINTS = 30,
	DESCRIPTION = "May lower opponent's Speed.")

BUBBLE_BEAM = dict(
	ELEMENT_TYPE = "WATER",
	ATTRIBUTES = pokemon_types.WATER,
	CATEGORY = "Special",
	POWER = 65, 
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "May lower opponent's Speed.")

CLAMP = dict(
 	ELEMENT_TYPE = "WATER",
	ATTRIBUTES = pokemon_types.WATER,
	CATEGORY = "Physical",
	POWER = 35,
	ACCURACY = 85,
	POWER_POINTS = 10,
	DESCRIPTION = "Traps opponent, damaging them for 4-5 turns.")

COMET_PUNCH = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 18,
	ACCURACY = 85,
	POWER_POINTS = 15,
	DESCRIPTION = "Hits 2-5 times in one turn.")

CONFUSE_RAY = dict(
	ELEMENT_TYPE = "GHOST",
	ATTRIBUTES = pokemon_types.GHOST,
	CATEGORY = "Status",
	POWER = None, 
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "Confuses opponent.")

CONFUSION = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	ATTRIBUTES = pokemon_types.PSYCHIC,
	CATEGORY = "Special",
	POWER = 50,
	ACCURACY = 100,
	POWER_POINTS = 25,
	DESCRIPTION = "May confuse opponent.")

CONSTRICT = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 10,
	ACCURACY = 100,
	POWER_POINTS = 35,
	DESCRIPTION = "May lower opponent's Speed by one stage.")

CONVERSION = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 30,
	DESCRIPTION = "Changes user's type to that of its first move.")

COUNTER = dict(
 	ELEMENT_TYPE = "FIGHTING",
	ATTRIBUTES = pokemon_types.FIGHTING,
	CATEGORY = "Physical",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "When hit by a Physical Attack, user strikes back with 2x POWER.")

CRABHAMMER = dict(
 	ELEMENT_TYPE = "WATER",
	ATTRIBUTES = pokemon_types.WATER,
	CATEGORY = "Physical",
	POWER = 100,
	ACCURACY = 90,
	POWER_POINTS = 10,
	DESCRIPTION = "High critical hit ratio.")

CUT = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 50,
	ACCURACY = 95,
	POWER_POINTS = 30,
	DESCRIPTION = "")

DEFENSE_CURL = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None, 
	ACCURACY = None,
	POWER_POINTS = 40,
	DESCRIPTION = "Raises user's Defense.")

DIG = dict(
 	ELEMENT_TYPE = "GROUND",
	ATTRIBUTES = pokemon_types.GROUND,
	CATEGORY = "Physical",
	POWER = 80,
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "Digs underground on first turn, attacks on second. Can also escape from caves.")

DISABLE = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "Opponent can't use its last attack for a few turns.")

DIZZY_PUNCH = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 70,
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "May confuse opponent.")

DOUBLE_KICK = dict(
	ELEMENT_TYPE = "FIGHTING",
	ATTRIBUTES = pokemon_types.FIGHTING,
	CATEGORY = "Physical",
	POWER = 30,
	ACCURACY = 100,
	POWER_POINTS = 30,
	DESCRIPTION = "Hits twice in one turn.")

DOUBLE_SLAP = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 15,
	ACCURACY = 85,
	POWER_POINTS = 10,
	DESCRIPTION = "Hits 2-5 times in one turn.")

DOUBLE_TEAM = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None, 
	ACCURACY = None,
	POWER_POINTS = 15,
	DESCRIPTION = "Raises user's Evasiveness.")

DOUBLE_EDGE = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 120, 
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "User receives recoil damage.")

DRAGON_RAGE = dict(
	ELEMENT_TYPE = "Dragon",
	ATTRIBUTES = pokemon_types.DRAGON,
	CATEGORY = "Special",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "Always inflicts 40 HP.")

DREAM_EATER = dict(
	ELEMENT_TYPE = "PSYCHIC",
	ATTRIBUTES = pokemon_types.PSYCHIC,
	CATEGORY = "Special",
	POWER = 100,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "User recovers half the HP inflicted on a sleeping opponent.")

DRILL_PECK = dict(
	ELEMENT_TYPE = "FLYING",
	ATTRIBUTES = pokemon_types.FLYING,
	CATEGORY = "Physical",
	POWER = 80,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "")

EARTHQUAKE = dict(
 	ELEMENT_TYPE = "GROUND",
	ATTRIBUTES = pokemon_types.GROUND,
	CATEGORY = "Physical",
	POWER = 100,
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "POWER is doubled if opponent is underground from using Dig.")

EGG_BOMB = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 100, 
	ACCURACY = 75,
	POWER_POINTS = 10,
	DESCRIPTION = "")

EMBER = dict(
 	ELEMENT_TYPE = "FIRE",
	ATTRIBUTES = pokemon_types.FIRE,
	CATEGORY = "Special",
	POWER = 40,
	ACCURACY = 100,
	POWER_POINTS = 25,
	DESCRIPTION = "May burn opponent.")

EXPLOSION = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 250,
	ACCURACY = 100,
	POWER_POINTS = 5,
	DESCRIPTION = "User faints.")

FIRE_BLAST = dict(
	ELEMENT_TYPE = "FIRE",
	ATTRIBUTES = pokemon_types.FIRE,
	CATEGORY = "Special",
	POWER = 110, 
	ACCURACY = 85,
	POWER_POINTS = 5,
	DESCRIPTION = "May burn opponent.")

FIRE_PUNCH = dict(
	ELEMENT_TYPE = "FIRE",
	ATTRIBUTES = pokemon_types.FIRE,
	CATEGORY = "Physical",
	POWER = 75,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "May burn opponent.")

FIRE_SPIN = dict(
	ELEMENT_TYPE = "FIRE",
	ATTRIBUTES = pokemon_types.FIRE,
	CATEGORY = "Special",
	POWER = 35, 
	ACCURACY = 85,
	POWER_POINTS = 15,
	DESCRIPTION = "Traps opponent, damaging them for 4-5 turns.")

FISSURE = dict(
 	ELEMENT_TYPE = "GROUND",
	ATTRIBUTES = pokemon_types.GROUND,
	CATEGORY = "Physical",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 5,
	DESCRIPTION = "One-Hit-KO, if it hits.")

FLAMETHROWER = dict(
 	ELEMENT_TYPE = "FIRE",
	ATTRIBUTES = pokemon_types.FIRE,
	CATEGORY = "Special",
	POWER = 90,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "May burn opponent.")

FLASH = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "Lowers opponent's ACCURACY.")

FLY = dict(
 	ELEMENT_TYPE = "FLYING",
	ATTRIBUTES = pokemon_types.FLYING,
	CATEGORY = "Physical",
	POWER = 90,
	ACCURACY = 95,
	POWER_POINTS = 15,
	DESCRIPTION = "Flies up on first turn, attacks on second turn.")

FOCUS_ENERGY = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None, 
	ACCURACY = None,
	POWER_POINTS = 30,
	DESCRIPTION = "Increases critical hit ratio.")

FURY_ATTACK = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 15,
	ACCURACY = 85,
	POWER_POINTS = 20,
	DESCRIPTION = "Hits 2-5 times in one turn.")

FURY_SWIPES = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 18,
	ACCURACY = 80,
	POWER_POINTS = 15,
	DESCRIPTION = "Hits 2-5 times in one turn.")

GLARE = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 30,
	DESCRIPTION = "Paralyzes opponent.")

GROWL = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 40,
	DESCRIPTION = "Lowers opponent's Attack.")

GROWTH = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 40,
	DESCRIPTION = "Raises user's Attack and Special Attack.")

GUILLOTINE = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 5,
	DESCRIPTION = "One-Hit-KO, if it hits.")

GUST = dict(
 	ELEMENT_TYPE = "FLYING",
	ATTRIBUTES = pokemon_types.FLYING,
	CATEGORY = "Special",
	POWER = 40,
	ACCURACY = 100,
	POWER_POINTS = 35,
	DESCRIPTION = "Hits Pokemon using Fly/Bounce with double POWER.")

HARDEN = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 30,
	DESCRIPTION = "Raises user's Defense.")

HAZE = dict(
 	ELEMENT_TYPE = "ICE",
	ATTRIBUTES = pokemon_types.ICE,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 30,
	DESCRIPTION = "Resets all stat changes.")

HEADBUTT = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 70,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "May cause flinching.")

HIGH_JUMP_KICK = dict(
	ELEMENT_TYPE = "FIGHTING",
	ATTRIBUTES = pokemon_types.FIGHTING,
	CATEGORY = "Physical",
	POWER = 130, 
	ACCURACY = 90,
	POWER_POINTS = 10,
	DESCRIPTION = "If it misses, the user loses half their HP.")

HORN_ATTACK = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 65,
	ACCURACY = 100,
	POWER_POINTS = 25,
	DESCRIPTION = "")

HORN_DRILL = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 5,
	DESCRIPTION = "One-Hit-KO, if it hits.")

HYDRO_PUMP = dict(
	ELEMENT_TYPE = "WATER",
	ATTRIBUTES = pokemon_types.WATER,
	CATEGORY = "Special",
	POWER = 110, 
	ACCURACY = 80,
	POWER_POINTS = 5,
	DESCRIPTION = "")

HYPER_BEAM = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Special",
	POWER = 150, 
	ACCURACY = 90,
	POWER_POINTS = 5,
	DESCRIPTION = "User must recharge next turn.")

HYPER_Fang = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 80,
	ACCURACY = 90,
	POWER_POINTS = 15,
	DESCRIPTION = "May cause flinching.")

HYPNOSIS = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	ATTRIBUTES = pokemon_types.PSYCHIC,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = 60,
	POWER_POINTS = 20,
	DESCRIPTION = "Puts opponent to sleep.")

ICE_BEAM = dict(
	ELEMENT_TYPE = "ICE",
	ATTRIBUTES = pokemon_types.ICE,
	CATEGORY = "Special",
	POWER = 90, 
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "May freeze opponent.")

ICE_PUNCH = dict(
	ELEMENT_TYPE = "ICE",
	ATTRIBUTES = pokemon_types.ICE,
	CATEGORY = "Physical",
	POWER = 75,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "May freeze opponent.")

JUMP_KICK = dict(
	ELEMENT_TYPE = "FIGHTING",
	ATTRIBUTES = pokemon_types.FIGHTING,
	CATEGORY = "Physical",
	POWER = 100, 
	ACCURACY = 95,
	POWER_POINTS = 10,
	DESCRIPTION = "If it misses, the user loses half their HP.")

KARATE_CHOP = dict(
	ELEMENT_TYPE = "FIGHTING",
	ATTRIBUTES = pokemon_types.FIGHTING,
	CATEGORY = "Physical",
	POWER = 50,
	ACCURACY = 100,
	POWER_POINTS = 25,
	DESCRIPTION = "High critical hit ratio.")

KINESIS = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	ATTRIBUTES = pokemon_types.PSYCHIC,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = 80,
	POWER_POINTS = 15,
	DESCRIPTION = "Lowers opponent's ACCURACY.")

LEECH_LIFE = dict(
	ELEMENT_TYPE = "BUG",
	ATTRIBUTES = pokemon_types.BUG,
	CATEGORY = "Physical",
	POWER = 80,
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "User recovers half the HP inflicted on opponent.")

LEECH_SEED = dict(
	ELEMENT_TYPE = "GRASS",
	ATTRIBUTES = pokemon_types.GRASS,
	CATEGORY = "Status",
	POWER = None, 
	ACCURACY = 90,
	POWER_POINTS = 10,
	DESCRIPTION = "User steals HP from opponent each turn.")

LEER = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 30,
	DESCRIPTION = "Lowers opponent's Defense.")

LICK = dict(
 	ELEMENT_TYPE = "GHOST",
	ATTRIBUTES = pokemon_types.GHOST,
	CATEGORY = "Physical",
	POWER = 30,
	ACCURACY = 100,
	POWER_POINTS = 30,
	DESCRIPTION = "May paralyze opponent.")

LIGHT_SCREEN = dict(
	ELEMENT_TYPE = "PSYCHIC",
	ATTRIBUTES = pokemon_types.PSYCHIC,
	CATEGORY = "Status",
	POWER = None, 
	ACCURACY = None,
	POWER_POINTS = 30,
	DESCRIPTION = "Halves damage from Special attacks for 5 turns.")

LOVELY_KISS = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None, 
	ACCURACY = 75,
	POWER_POINTS = 10,
	DESCRIPTION = "Puts opponent to sleep.")

LOW_KICK = dict(
	ELEMENT_TYPE = "FIGHTING",
	ATTRIBUTES = pokemon_types.FIGHTING,
	CATEGORY = "Physical",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "The heavier the opponent, the stronger the attack.")

MEDITATE = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	ATTRIBUTES = pokemon_types.PSYCHIC,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 40,
	DESCRIPTION = "Raises user's Attack.")

MEGA_DRAIN = dict(
	ELEMENT_TYPE = "GRASS",
	ATTRIBUTES = pokemon_types.GRASS,
	CATEGORY = "Special",
	POWER = 40, 
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "User recovers half the HP inflicted on opponent.")

MEGA_KICK = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 120, 
	ACCURACY = 75,
	POWER_POINTS = 5,
	DESCRIPTION = "")

MEGA_PUNCH = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 80,
	ACCURACY = 85,
	POWER_POINTS = 20,
	DESCRIPTION = "")

METRONOME = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 10,
	DESCRIPTION = "User performs any move in the game at random.")

MIMIC = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 10,
	DESCRIPTION = "Copies the opponent's last move.")

MINIMIZE = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 10,
	DESCRIPTION = "Sharply raises user's Evasiveness.")

MIRROR_MOVE = dict(
	ELEMENT_TYPE = "FLYING",
	ATTRIBUTES = pokemon_types.FLYING,
	CATEGORY = "Status",
	POWER = None, 
	ACCURACY = None,
	POWER_POINTS = 20,
	DESCRIPTION = "User performs the opponent's last move.")

MIST = dict(
 	ELEMENT_TYPE = "ICE",
	ATTRIBUTES = pokemon_types.ICE,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 30,
	DESCRIPTION = "User's stats cannot be changed for a period of time.")

NIGHT_SHADE = dict(
	ELEMENT_TYPE = "GHOST",
	ATTRIBUTES = pokemon_types.GHOST,
	CATEGORY = "Special",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "Inflicts damage equal to user's level.")

PAY_DAY = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 40,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "A small amount of money is gained after the battle resolves.")

PECK = dict(
 	ELEMENT_TYPE = "FLYING",
	ATTRIBUTES = pokemon_types.FLYING,
	CATEGORY = "Physical",
	POWER = 35,
	ACCURACY = 100,
	POWER_POINTS = 35,
	DESCRIPTION = "")

PETAL_DANCE = dict(
	ELEMENT_TYPE = "GRASS",
	ATTRIBUTES = pokemon_types.GRASS,
	CATEGORY = "Special",
	POWER = 120, 
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "User attacks for 2-3 turns but then becomes confused.")

PIN_MISSILE = dict(
	ELEMENT_TYPE = "BUG",
	ATTRIBUTES = pokemon_types.BUG,
	CATEGORY = "Physical",
	POWER = 25,
	ACCURACY = 95,
	POWER_POINTS = 20,
	DESCRIPTION = "Hits 2-5 times in one turn.")

POISON_GAS = dict(
	ELEMENT_TYPE = "POISON",
	ATTRIBUTES = pokemon_types.POISON,
	CATEGORY = "Status",
	POWER = None, 
	ACCURACY = 90,
	POWER_POINTS = 40,
	DESCRIPTION = "Poisons opponent.")

POISON_POWDER = dict(
	ELEMENT_TYPE = "POISON",
	ATTRIBUTES = pokemon_types.POISON,
	CATEGORY = "Status",
	POWER = None, 
	ACCURACY = 75,
	POWER_POINTS = 35,
	DESCRIPTION = "Poisons opponent.")

POISON_STING = dict(
	ELEMENT_TYPE = "POISON",
	ATTRIBUTES = pokemon_types.POISON,
	CATEGORY = "Physical",
	POWER = 15,
	ACCURACY = 100,
	POWER_POINTS = 35,
	DESCRIPTION = "May poison the opponent.")

POUND = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 40,
	ACCURACY = 100,
	POWER_POINTS = 35,
	DESCRIPTION = "")

PSYBEAM = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	ATTRIBUTES = pokemon_types.PSYCHIC,
	CATEGORY = "Special",
	POWER = 65,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "May confuse opponent.")

PSYCHIC = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	ATTRIBUTES = pokemon_types.PSYCHIC,
	CATEGORY = "Special",
	POWER = 90,
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "May lower opponent's Special Defense.")

PSYWAVE = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	ATTRIBUTES = pokemon_types.PSYCHIC,
	CATEGORY = "Special",
	POWER = None,
	ACCURACY = 80,
	POWER_POINTS = 15,
	DESCRIPTION = "Inflicts damage 50-150% of user's level.")

QUICK_ATTACK = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 40,
	ACCURACY = 100,
	POWER_POINTS = 30,
	DESCRIPTION = "User attacks first.")

RAGE = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 20,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "Raises user's Attack when hit.")

RAZOR_LEAF = dict(
	ELEMENT_TYPE = "GRASS",
	ATTRIBUTES = pokemon_types.GRASS,
	CATEGORY = "Physical",
	POWER = 55,
	ACCURACY = 95,
	POWER_POINTS = 25,
	DESCRIPTION = "High critical hit ratio.")

RAZOR_WIND = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Special",
	POWER = 80, 
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "Charges on first turn, attacks on second. High critical hit ratio.")

RECOVER = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 10,
	DESCRIPTION = "User recovers half its max HP.")

REFLECT = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	ATTRIBUTES = pokemon_types.PSYCHIC,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 20,
	DESCRIPTION = "Halves damage from Physical attacks for 5 turns.")

REST = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	ATTRIBUTES = pokemon_types.PSYCHIC,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 10,
	DESCRIPTION = "User sleeps for 2 turns, but user is fully healed.")

ROAR = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 20,
	DESCRIPTION = "In battles, the opponent switches. In the wild, the Pokemon runs.")

ROCK_SLIDE = dict(
	ELEMENT_TYPE = "ROCK",
	ATTRIBUTES = pokemon_types.ROCK,
	CATEGORY = "Physical",
	POWER = 75,
	ACCURACY = 90,
	POWER_POINTS = 10,
	DESCRIPTION = "May cause flinching.")

ROCK_THROW = dict(
	ELEMENT_TYPE = "ROCK",
	ATTRIBUTES = pokemon_types.ROCK,
	CATEGORY = "Physical",
	POWER = 50,
	ACCURACY = 90,
	POWER_POINTS = 15,
	DESCRIPTION = "")

ROLLING_KICK = dict(
	ELEMENT_TYPE = "FIGHTING",
	ATTRIBUTES = pokemon_types.FIGHTING,
	CATEGORY = "Physical",
	POWER = 60,
	ACCURACY = 85,
	POWER_POINTS = 15,
	DESCRIPTION = "May cause flinching.")

SAND_ATTACK = dict(
	ELEMENT_TYPE = "GROUND",
	ATTRIBUTES = pokemon_types.GROUND,
	CATEGORY = "Status",
	POWER = None, 
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "Lowers opponent's ACCURACY.")

SCRATCH = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 40,
	ACCURACY = 100,
	POWER_POINTS = 35,
	DESCRIPTION = "")

SCREECH = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = 85,
	POWER_POINTS = 40,
	DESCRIPTION = "Sharply lowers opponent's Defense.")

SEISMIC_TOSS = dict(
	ELEMENT_TYPE = "FIGHTING",
	ATTRIBUTES = pokemon_types.FIGHTING,
	CATEGORY = "Physical",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "Inflicts damage equal to user's level.")

SELF_DESTRUCT = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 200, 
	ACCURACY = 100,
	POWER_POINTS = 5,
	DESCRIPTION = "User faints.")

SHARPEN = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 30,
	DESCRIPTION = "Raises user's Attack.")

SING = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = 55,
	POWER_POINTS = 15,
	DESCRIPTION = "Puts opponent to sleep.")

SKULL_BASH = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 130, 
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "Raises Defense on first turn, attacks on second.")

SKY_ATTACK = dict(
	ELEMENT_TYPE = "FLYING",
	ATTRIBUTES = pokemon_types.FLYING,
	CATEGORY = "Physical",
	POWER = 140, 
	ACCURACY = 90,
	POWER_POINTS = 5,
	DESCRIPTION = "Charges on first turn, attacks on second. May cause flinching.")

SLAM = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 80,
	ACCURACY = 75,
	POWER_POINTS = 20,
	DESCRIPTION = "")

SLASH = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 70,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "High critical hit ratio.")

SLEEP_POWDER = dict(
	ELEMENT_TYPE = "GRASS",
	ATTRIBUTES = pokemon_types.GRASS,
	CATEGORY = "Status",
	POWER = None, 
	ACCURACY = 75,
	POWER_POINTS = 15,
	DESCRIPTION = "Puts opponent to sleep.")

SLUDGE = dict(
 	ELEMENT_TYPE = "POISON",
	ATTRIBUTES = pokemon_types.POISON,
	CATEGORY = "Special",
	POWER = 65,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "May poison opponent.")

SMOG = dict(
 	ELEMENT_TYPE = "POISON",
	ATTRIBUTES = pokemon_types.POISON,
	CATEGORY = "Special",
	POWER = 30,
	ACCURACY = 70,
	POWER_POINTS = 20,
	DESCRIPTION = "May poison opponent.")

SMOKESCREEN = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "Lowers opponent's ACCURACY.")

SOFT_BOILED = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None, 
	ACCURACY = None,
	POWER_POINTS = 10,
	DESCRIPTION = "User recovers half its max HP.")

SOLAR_BEAM = dict(
	ELEMENT_TYPE = "GRASS",
	ATTRIBUTES = pokemon_types.GRASS,
	CATEGORY = "Special",
	POWER = 120, 
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "Charges on first turn, attacks on second.")

SONIC_BOOM = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Special",
	POWER = None,
	ACCURACY = 90,
	POWER_POINTS = 20,
	DESCRIPTION = "Always inflicts 20 HP.")

SPIKE_CANNON = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 20,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "Hits 2-5 times in one turn.")

SPLASH = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 40,
	DESCRIPTION = "Doesn't do ANYTHING.")

SPORE = dict(
 	ELEMENT_TYPE = "GRASS",
	ATTRIBUTES = pokemon_types.GRASS,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "Puts opponent to sleep.")

STOMP = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 65,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "May cause flinching.")

STRENGTH = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 80,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "")

STRING_SHOT = dict(
	ELEMENT_TYPE = "BUG",
	ATTRIBUTES = pokemon_types.BUG,
	CATEGORY = "Status",
	POWER = None, 
	ACCURACY = 95,
	POWER_POINTS = 40,
	DESCRIPTION = "Sharply lowers opponent's Speed.")

STRUGGLE = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 50,
	ACCURACY = 100,
	POWER_POINTS = None,
	DESCRIPTION = "Only usable when all PP are gone. Hurts the user.")

STUN_SPORE = dict(
	ELEMENT_TYPE = "GRASS",
	ATTRIBUTES = pokemon_types.GRASS,
	CATEGORY = "Status",
	POWER = None, 
	ACCURACY = 75,
	POWER_POINTS = 30,
	DESCRIPTION = "Paralyzes opponent.")

SUBMISSION = dict(
 	ELEMENT_TYPE = "FIGHTING",
	ATTRIBUTES = pokemon_types.FIGHTING,
	CATEGORY = "Physical",
	POWER = 80,
	ACCURACY = 80,
	POWER_POINTS = 20,
	DESCRIPTION = "User receives recoil damage.")

SUBSTITUTE = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 10,
	DESCRIPTION = "Uses HP to creates a decoy that takes hits.")

SUPER_FANG = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = None,
	ACCURACY = 90,
	POWER_POINTS = 10,
	DESCRIPTION = "Always takes off half of the opponent's HP.")

SUPERSONIC = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = 55,
	POWER_POINTS = 20,
	DESCRIPTION = "Confuses opponent.")

SURF = dict(
 	ELEMENT_TYPE = "WATER",
	ATTRIBUTES = pokemon_types.WATER,
	CATEGORY = "Special",
	POWER = 90,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "Hits all adjacent Pokemon.")

SWIFT = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Special",
	POWER = 60,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "Ignores ACCURACY and Evasiveness.")

SWORDS_DANCE = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None, 
	ACCURACY = None,
	POWER_POINTS = 20,
	DESCRIPTION = "Sharply raises user's Attack.")

TACKLE = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 40,
	ACCURACY = 100,
	POWER_POINTS = 35,
	DESCRIPTION = "")

TAIL_WHIP = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None, 
	ACCURACY = 100,
	POWER_POINTS = 30,
	DESCRIPTION = "Lowers opponent's Defense.")

TAKE_DOWN = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 90,
	ACCURACY = 85,
	POWER_POINTS = 20,
	DESCRIPTION = "User receives recoil damage.")

TELEPORT = dict(
 	ELEMENT_TYPE = "PSYCHIC",
	ATTRIBUTES = pokemon_types.PSYCHIC,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 20,
	DESCRIPTION = "Allows user to flee wild battles; also warps player to last PokeCenter.")

THRASH = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 120,
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "User attacks for 2-3 turns but then becomes confused.")

THUNDER = dict(
 	ELEMENT_TYPE = "ELECTRIC",
	ATTRIBUTES = pokemon_types.ELECTRIC,
	CATEGORY = "Special",
	POWER = 110,
	ACCURACY = 70,
	POWER_POINTS = 10,
	DESCRIPTION = "May paralyze opponent.")

THUNDER_PUNCH = dict(
	ELEMENT_TYPE = "ELECTRIC",
	ATTRIBUTES = pokemon_types.ELECTRIC,
	CATEGORY = "Physical",
	POWER = 75,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "May paralyze opponent.")

THUNDER_SHOCK = dict(
	ELEMENT_TYPE = "ELECTRIC",
	ATTRIBUTES = pokemon_types.ELECTRIC,
	CATEGORY = "Special",
	POWER = 40, 
	ACCURACY = 100,
	POWER_POINTS = 30,
	DESCRIPTION = "May paralyze opponent.")

THUNDER_WAVE = dict(
	ELEMENT_TYPE = "ELECTRIC",
	ATTRIBUTES = pokemon_types.ELECTRIC,
	CATEGORY = "Status",
	POWER = None, 
	ACCURACY = 90,
	POWER_POINTS = 20,
	DESCRIPTION = "Paralyzes opponent.")

THUNDERBOLT = dict(
 	ELEMENT_TYPE = "ELECTRIC",
	ATTRIBUTES = pokemon_types.ELECTRIC,
	CATEGORY = "Special",
	POWER = 90,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "May paralyze opponent.")

TOXIC = dict(
 	ELEMENT_TYPE = "POISON",
	ATTRIBUTES = pokemon_types.POISON,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = 90,
	POWER_POINTS = 10,
	DESCRIPTION = "Badly poisons opponent.")

TRANSFORM = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 10,
	DESCRIPTION = "User takes on the form and attacks of the opponent.")

TRI_ATTACK = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Special",
	POWER = 80, 
	ACCURACY = 100,
	POWER_POINTS = 10,
	DESCRIPTION = "May paralyze, burn or freeze opponent.")

TWINEEDLE = dict(
 	ELEMENT_TYPE = "BUG",
	ATTRIBUTES = pokemon_types.BUG,
	CATEGORY = "Physical",
	POWER = 25,
	ACCURACY = 100,
	POWER_POINTS = 20,
	DESCRIPTION = "Hits twice in one turn. May poison opponent.")

VICE_GRIP = dict(
	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 55,
	ACCURACY = 100,
	POWER_POINTS = 30,
	DESCRIPTION = "")

VINE_WHIP = dict(
	ELEMENT_TYPE = "GRASS",
	ATTRIBUTES = pokemon_types.GRASS,
	CATEGORY = "Physical",
	POWER = 45,
	ACCURACY = 100,
	POWER_POINTS = 25,
	DESCRIPTION = "")

WATER_GUN = dict(
	ELEMENT_TYPE = "WATER",
	ATTRIBUTES = pokemon_types.WATER,
	CATEGORY = "Special",
	POWER = 40, 
	ACCURACY = 100,
	POWER_POINTS = 25,
	DESCRIPTION = "")

WATERFALL = dict(
 	ELEMENT_TYPE = "WATER",
	ATTRIBUTES = pokemon_types.WATER,
	CATEGORY = "Physical",
	POWER = 80,
	ACCURACY = 100,
	POWER_POINTS = 15,
	DESCRIPTION = "May cause flinching.")

WHIRLWIND = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 20,
	DESCRIPTION = "In battles, the opponent switches. In the wild, the Pokemon runs.")

WING_ATTACK = dict(
	ELEMENT_TYPE = "FLYING",
	ATTRIBUTES = pokemon_types.FLYING,
	CATEGORY = "Physical",
	POWER = 60,
	ACCURACY = 100,
	POWER_POINTS = 35,
	DESCRIPTION = "")

WITHDRAW = dict(
 	ELEMENT_TYPE = "WATER",
	ATTRIBUTES = pokemon_types.WATER,
	CATEGORY = "Status",
	POWER = None,
	ACCURACY = None,
	POWER_POINTS = 40,
	DESCRIPTION = "Raises user's Defense.")

WRAP = dict(
 	ELEMENT_TYPE = "NORMAL",
	ATTRIBUTES = pokemon_types.NORMAL,
	CATEGORY = "Physical",
	POWER = 15,
	ACCURACY = 90,
	POWER_POINTS = 20,
	DESCRIPTION = "Traps opponent, damaging them for 4-5 turns.")

"""Dictionary containing the primary Pokemon moves.

Key contains collection of dictionaries containing move properties and statistics.
"""

MOVE_SET = {
	"ABSORB": ABSORB,
	"ACID": ACID,
	"ACID_ARMOUR": ACID_ARMOUR,
	"AGILITY": AGILITY,
	"AMNESIA": AMNESIA,
	"AURORA_BEAM": AURORA_BEAM,
	"BARRAGE": BARRAGE,
	"BARRIER": BARRIER,
	"BIDE": BIDE,
	"BIND": BIND,
	"BITE": BITE,
	"BLIZZARD": BLIZZARD,
	"BODY_SLAM": BODY_SLAM,
	"BONEMERANG": BONEMERANG,
	"BONE_CLUB": BONE_CLUB,
	"BUBBLE": BUBBLE,
	"BUBBLE_BEAM": BUBBLE_BEAM,
	"CLAMP": CLAMP,
	"COMET_PUNCH": COMET_PUNCH,
	"CONFUSE_RAY": CONFUSE_RAY,
	"CONFUSION": CONFUSION,
	"CONSTRICT": CONSTRICT,
	"CONVERSION": CONVERSION,
	"COUNTER": COUNTER,
	"CRABHAMMER": CRABHAMMER,
	"CUT": CUT,
	"DEFENSE_CURL": DEFENSE_CURL,
	"DIG": DIG,
	"DISABLE": DISABLE,
	"DIZZY_PUNCH": DIZZY_PUNCH,
	"DOUBLE_EDGE": DOUBLE_EDGE,
	"DOUBLE_KICK": DOUBLE_KICK,
	"DOUBLE_SLAP": DOUBLE_SLAP,
	"DOUBLE_TEAM": DOUBLE_TEAM,
	"DRAGON_RAGE": DRAGON_RAGE,
	"DREAM_EATER": DREAM_EATER,
	"DRILL_PECK": DRILL_PECK,
	"EARTHQUAKE": EARTHQUAKE,
	"EGG_BOMB": EGG_BOMB,
	"EMBER": EMBER,
	"EXPLOSION": EXPLOSION,
	"FIRE_BLAST": FIRE_BLAST,
	"FIRE_PUNCH": FIRE_PUNCH,
	"FIRE_SPIN": FIRE_SPIN,
	"FISSURE": FISSURE,
	"FLAMETHROWER": FLAMETHROWER,
	"FLASH": FLASH,
	"FLY": FLY,
	"FOCUS_ENERGY": FOCUS_ENERGY,
	"FURY_ATTACK": FURY_ATTACK,
	"FURY_SWIPES": FURY_SWIPES,
	"GLARE": GLARE,
	"GROWL": GROWL,
	"GROWTH": GROWTH,
	"GUILLOTINE": GUILLOTINE,
	"GUST": GUST,
	"HARDEN": HARDEN,
	"HAZE": HAZE,
	"HEADBUTT": HEADBUTT,
	"HORN_ATTACK": HORN_ATTACK,
	"HORN_DRILL": HORN_DRILL,
	"HYDRO_PUMP": HYDRO_PUMP,
	"HYPER_BEAM": HYPER_BEAM,
	"HYPER_Fang": HYPER_Fang,
	"HYPNOSIS": HYPNOSIS,
	"ICE_BEAM": ICE_BEAM,
	"ICE_PUNCH": ICE_PUNCH,
	"JUMP_KICK": JUMP_KICK,
	"KARATE_CHOP": KARATE_CHOP,
	"KINESIS": KINESIS,
	"LEECH_LIFE": LEECH_LIFE,
	"LEECH_SEED": LEECH_SEED,
	"LEER": LEER,
	"LICK": LICK,
	"LIGHT_SCREEN": LIGHT_SCREEN,
	"LOVELY_KISS": LOVELY_KISS,
	"LOW_KICK": LOW_KICK,
	"MEDITATE": MEDITATE,
	"MEGA_DRAIN": MEGA_DRAIN,
	"MEGA_KICK": MEGA_KICK,
	"MEGA_PUNCH": MEGA_PUNCH,
	"METRONOME": METRONOME,
	"MIMIC": MIMIC,
	"MINIMIZE": MINIMIZE,
	"MIRROR_MOVE": MIRROR_MOVE,
	"MIST": MIST,
	"NIGHT_SHADE": NIGHT_SHADE,
	"PAY_DAY": PAY_DAY,
	"PECK": PECK,
	"PETAL_DANCE": PETAL_DANCE,
	"PIN_MISSILE": PIN_MISSILE,
	"POISON_GAS": POISON_GAS,
	"POISON_POWDER": POISON_POWDER,
	"POISON_STING": POISON_STING,
	"POUND": POUND,
	"PSYBEAM": PSYBEAM,
	"PSYCHIC": PSYCHIC,
	"PSYWAVE": PSYWAVE,
	"QUICK_ATTACK": QUICK_ATTACK,
	"RAGE": RAGE,
	"RAZOR_LEAF": RAZOR_LEAF,
	"RAZOR_WIND": RAZOR_WIND,
	"RECOVER": RECOVER,
	"REFLECT": REFLECT,
	"REST": REST,
	"ROAR": ROAR,
	"ROCK_SLIDE": ROCK_SLIDE,
	"ROCK_THROW": ROCK_THROW,
	"ROLLING_KICK": ROLLING_KICK,
	"SAND_ATTACK": SAND_ATTACK,
	"SCRATCH": SCRATCH,
	"SCREECH": SCREECH,
	"SEISMIC_TOSS": SEISMIC_TOSS,
	"SELF_DESTRUCT": SELF_DESTRUCT,
	"SHARPEN": SHARPEN,
	"SING": SING,
	"SKULL_BASH": SKULL_BASH,
	"SKY_ATTACK": SKY_ATTACK,
	"SLAM": SLAM,
	"SLASH": SLASH,
	"SLEEP_POWDER": SLEEP_POWDER,
	"SLUDGE": SLUDGE,
	"SMOG": SMOG,
	"SMOKESCREEN": SMOKESCREEN,
	"SOFT_BOILED": SOFT_BOILED,
	"SOLAR_BEAM": SOLAR_BEAM,
	"SONIC_BOOM": SONIC_BOOM,
	"SPIKE_CANNON": SPIKE_CANNON,
	"SPLASH": SPLASH,
	"SPORE": SPORE,
	"STOMP": STOMP,
	"STRENGTH": STRENGTH,
	"STRING_SHOT": STRING_SHOT,
	"STRUGGLE": STRUGGLE,
	"STUN_SPORE": STUN_SPORE,
	"SUBMISSION": SUBMISSION,
	"SUBSTITUTE": SUBSTITUTE,
	"SUPERSONIC": SUPERSONIC,
	"SUPER_FANG": SUPER_FANG,
	"SURF": SURF,
	"SWIFT": SWIFT,
	"SWORDS_DANCE": SWORDS_DANCE,
	"TACKLE": TACKLE,
	"TAIL_WHIP": TAIL_WHIP,
	"TAKE_DOWN": TAKE_DOWN,
	"TELEPORT": TELEPORT,
	"THRASH": THRASH,
	"THUNDER": THUNDER,
	"THUNDERBOLT": THUNDERBOLT,
	"THUNDER_PUNCH": THUNDER_PUNCH,
	"THUNDER_SHOCK": THUNDER_SHOCK,
	"THUNDER_WAVE": THUNDER_WAVE,
	"TOXIC": TOXIC,
	"TRANSFORM": TRANSFORM,
	"TRI_ATTACK": TRI_ATTACK,
	"TWINEEDLE": TWINEEDLE,
	"VICE_GRIP": VICE_GRIP,
	"VINE_WHIP": VINE_WHIP,
	"WATERFALL": WATERFALL,
	"WATER_GUN": WATER_GUN,
	"WHIRLWIND": WHIRLWIND,
	"WING_ATTACK": WING_ATTACK,
	"WITHDRAW": WITHDRAW,
	"WRAP": WRAP}

"""Dictionary containing the moves for Bug type Pokemon."""

BUG_TYPE_MOVE_SET = { 
	k: v for (k,v) in MOVE_SET.iteritems() 
	if v["ELEMENT_TYPE"] == "BUG"}

"""Dictionary containing the moves for Dark type Pokemon."""

DARK_TYPE_MOVE_SET = { 
	k: v for (k,v) in MOVE_SET.iteritems() 
	if v["ELEMENT_TYPE"] == "DARK"}

"""Dictionary containing the moves for Dragon type Pokemon."""

DRAGON_TYPE_MOVE_SET = { 
	k: v for (k,v) in MOVE_SET.iteritems() 
	if v["ELEMENT_TYPE"] == "DRAGON"}

"""Dictionary containing the moves for Electric type Pokemon."""

ELECTRIC_TYPE_MOVE_SET = { 
	k: v for (k,v) in MOVE_SET.iteritems() 
	if v["ELEMENT_TYPE"] == "ELECTRIC"}

"""Dictionary containing the moves for Fairy type Pokemon."""

FAIRY_TYPE_MOVE_SET = { 
	k: v for (k,v) in MOVE_SET.iteritems() 
	if v["ELEMENT_TYPE"] == "FAIRY" }

"""Dictionary containing the moves for Fighting type Pokemon."""

FIGHTING_TYPE_MOVE_SET = { 
	k: v for (k,v) in MOVE_SET.iteritems() 
	if v["ELEMENT_TYPE"] == "FIGHTING"}

"""Dictionary containing the moves for Fire type Pokemon."""

FIRE_TYPE_MOVE_SET = { 
	k: v for (k,v) in MOVE_SET.iteritems() 
	if v["ELEMENT_TYPE"] == "FIRE"}

"""Dictionary containing the moves for Flying type Pokemon."""

FLYING_TYPE_MOVE_SET = { 
	k: v for (k,v) in MOVE_SET.iteritems() 
	if v["ELEMENT_TYPE"] == "FLYING"}

"""Dictionary containing the moves for Ghost type Pokemon."""

GHOST_TYPE_MOVE_SET = { 
	k: v for (k,v) in MOVE_SET.iteritems() 
	if v["ELEMENT_TYPE"] == "GHOST"}

"""Dictionary containing the moves for Grass type Pokemon."""

GRASS_TYPE_MOVE_SET = { 
	k: v for (k,v) in MOVE_SET.iteritems() 
	if v["ELEMENT_TYPE"] == "GRASS"}

"""Dictionary containing the moves for Ground type Pokemon."""

GROUND_TYPE_MOVE_SET = { 
	k: v for (k,v) in MOVE_SET.iteritems() 
	if v["ELEMENT_TYPE"] == "GROUND"}

"""Dictionary containing the moves for Ice type Pokemon."""

ICE_TYPE_MOVE_SET = { 
	k: v for (k,v) in MOVE_SET.iteritems() 
	if v["ELEMENT_TYPE"] == "ICE"}

"""Dictionary containing the moves for Normal type Pokemon."""

NORMAL_TYPE_MOVE_SET = { 
	k: v for (k,v) in MOVE_SET.iteritems() 
	if v["ELEMENT_TYPE"] == "NORMAL"}

"""Dictionary containing the moves for Poison type Pokemon."""

POISON_TYPE_MOVE_SET = { 
	k: v for (k,v) in MOVE_SET.iteritems() 
	if v["ELEMENT_TYPE"] == "POISON"}

"""Dictionary containing the moves for Psychic type Pokemon."""

PSYCHIC_TYPE_MOVE_SET = { 
	k: v for (k,v) in MOVE_SET.iteritems() 
	if v["ELEMENT_TYPE"] == "PSYCHIC"}

"""Dictionary containing the moves for Rock type Pokemon."""

ROCK_TYPE_MOVE_SET = { 
	k: v for (k,v) in MOVE_SET.iteritems() 
	if v["ELEMENT_TYPE"] == "ROCK"}

"""Dictionary containing the moves for Steel type Pokemon."""

STEEL_TYPE_MOVE_SET = { 
	k: v for (k,v) in MOVE_SET.iteritems() 
	if v["ELEMENT_TYPE"] == "STEEL"}

"""Dictionary containing the moves for Water type Pokemon."""

WATER_TYPE_MOVE_SET = { 
	k: v for (k,v) in MOVE_SET.iteritems() 
	if v["ELEMENT_TYPE"] == "WATER"}

"""Tuple containing strings of Pokemon moves.

Names are generated from initialised names. Requires Pokemon move is defined in Move Set dictionary.
"""

MOVE_NAMES = tuple(dict.keys(MOVE_SET))

"""Tuple containing strings of moves for Bug type Pokemon."""

BUG_TYPE_MOVE_NAMES = tuple(dict.keys(BUG_TYPE_MOVE_SET))

"""Tuple containing strings of moves for Dark type Pokemon."""

DARK_TYPE_MOVE_NAMES = tuple(dict.keys(DARK_TYPE_MOVE_SET))

"""Tuple containing strings of moves for Dragon type Pokemon."""

DRAGON_TYPE_MOVE_NAMES = tuple(dict.keys(DRAGON_TYPE_MOVE_SET))

"""Tuple containing strings of moves for Electric type Pokemon."""

ELECTRIC_TYPE_MOVE_NAMES = tuple(dict.keys(ELECTRIC_TYPE_MOVE_SET))

"""Tuple containing strings of moves for Fairy type Pokemon."""

FAIRY_TYPE_MOVE_NAMES = tuple(dict.keys(FAIRY_TYPE_MOVE_SET))

"""Tuple containing strings of moves for Fighting type Pokemon."""

FIGHTING_TYPE_MOVE_NAMES = tuple(dict.keys(FIGHTING_TYPE_MOVE_SET))

"""Tuple containing strings of moves for Fire type Pokemon."""

FIRE_TYPE_MOVE_NAMES = tuple(dict.keys(FIRE_TYPE_MOVE_SET))

"""Tuple containing strings of moves for Flying type Pokemon."""

FLYING_TYPE_MOVE_NAMES = tuple(dict.keys(FLYING_TYPE_MOVE_SET))

"""Tuple containing strings of moves for Ghost type Pokemon."""

GHOST_TYPE_MOVE_NAMES = tuple(dict.keys(GHOST_TYPE_MOVE_SET))

"""Tuple containing strings of moves for Grass type Pokemon."""

GRASS_TYPE_MOVE_NAMES = tuple(dict.keys(GRASS_TYPE_MOVE_SET))

"""Tuple containing strings of moves for Ground type Pokemon."""

GROUND_TYPE_MOVE_NAMES = tuple(dict.keys(GROUND_TYPE_MOVE_SET))

"""Tuple containing strings of moves for Ice type Pokemon."""

ICE_TYPE_MOVE_NAMES = tuple(dict.keys(ICE_TYPE_MOVE_SET))

"""Tuple containing strings of moves for Normal type Pokemon."""

NORMAL_TYPE_MOVE_NAMES = tuple(dict.keys(NORMAL_TYPE_MOVE_SET))

"""Tuple containing strings of moves for Poison type Pokemon."""

POISON_TYPE_MOVE_NAMES = tuple(dict.keys(POISON_TYPE_MOVE_SET))

"""Tuple containing strings of moves for Psychic type Pokemon."""

PSYCHIC_TYPE_MOVE_NAMES = tuple(dict.keys(PSYCHIC_TYPE_MOVE_SET))

"""Tuple containing strings of moves for Rock type Pokemon."""

ROCK_TYPE_MOVE_NAMES = tuple(dict.keys(ROCK_TYPE_MOVE_SET))

"""Tuple containing strings of moves for Steel type Pokemon."""

STEEL_TYPE_MOVE_NAMES = tuple(dict.keys(STEEL_TYPE_MOVE_SET))

"""Tuple containing strings of moves for Water type Pokemon."""

WATER_TYPE_MOVE_NAMES = tuple(dict.keys(WATER_TYPE_MOVE_SET))

"""String generated from the required keys for Pokemon moves."""

MOVE_SET_KEYS_STRS = " ".join([
	"ELEMENT_TYPE",
	"ATTRIBUTES",
	"CATEGORY",
	"POWER", 
	"ACCURACY",
	"POWER_POINTS",
	"DESCRIPTION"])

######################
### Module classes ###
######################

class Generate (namedtuple("Props", MOVE_SET_KEYS_STRS)):
	"""Generates type properties for defined Pokemon type."""

	def __new__ (self, pokemon_move):
		"""Inherit constants for class from named tuple Props.
		
		Anticipated to be consumed in Pokemon base type class constructor. 
		"""

		"""
		>>> import pokemon_moves
		>>> pokemon_moves.Generate("DOUBLE EDGE")

		Props(
			ELEMENT_TYPE='NORMAL', 
			ATTRIBUTES=Props(
				GHOST=GhostTypeMeta(
					EFFECT='NO_EFFECT', 
					SUM=0), 
			...), 
			CATEGORY='Physical', 
			POWER=120, 
			ACCURACY=100, 
			POWER_POINTS=15, 
			DESCRIPTION='User receives recoil damage.')
		"""

		# Named arguments #

		# @parameter: <pokemon_move>, @type: <str>, @required: <true>
		# @description: Pokemon move class type to generate.

		# set pokemon type argument as string and uppercase for comparisons and collections.
		pokemon_move = str.upper(str(pokemon_move))

		# set substring substitution on whitespaces.
		pokemon_move = re.sub(r'\s', '_', pokemon_move)

		# confirm pokemon move is defined move otherwise select move at random.
		pokemon_move = pokemon_move if pokemon_move in MOVE_NAMES else random.choice(MOVE_NAMES)

		# return: @type: @class.__main__.Generate
		return super(Generate, self).__new__(self, **MOVE_SET[pokemon_move])

######################
### Module exports ###
######################

"""Generate constants from defined properties. Overwrites previous properties.

Composed to consume existing declerations.
"""

for i in range(0, len(MOVE_NAMES)):
	"""Set module properties. Sets package variable using defined names in move sets."""
	setattr(sys.modules[__name__], MOVE_NAMES[i], Generate(MOVE_NAMES[i]))