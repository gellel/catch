#!/usr/bin/env python3

# -*- coding: utf-8 -*- 

# from collections import named tuple module.
from collections import namedtuple
# import random
import random
# import pokemon types
import pokemon_types

########################
### File information ###
########################

__author__  = "Lindsay Gelle (https://github.com/gellel)"

__version__ = "1.0"

########################
### Module constants ###
########################

"""Tuple containing STRINGs of keys for Pokemon moves generator.

Key names are base from Pokemon DB.
"""

KEYS = (
	"ELEMENT_TYPE", 
	"CATEGORY", 
	"POWER", 
	"ACCURACY", 
	"PP", 
	"DESCRIPTION")

"""STRING comprised of the different Pokemon generator key subSTRINGs."""

KEYS_STRS = " ".join(KEYS)


ABSORB = dict(
	element_type= "Grass",
	category = "Special",
	power = 20,
	accuracy = 100,
	pp = 25,
	description = "User recovers half the HP inflicted on opponent.")

ACID = dict(
	element_type = "Poison",
	category = "Special",
	power = 40,
	accuracy = 100,
	pp = 30,
	description = "May lower opponent's Special Defense.")

ACID_ARMOUR = dict(
	element_type = "Poison",
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 20,
	description = "Sharply raises user's Defense.")

AGILITY = dict(
	element_type = "Psychic",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 30,
	description = "Sharply raises user's Speed.")

AMNESIA = dict(
	element_type = "Psychic",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 20,
	description = "Sharply raises user's Special Defense.")

AURORA_BEAM = dict(
	element_type = "Ice",
	category = "Special",
	power = 65, 
	accuracy = 100,
	pp = 20,
	description = "May lower opponent's Attack.")

BARRAGE = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 15,
	accuracy = 85,
	pp = 20,
	description = "Hits 2-5 times in one turn.")

BARRIER = dict(
 	element_type = "Psychic",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 20,
	description = "Sharply raises user's Defense.")

BIDE = dict(
 	element_type = "Normal",
	category = "Physical",
	power = None,
	accuracy = None,
	pp = 10,
	description = "User takes damage for two turns then strikes back double.")

BIND = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 15,
	accuracy = 85,
	pp = 20,
	description = "Traps opponent, damaging them for 4-5 turns.")

BITE = dict(
 	element_type = "Dark",
	category = "Physical",
	power = 60,
	accuracy = 100,
	pp = 25,
	description = "May cause flinching.")

BLIZZARD = dict(
 	element_type = "Ice",
	category = "Special",
	power = 110,
	accuracy = 70,
	pp = 5,
	description = "May freeze opponent.")

BODY_SLAM = dict(
	element_type = "Normal",
	category = "Physical",
	power = 85,
	accuracy = 100,
	pp = 15,
	description = "May paralyze opponent.")

BONE_CLUB = dict(
	element_type = "Ground",
	category = "Physical",
	power = 65,
	accuracy = 85,
	pp = 20,
	description = "May cause flinching.")

BONEMERANG = dict(
 	element_type = "Ground",
	category = "Physical",
	power = 50,
	accuracy = 90,
	pp = 10,
	description = "Hits twice in one turn.")

BUBBLE = dict(
 	element_type = "Water",
	category = "Special",
	power = 40,
	accuracy = 100,
	pp = 30,
	description = "May lower opponent's Speed.")

BUBBLE_BEAM = dict(
	element_type = "Water",
	category = "Special",
	power = 65, 
	accuracy = 100,
	pp = 20,
	description = "May lower opponent's Speed.")

CLAMP = dict(
 	element_type = "Water",
	category = "Physical",
	power = 35,
	accuracy = 85,
	pp = 10,
	description = "Traps opponent, damaging them for 4-5 turns.")

COMET_PUNCH = dict(
	element_type = "Normal",
	category = "Physical",
	power = 18,
	accuracy = 85,
	pp = 15,
	description = "Hits 2-5 times in one turn.")

CONFUSE_RAY = dict(
	element_type = "Ghost",
	category = "Status",
	power = None, 
	accuracy = 100,
	pp = 10,
	description = "Confuses opponent.")

CONFUSION = dict(
 	element_type = "Psychic",
	category = "Special",
	power = 50,
	accuracy = 100,
	pp = 25,
	description = "May confuse opponent.")

CONSTRICT = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 10,
	accuracy = 100,
	pp = 35,
	description = "May lower opponent's Speed by one stage.")

CONVERSION = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 30,
	description = "Changes user's type to that of its first move.")

COUNTER = dict(
 	element_type = "Fighting",
	category = "Physical",
	power = None,
	accuracy = 100,
	pp = 20,
	description = "When hit by a Physical Attack, user strikes back with 2x power.")

CRABHAMMER = dict(
 	element_type = "Water",
	category = "Physical",
	power = 100,
	accuracy = 90,
	pp = 10,
	description = "High critical hit ratio.")

CUT = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 50,
	accuracy = 95,
	pp = 30,
	description = "")

DEFENSE_CURL = dict(
	element_type = "Normal",
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 40,
	description = "Raises user's Defense.")

DIG = dict(
 	element_type = "Ground",
	category = "Physical",
	power = 80,
	accuracy = 100,
	pp = 10,
	description = "Digs underground on first turn, attacks on second. Can also escape from caves.")

DISABLE = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = 100,
	pp = 20,
	description = "Opponent can't use its last attack for a few turns.")

DIZZY_PUNCH = dict(
	element_type = "Normal",
	category = "Physical",
	power = 70,
	accuracy = 100,
	pp = 10,
	description = "May confuse opponent.")

DOUBLE_KICK = dict(
	element_type = "Fighting",
	category = "Physical",
	power = 30,
	accuracy = 100,
	pp = 30,
	description = "Hits twice in one turn.")

DOUBLE_SLAP = dict(
	element_type = "Normal",
	category = "Physical",
	power = 15,
	accuracy = 85,
	pp = 10,
	description = "Hits 2-5 times in one turn.")

DOUBLE_TEAM = dict(
	element_type = "Normal",
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 15,
	description = "Raises user's Evasiveness.")

DOUBLE_EDGE = dict(
	element_type = "Normal",
	category = "Physical",
	power = 120, 
	accuracy = 100,
	pp = 15,
	description = "User receives recoil damage.")

DRAGON_RAGE = dict(
	element_type = "Dragon",
	category = "Special",
	power = None,
	accuracy = 100,
	pp = 10,
	description = "Always inflicts 40 HP.")

DREAM_EATER = dict(
	element_type = "Psychic",
	category = "Special",
	power = 10,0 
	accuracy = 100,
	pp = 15,
	description = "User recovers half the HP inflicted on a sleeping opponent.")

DRILL_PECK = dict(
	element_type = "Flying",
	category = "Physical",
	power = 80,
	accuracy = 100,
	pp = 20,
	description = "")

EARTHQUAKE = dict(
 	element_type = "Ground",
	category = "Physical",
	power = 100,
	accuracy = 100,
	pp = 10,
	description = "Power is doubled if opponent is underground from using Dig.")

EGG_BOMB = dict(
	element_type = "Normal",
	category = "Physical",
	power = 100, 
	accuracy = 75,
	pp = 10,
	description = "")

EMBER = dict(
 	element_type = "Fire",
	category = "Special",
	power = 40,
	accuracy = 100,
	pp = 25,
	description = "May burn opponent.")

EXPLOSION = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 250,
	accuracy = 100,
	pp = 5,
	description = "User faints.")

FIRE_BLAST = dict(
	element_type = "Fire",
	category = "Special",
	power = 11,0 
	accuracy = 85,
	pp = 5,
	description = "May burn opponent.")

FIRE_PUNCH = dict(
	element_type = "Fire",
	category = "Physical",
	power = 75,
	accuracy = 100,
	pp = 15,
	description = "May burn opponent.")

FIRE_SPIN = dict(
	element_type = "Fire",
	category = "Special",
	power = 35, 
	accuracy = 85,
	pp = 15,
	description = "Traps opponent, damaging them for 4-5 turns.")

FISSURE = dict(
 	element_type = "Ground",
	category = "Physical",
	power = None,
	accuracy = None,
	pp = 5,
	description = "One-Hit-KO, if it hits.")

FLAMETHROWER = dict(
 	element_type = "Fire",
	category = "Special",
	power = 90,
	accuracy = 100,
	pp = 15,
	description = "May burn opponent.")

FLASH = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = 100,
	pp = 20,
	description = "Lowers opponent's Accuracy.")

FLY = dict(
 	element_type = "Flying",
	category = "Physical",
	power = 90,
	accuracy = 95,
	pp = 15,
	description = "Flies up on first turn, attacks on second turn.")

FOCUS_ENERGY = dict(
	element_type = "Normal",
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 30,
	description = "Increases critical hit ratio.")

FURY_ATTACK = dict(
	element_type = "Normal",
	category = "Physical",
	power = 15,
	accuracy = 85,
	pp = 20,
	description = "Hits 2-5 times in one turn.")

FURY_SWIPES = dict(
	element_type = "Normal",
	category = "Physical",
	power = 18,
	accuracy = 80,
	pp = 15,
	description = "Hits 2-5 times in one turn.")

GLARE = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = 100,
	pp = 30,
	description = "Paralyzes opponent.")

GROWL = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = 100,
	pp = 40,
	description = "Lowers opponent's Attack.")

GROWTH = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 40,
	description = "Raises user's Attack and Special Attack.")

GUILLOTINE = dict(
 	element_type = "Normal",
	category = "Physical",
	power = None,
	accuracy = None,
	pp = 5,
	description = "One-Hit-KO, if it hits.")

GUST = dict(
 	element_type = "Flying",
	category = "Special",
	power = 40,
	accuracy = 100,
	pp = 35,
	description = "Hits Pokemon using Fly/Bounce with double power.")

HARDEN = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 30,
	description = "Raises user's Defense.")

HAZE = dict(
 	element_type = "Ice",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 30,
	description = "Resets all stat changes.")

HEADBUTT = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 70,
	accuracy = 100,
	pp = 15,
	description = "May cause flinching.")

HIGH_JUMP_KICK = dict(
	element_type = "Fighting",
	category = "Physical",
	power = 130, 
	accuracy = 90,
	pp = 10,
	description = "If it misses, the user loses half their HP.")

HORN_ATTACK = dict(
	element_type = "Normal",
	category = "Physical",
	power = 65,
	accuracy = 100,
	pp = 25,
	description = "")

HORN_DRILL = dict(
	element_type = "Normal",
	category = "Physical",
	power = None,
	accuracy = None,
	pp = 5,
	description = "One-Hit-KO, if it hits.")

HYDRO_PUMP = dict(
	element_type = "Water",
	category = "Special",
	power = 11,0 
	accuracy = 80,
	pp = 5,
	description = "")

HYPER_BEAM = dict(
	element_type = "Normal",
	category = "Special",
	power = 15,0 
	accuracy = 90,
	pp = 5,
	description = "User must recharge next turn.")

HYPER_Fang = dict(
	element_type = "Normal",
	category = "Physical",
	power = 80,
	accuracy = 90,
	pp = 15,
	description = "May cause flinching.")

HYPNOSIS = dict(
 	element_type = "Psychic",
	category = "Status",
	power = None,
	accuracy = 60,
	pp = 20,
	description = "Puts opponent to sleep.")

ICE_BEAM = dict(
	element_type = "Ice",
	category = "Special",
	power = 90, 
	accuracy = 100,
	pp = 10,
	description = "May freeze opponent.")

ICE_PUNCH = dict(
	element_type = "Ice",
	category = "Physical",
	power = 75,
	accuracy = 100,
	pp = 15,
	description = "May freeze opponent.")

JUMP_KICK = dict(
	element_type = "Fighting",
	category = "Physical",
	power = 100, 
	accuracy = 95,
	pp = 10,
	description = "If it misses, the user loses half their HP.")

KARATE_CHOP = dict(
	element_type = "Fighting",
	category = "Physical",
	power = 50,
	accuracy = 100,
	pp = 25,
	description = "High critical hit ratio.")

KINESIS = dict(
 	element_type = "Psychic",
	category = "Status",
	power = None,
	accuracy = 80,
	pp = 15,
	description = "Lowers opponent's Accuracy.")

LEECH_LIFE = dict(
	element_type = "Bug",
	category = "Physical",
	power = 80,
	accuracy = 100,
	pp = 10,
	description = "User recovers half the HP inflicted on opponent.")

LEECH_SEED = dict(
	element_type = "Grass",
	category = "Status",
	power = None, 
	accuracy = 90,
	pp = 10,
	description = "User steals HP from opponent each turn.")

LEER = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = 100,
	pp = 30,
	description = "Lowers opponent's Defense.")

LICK = dict(
 	element_type = "Ghost",
	category = "Physical",
	power = 30,
	accuracy = 100,
	pp = 30,
	description = "May paralyze opponent.")

LIGHT_SCREEN = dict(
	element_type = "Psychic",
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 30,
	description = "Halves damage from Special attacks for 5 turns.")

LOVELY_KISS = dict(
	element_type = "Normal",
	category = "Status",
	power = None, 
	accuracy = 75,
	pp = 10,
	description = "Puts opponent to sleep.")

LOW_KICK = dict(
	element_type = "Fighting",
	category = "Physical",
	power = None,
	accuracy = 100,
	pp = 20,
	description = "The heavier the opponent, the stronger the attack.")

MEDITATE = dict(
 	element_type = "Psychic",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 40,
	description = "Raises user's Attack.")

MEGA_DRAIN = dict(
	element_type = "Grass",
	category = "Special",
	power = 40, 
	accuracy = 100,
	pp = 15,
	description = "User recovers half the HP inflicted on opponent.")

MEGA_KICK = dict(
	element_type = "Normal",
	category = "Physical",
	power = 120, 
	accuracy = 75,
	pp = 5,
	description = "")

MEGA_PUNCH = dict(
	element_type = "Normal",
	category = "Physical",
	power = 80,
	accuracy = 85,
	pp = 20,
	description = "")

METRONOME = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 10,
	description = "User performs any move in the game at random.")

MIMIC = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 10,
	description = "Copies the opponent's last move.")

MINIMIZE = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 10,
	description = "Sharply raises user's Evasiveness.")

MIRROR_MOVE = dict(
	element_type = "Flying",
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 20,
	description = "User performs the opponent's last move.")

MIST = dict(
 	element_type = "Ice",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 30,
	description = "User's stats cannot be changed for a period of time.")

NIGHT_SHADE = dict(
	element_type = "Ghost",
	category = "Special",
	power = None,
	accuracy = 100,
	pp = 15,
	description = "Inflicts damage equal to user's level.")

PAY_DAY = dict(
	element_type = "Normal",
	category = "Physical",
	power = 40,
	accuracy = 100,
	pp = 20,
	description = "A small amount of money is gained after the battle resolves.")

PECK = dict(
 	element_type = "Flying",
	category = "Physical",
	power = 35,
	accuracy = 100,
	pp = 35,
	description = "")

PETAL_DANCE = dict(
	element_type = "Grass",
	category = "Special",
	power = 12,0 
	accuracy = 100,
	pp = 10,
	description = "User attacks for 2-3 turns but then becomes confused.")

PIN_MISSILE = dict(
	element_type = "Bug",
	category = "Physical",
	power = 25,
	accuracy = 95,
	pp = 20,
	description = "Hits 2-5 times in one turn.")

POISON_GAS = dict(
	element_type = "Poison",
	category = "Status",
	power = None, 
	accuracy = 90,
	pp = 40,
	description = "Poisons opponent.")

POISON_POWDER = dict(
	element_type = "Poison",
	category = "Status",
	power = None, 
	accuracy = 75,
	pp = 35,
	description = "Poisons opponent.")

POISON_STING = dict(
	element_type = "Poison",
	category = "Physical",
	power = 15,
	accuracy = 100,
	pp = 35,
	description = "May poison the opponent.")

POUND = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 40,
	accuracy = 100,
	pp = 35,
	description = "")

PSYBEAM = dict(
 	element_type = "Psychic",
	category = "Special",
	power = 65,
	accuracy = 100,
	pp = 20,
	description = "May confuse opponent.")

PSYCHIC = dict(
 	element_type = "Psychic",
	category = "Special",
	power = 90,
	accuracy = 100,
	pp = 10,
	description = "May lower opponent's Special Defense.")

PSYWAVE = dict(
 	element_type = "Psychic",
	category = "Special",
	power = None,
	accuracy = 80,
	pp = 15,
	description = "Inflicts damage 50-150% of user's level.")

QUICK_ATTACK = dict(
	element_type = "Normal",
	category = "Physical",
	power = 40,
	accuracy = 100,
	pp = 30,
	description = "User attacks first.")

RAGE = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 20,
	accuracy = 100,
	pp = 20,
	description = "Raises user's Attack when hit.")

RAZOR_LEAF = dict(
	element_type = "Grass",
	category = "Physical",
	power = 55,
	accuracy = 95,
	pp = 25,
	description = "High critical hit ratio.")

RAZOR_WIND = dict(
	element_type = "Normal",
	category = "Special",
	power = 80, 
	accuracy = 100,
	pp = 10,
	description = "Charges on first turn, attacks on second. High critical hit ratio.")

RECOVER = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 10,
	description = "User recovers half its max HP.")

REFLECT = dict(
 	element_type = "Psychic",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 20,
	description = "Halves damage from Physical attacks for 5 turns.")

REST = dict(
 	element_type = "Psychic",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 10,
	description = "User sleeps for 2 turns, but user is fully healed.")

ROAR = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 20,
	description = "In battles, the opponent switches. In the wild, the Pokemon runs.")

ROCK_SLIDE = dict(
	element_type = "Rock",
	category = "Physical",
	power = 75,
	accuracy = 90,
	pp = 10,
	description = "May cause flinching.")

ROCK_THROW = dict(
	element_type = "Rock",
	category = "Physical",
	power = 50,
	accuracy = 90,
	pp = 15,
	description = "")

ROLLING_KICK = dict(
	element_type = "Fighting",
	category = "Physical",
	power = 60,
	accuracy = 85,
	pp = 15,
	description = "May cause flinching.")

SAND_ATTACK = dict(
	element_type = "Ground",
	category = "Status",
	power = None, 
	accuracy = 100,
	pp = 15,
	description = "Lowers opponent's Accuracy.")

SCRATCH = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 40,
	accuracy = 100,
	pp = 35,
	description = "")

SCREECH = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = 85,
	pp = 40,
	description = "Sharply lowers opponent's Defense.")

SEISMIC_TOSS = dict(
	element_type = "Fighting",
	category = "Physical",
	power = None,
	accuracy = 100,
	pp = 20,
	description = "Inflicts damage equal to user's level.")

SELF_DESTRUCT = dict(
	element_type = "Normal",
	category = "Physical",
	power = 200, 
	accuracy = 100,
	pp = 5,
	description = "User faints.")

SHARPEN = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 30,
	description = "Raises user's Attack.")

SING = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = 55,
	pp = 15,
	description = "Puts opponent to sleep.")

SKULL_BASH = dict(
	element_type = "Normal",
	category = "Physical",
	power = 130, 
	accuracy = 100,
	pp = 10,
	description = "Raises Defense on first turn, attacks on second.")

SKY_ATTACK = dict(
	element_type = "Flying",
	category = "Physical",
	power = 140, 
	accuracy = 90,
	pp = 5,
	description = "Charges on first turn, attacks on second. May cause flinching.")

SLAM = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 80,
	accuracy = 75,
	pp = 20,
	description = "")

SLASH = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 70,
	accuracy = 100,
	pp = 20,
	description = "High critical hit ratio.")

SLEEP_POWDER = dict(
	element_type = "Grass",
	category = "Status",
	power = None, 
	accuracy = 75,
	pp = 15,
	description = "Puts opponent to sleep.")

SLUDGE = dict(
 	element_type = "Poison",
	category = "Special",
	power = 65,
	accuracy = 100,
	pp = 20,
	description = "May poison opponent.")

SMOG = dict(
 	element_type = "Poison",
	category = "Special",
	power = 30,
	accuracy = 70,
	pp = 20,
	description = "May poison opponent.")

SMOKESCREEN = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = 100,
	pp = 20,
	description = "Lowers opponent's Accuracy.")

SOFT_BOILED = dict(
	element_type = "Normal",
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 10,
	description = "User recovers half its max HP.")

SOLAR_BEAM = dict(
	element_type = "Grass",
	category = "Special",
	power = 12,0 
	accuracy = 100,
	pp = 10,
	description = "Charges on first turn, attacks on second.")

SONIC_BOOM = dict(
	element_type = "Normal",
	category = "Special",
	power = None,
	accuracy = 90,
	pp = 20,
	description = "Always inflicts 20 HP.")

SPIKE_CANNON = dict(
	element_type = "Normal",
	category = "Physical",
	power = 20,
	accuracy = 100,
	pp = 15,
	description = "Hits 2-5 times in one turn.")

SPLASH = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 40,
	description = "Doesn't do ANYTHING.")

SPORE = dict(
 	element_type = "Grass",
	category = "Status",
	power = None,
	accuracy = 100,
	pp = 15,
	description = "Puts opponent to sleep.")

STOMP = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 65,
	accuracy = 100,
	pp = 20,
	description = "May cause flinching.")

STRENGTH = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 80,
	accuracy = 100,
	pp = 15,
	description = "")

STRING_SHOT = dict(
	element_type = "Bug",
	category = "Status",
	power = None, 
	accuracy = 95,
	pp = 40,
	description = "Sharply lowers opponent's Speed.")

STRUGGLE = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 50,
	accuracy = 100,
	pp = None,
	description = "Only usable when all PP are gone. Hurts the user.")

STUN_SPORE = dict(
	element_type = "Grass",
	category = "Status",
	power = None, 
	accuracy = 75,
	pp = 30,
	description = "Paralyzes opponent.")

SUBMISSION = dict(
 	element_type = "Fighting",
	category = "Physical",
	power = 80,
	accuracy = 80,
	pp = 20,
	description = "User receives recoil damage.")

SUBSTITUTE = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 10,
	description = "Uses HP to creates a decoy that takes hits.")

SUPER_FANG = dict(
	element_type = "Normal",
	category = "Physical",
	power = None,
	accuracy = 90,
	pp = 10,
	description = "Always takes off half of the opponent's HP.")

SUPERSONIC = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = 55,
	pp = 20,
	description = "Confuses opponent.")

SURF = dict(
 	element_type = "Water",
	category = "Special",
	power = 90,
	accuracy = 100,
	pp = 15,
	description = "Hits all adjacent Pokemon.")

SWIFT = dict(
 	element_type = "Normal",
	category = "Special",
	power = 60,
	accuracy = 100,
	pp = 20,
	description = "Ignores Accuracy and Evasiveness.")

SWORDS_DANCE = dict(
	element_type = "Normal",
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 20,
	description = "Sharply raises user's Attack.")

TACKLE = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 40,
	accuracy = 100,
	pp = 35,
	description = "")

TAIL_WHIP = dict(
	element_type = "Normal",
	category = "Status",
	power = None, 
	accuracy = 100,
	pp = 30,
	description = "Lowers opponent's Defense.")

TAKE_DOWN = dict(
	element_type = "Normal",
	category = "Physical",
	power = 90,
	accuracy = 85,
	pp = 20,
	description = "User receives recoil damage.")

TELEPORT = dict(
 	element_type = "Psychic",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 20,
	description = "Allows user to flee wild battles; also warps player to last PokeCenter.")

THRASH = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 120,
	accuracy = 100,
	pp = 10,
	description = "User attacks for 2-3 turns but then becomes confused.")

THUNDER = dict(
 	element_type = "Electric",
	category = "Special",
	power = 110,
	accuracy = 70,
	pp = 10,
	description = "May paralyze opponent.")

THUNDER_PUNCH = dict(
	element_type = "Electric",
	category = "Physical",
	power = 75,
	accuracy = 100,
	pp = 15,
	description = "May paralyze opponent.")

THUNDER_SHOCK = dict(
	element_type = "Electric",
	category = "Special",
	power = 40, 
	accuracy = 100,
	pp = 30,
	description = "May paralyze opponent.")

THUNDER_WAVE = dict(
	element_type = "Electric",
	category = "Status",
	power = None, 
	accuracy = 90,
	pp = 20,
	description = "Paralyzes opponent.")

THUNDERBOLT = dict(
 	element_type = "Electric",
	category = "Special",
	power = 90,
	accuracy = 100,
	pp = 15,
	description = "May paralyze opponent.")

TOXIC = dict(
 	element_type = "Poison",
	category = "Status",
	power = None,
	accuracy = 90,
	pp = 10,
	description = "Badly poisons opponent.")

TRANSFORM = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 10,
	description = "User takes on the form and attacks of the opponent.")

TRI_ATTACK = dict(
	element_type = "Normal",
	category = "Special",
	power = 80, 
	accuracy = 100,
	pp = 10,
	description = "May paralyze, burn or freeze opponent.")

TWINEEDLE = dict(
 	element_type = "Bug",
	category = "Physical",
	power = 25,
	accuracy = 100,
	pp = 20,
	description = "Hits twice in one turn. May poison opponent.")

VICE_GRIP = dict(
	element_type = "Normal",
	category = "Physical",
	power = 55,
	accuracy = 100,
	pp = 30,
	description = "")

VINE_WHIP = dict(
	element_type = "Grass",
	category = "Physical",
	power = 45,
	accuracy = 100,
	pp = 25,
	description = "")

WATER_GUN = dict(
	element_type = "Water",
	category = "Special",
	power = 40, 
	accuracy = 100,
	pp = 25,
	description = "")

WATERFALL = dict(
 	element_type = "Water",
	category = "Physical",
	power = 80,
	accuracy = 100,
	pp = 15,
	description = "May cause flinching.")

WHIRLWIND = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 20,
	description = "In battles, the opponent switches. In the wild, the Pokemon runs.")

WING_ATTACK = dict(
	element_type = "Flying",
	category = "Physical",
	power = 60,
	accuracy = 100,
	pp = 35,
	description = "")

WITHDRAW = dict(
 	element_type = "Water",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 40,
	description = "Raises user's Defense.")

WRAP = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 15,
	accuracy = 90,
	pp = 20,
	description = "Traps opponent, damaging them for 4-5 turns.")





class Generate (namedtuple("Props", NAMES_STRS)):
	"""Generates moveset properties."""

	def __new__ (self, pokemon_type):
		
		return super(Generate, self).__new__(self, **{})
