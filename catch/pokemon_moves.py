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

ABSORB = dict(
	ELEMENT_TYPE = "Grass",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.GRASS,
	category = "Special",
	POWER = 20,
	accuracy = 100,
	pp = 25,
	description = "User recovers half the HP inflicted on opponent.")

ACID = dict(
	ELEMENT_TYPE = "Poison",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.POISON,
	category = "Special",
	POWER = 40,
	accuracy = 100,
	pp = 30,
	description = "May lower opponent's Special Defense.")

ACID_ARMOUR = dict(
	ELEMENT_TYPE = "Poison",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.POISON,
	category = "Status",
	POWER = None, 
	accuracy = None,
	pp = 20,
	description = "Sharply raises user's Defense.")

AGILITY = dict(
	ELEMENT_TYPE = "Psychic",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.PSYCHIC,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 30,
	description = "Sharply raises user's Speed.")

AMNESIA = dict(
	ELEMENT_TYPE = "Psychic",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.PSYCHIC,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 20,
	description = "Sharply raises user's Special Defense.")

AURORA_BEAM = dict(
	ELEMENT_TYPE = "Ice",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.ICE,
	category = "Special",
	POWER = 65, 
	accuracy = 100,
	pp = 20,
	description = "May lower opponent's Attack.")

BARRAGE = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 15,
	accuracy = 85,
	pp = 20,
	description = "Hits 2-5 times in one turn.")

BARRIER = dict(
 	ELEMENT_TYPE = "Psychic",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.PSYCHIC,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 20,
	description = "Sharply raises user's Defense.")

BIDE = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = None,
	accuracy = None,
	pp = 10,
	description = "User takes damage for two turns then strikes back double.")

BIND = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 15,
	accuracy = 85,
	pp = 20,
	description = "Traps opponent, damaging them for 4-5 turns.")

BITE = dict(
 	ELEMENT_TYPE = "Dark",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.DARK,
	category = "Physical",
	POWER = 60,
	accuracy = 100,
	pp = 25,
	description = "May cause flinching.")

BLIZZARD = dict(
 	ELEMENT_TYPE = "Ice",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.ICE,
	category = "Special",
	POWER = 110,
	accuracy = 70,
	pp = 5,
	description = "May freeze opponent.")

BODY_SLAM = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 85,
	accuracy = 100,
	pp = 15,
	description = "May paralyze opponent.")

BONE_CLUB = dict(
	ELEMENT_TYPE = "Ground",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.GROUND,
	category = "Physical",
	POWER = 65,
	accuracy = 85,
	pp = 20,
	description = "May cause flinching.")

BONEMERANG = dict(
 	ELEMENT_TYPE = "Ground",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.GROUND,
	category = "Physical",
	POWER = 50,
	accuracy = 90,
	pp = 10,
	description = "Hits twice in one turn.")

BUBBLE = dict(
 	ELEMENT_TYPE = "Water",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.WATER,
	category = "Special",
	POWER = 40,
	accuracy = 100,
	pp = 30,
	description = "May lower opponent's Speed.")

BUBBLE_BEAM = dict(
	ELEMENT_TYPE = "Water",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.WATER,
	category = "Special",
	POWER = 65, 
	accuracy = 100,
	pp = 20,
	description = "May lower opponent's Speed.")

CLAMP = dict(
 	ELEMENT_TYPE = "Water",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.WATER,
	category = "Physical",
	POWER = 35,
	accuracy = 85,
	pp = 10,
	description = "Traps opponent, damaging them for 4-5 turns.")

COMET_PUNCH = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 18,
	accuracy = 85,
	pp = 15,
	description = "Hits 2-5 times in one turn.")

CONFUSE_RAY = dict(
	ELEMENT_TYPE = "Ghost",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.GHOST,
	category = "Status",
	POWER = None, 
	accuracy = 100,
	pp = 10,
	description = "Confuses opponent.")

CONFUSION = dict(
 	ELEMENT_TYPE = "Psychic",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.PSYCHIC,
	category = "Special",
	POWER = 50,
	accuracy = 100,
	pp = 25,
	description = "May confuse opponent.")

CONSTRICT = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 10,
	accuracy = 100,
	pp = 35,
	description = "May lower opponent's Speed by one stage.")

CONVERSION = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 30,
	description = "Changes user's type to that of its first move.")

COUNTER = dict(
 	ELEMENT_TYPE = "Fighting",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.FIGHTING,
	category = "Physical",
	POWER = None,
	accuracy = 100,
	pp = 20,
	description = "When hit by a Physical Attack, user strikes back with 2x POWER.")

CRABHAMMER = dict(
 	ELEMENT_TYPE = "Water",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.WATER,
	category = "Physical",
	POWER = 100,
	accuracy = 90,
	pp = 10,
	description = "High critical hit ratio.")

CUT = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 50,
	accuracy = 95,
	pp = 30,
	description = "")

DEFENSE_CURL = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None, 
	accuracy = None,
	pp = 40,
	description = "Raises user's Defense.")

DIG = dict(
 	ELEMENT_TYPE = "Ground",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.GROUND,
	category = "Physical",
	POWER = 80,
	accuracy = 100,
	pp = 10,
	description = "Digs underground on first turn, attacks on second. Can also escape from caves.")

DISABLE = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = 100,
	pp = 20,
	description = "Opponent can't use its last attack for a few turns.")

DIZZY_PUNCH = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 70,
	accuracy = 100,
	pp = 10,
	description = "May confuse opponent.")

DOUBLE_KICK = dict(
	ELEMENT_TYPE = "Fighting",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.FIGHTING,
	category = "Physical",
	POWER = 30,
	accuracy = 100,
	pp = 30,
	description = "Hits twice in one turn.")

DOUBLE_SLAP = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 15,
	accuracy = 85,
	pp = 10,
	description = "Hits 2-5 times in one turn.")

DOUBLE_TEAM = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None, 
	accuracy = None,
	pp = 15,
	description = "Raises user's Evasiveness.")

DOUBLE_EDGE = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 120, 
	accuracy = 100,
	pp = 15,
	description = "User receives recoil damage.")

DRAGON_RAGE = dict(
	ELEMENT_TYPE = "Dragon",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.DRAGON,
	category = "Special",
	POWER = None,
	accuracy = 100,
	pp = 10,
	description = "Always inflicts 40 HP.")

DREAM_EATER = dict(
	ELEMENT_TYPE = "Psychic",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.PSYCHIC,
	category = "Special",
	POWER = 100,
	accuracy = 100,
	pp = 15,
	description = "User recovers half the HP inflicted on a sleeping opponent.")

DRILL_PECK = dict(
	ELEMENT_TYPE = "Flying",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.FLYING,
	category = "Physical",
	POWER = 80,
	accuracy = 100,
	pp = 20,
	description = "")

EARTHQUAKE = dict(
 	ELEMENT_TYPE = "Ground",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.GROUND,
	category = "Physical",
	POWER = 100,
	accuracy = 100,
	pp = 10,
	description = "POWER is doubled if opponent is underground from using Dig.")

EGG_BOMB = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 100, 
	accuracy = 75,
	pp = 10,
	description = "")

EMBER = dict(
 	ELEMENT_TYPE = "Fire",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.FIRE,
	category = "Special",
	POWER = 40,
	accuracy = 100,
	pp = 25,
	description = "May burn opponent.")

EXPLOSION = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 250,
	accuracy = 100,
	pp = 5,
	description = "User faints.")

FIRE_BLAST = dict(
	ELEMENT_TYPE = "Fire",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.FIRE,
	category = "Special",
	POWER = 110, 
	accuracy = 85,
	pp = 5,
	description = "May burn opponent.")

FIRE_PUNCH = dict(
	ELEMENT_TYPE = "Fire",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.FIRE,
	category = "Physical",
	POWER = 75,
	accuracy = 100,
	pp = 15,
	description = "May burn opponent.")

FIRE_SPIN = dict(
	ELEMENT_TYPE = "Fire",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.FIRE,
	category = "Special",
	POWER = 35, 
	accuracy = 85,
	pp = 15,
	description = "Traps opponent, damaging them for 4-5 turns.")

FISSURE = dict(
 	ELEMENT_TYPE = "Ground",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.GROUND,
	category = "Physical",
	POWER = None,
	accuracy = None,
	pp = 5,
	description = "One-Hit-KO, if it hits.")

FLAMETHROWER = dict(
 	ELEMENT_TYPE = "Fire",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.FIRE,
	category = "Special",
	POWER = 90,
	accuracy = 100,
	pp = 15,
	description = "May burn opponent.")

FLASH = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = 100,
	pp = 20,
	description = "Lowers opponent's ACCURACY.")

FLY = dict(
 	ELEMENT_TYPE = "Flying",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.FLYING,
	category = "Physical",
	POWER = 90,
	accuracy = 95,
	pp = 15,
	description = "Flies up on first turn, attacks on second turn.")

FOCUS_ENERGY = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None, 
	accuracy = None,
	pp = 30,
	description = "Increases critical hit ratio.")

FURY_ATTACK = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 15,
	accuracy = 85,
	pp = 20,
	description = "Hits 2-5 times in one turn.")

FURY_SWIPES = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 18,
	accuracy = 80,
	pp = 15,
	description = "Hits 2-5 times in one turn.")

GLARE = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = 100,
	pp = 30,
	description = "Paralyzes opponent.")

GROWL = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = 100,
	pp = 40,
	description = "Lowers opponent's Attack.")

GROWTH = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 40,
	description = "Raises user's Attack and Special Attack.")

GUILLOTINE = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = None,
	accuracy = None,
	pp = 5,
	description = "One-Hit-KO, if it hits.")

GUST = dict(
 	ELEMENT_TYPE = "Flying",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.FLYING,
	category = "Special",
	POWER = 40,
	accuracy = 100,
	pp = 35,
	description = "Hits Pokemon using Fly/Bounce with double POWER.")

HARDEN = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 30,
	description = "Raises user's Defense.")

HAZE = dict(
 	ELEMENT_TYPE = "Ice",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.ICE,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 30,
	description = "Resets all stat changes.")

HEADBUTT = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 70,
	accuracy = 100,
	pp = 15,
	description = "May cause flinching.")

HIGH_JUMP_KICK = dict(
	ELEMENT_TYPE = "Fighting",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.FIGHTING,
	category = "Physical",
	POWER = 130, 
	accuracy = 90,
	pp = 10,
	description = "If it misses, the user loses half their HP.")

HORN_ATTACK = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 65,
	accuracy = 100,
	pp = 25,
	description = "")

HORN_DRILL = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = None,
	accuracy = None,
	pp = 5,
	description = "One-Hit-KO, if it hits.")

HYDRO_PUMP = dict(
	ELEMENT_TYPE = "Water",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.WATER,
	category = "Special",
	POWER = 110, 
	accuracy = 80,
	pp = 5,
	description = "")

HYPER_BEAM = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Special",
	POWER = 150, 
	accuracy = 90,
	pp = 5,
	description = "User must recharge next turn.")

HYPER_Fang = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 80,
	accuracy = 90,
	pp = 15,
	description = "May cause flinching.")

HYPNOSIS = dict(
 	ELEMENT_TYPE = "Psychic",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.PSYCHIC,
	category = "Status",
	POWER = None,
	accuracy = 60,
	pp = 20,
	description = "Puts opponent to sleep.")

ICE_BEAM = dict(
	ELEMENT_TYPE = "Ice",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.ICE,
	category = "Special",
	POWER = 90, 
	accuracy = 100,
	pp = 10,
	description = "May freeze opponent.")

ICE_PUNCH = dict(
	ELEMENT_TYPE = "Ice",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.ICE,
	category = "Physical",
	POWER = 75,
	accuracy = 100,
	pp = 15,
	description = "May freeze opponent.")

JUMP_KICK = dict(
	ELEMENT_TYPE = "Fighting",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.FIGHTING,
	category = "Physical",
	POWER = 100, 
	accuracy = 95,
	pp = 10,
	description = "If it misses, the user loses half their HP.")

KARATE_CHOP = dict(
	ELEMENT_TYPE = "Fighting",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.FIGHTING,
	category = "Physical",
	POWER = 50,
	accuracy = 100,
	pp = 25,
	description = "High critical hit ratio.")

KINESIS = dict(
 	ELEMENT_TYPE = "Psychic",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.PSYCHIC,
	category = "Status",
	POWER = None,
	accuracy = 80,
	pp = 15,
	description = "Lowers opponent's ACCURACY.")

LEECH_LIFE = dict(
	ELEMENT_TYPE = "Bug",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.BUG,
	category = "Physical",
	POWER = 80,
	accuracy = 100,
	pp = 10,
	description = "User recovers half the HP inflicted on opponent.")

LEECH_SEED = dict(
	ELEMENT_TYPE = "Grass",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.GRASS,
	category = "Status",
	POWER = None, 
	accuracy = 90,
	pp = 10,
	description = "User steals HP from opponent each turn.")

LEER = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = 100,
	pp = 30,
	description = "Lowers opponent's Defense.")

LICK = dict(
 	ELEMENT_TYPE = "Ghost",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.GHOST,
	category = "Physical",
	POWER = 30,
	accuracy = 100,
	pp = 30,
	description = "May paralyze opponent.")

LIGHT_SCREEN = dict(
	ELEMENT_TYPE = "Psychic",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.PSYCHIC,
	category = "Status",
	POWER = None, 
	accuracy = None,
	pp = 30,
	description = "Halves damage from Special attacks for 5 turns.")

LOVELY_KISS = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None, 
	accuracy = 75,
	pp = 10,
	description = "Puts opponent to sleep.")

LOW_KICK = dict(
	ELEMENT_TYPE = "Fighting",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.FIGHTING,
	category = "Physical",
	POWER = None,
	accuracy = 100,
	pp = 20,
	description = "The heavier the opponent, the stronger the attack.")

MEDITATE = dict(
 	ELEMENT_TYPE = "Psychic",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.PSYCHIC,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 40,
	description = "Raises user's Attack.")

MEGA_DRAIN = dict(
	ELEMENT_TYPE = "Grass",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.GRASS,
	category = "Special",
	POWER = 40, 
	accuracy = 100,
	pp = 15,
	description = "User recovers half the HP inflicted on opponent.")

MEGA_KICK = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 120, 
	accuracy = 75,
	pp = 5,
	description = "")

MEGA_PUNCH = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 80,
	accuracy = 85,
	pp = 20,
	description = "")

METRONOME = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 10,
	description = "User performs any move in the game at random.")

MIMIC = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 10,
	description = "Copies the opponent's last move.")

MINIMIZE = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 10,
	description = "Sharply raises user's Evasiveness.")

MIRROR_MOVE = dict(
	ELEMENT_TYPE = "Flying",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.FLYING,
	category = "Status",
	POWER = None, 
	accuracy = None,
	pp = 20,
	description = "User performs the opponent's last move.")

MIST = dict(
 	ELEMENT_TYPE = "Ice",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.ICE,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 30,
	description = "User's stats cannot be changed for a period of time.")

NIGHT_SHADE = dict(
	ELEMENT_TYPE = "Ghost",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.GHOST,
	category = "Special",
	POWER = None,
	accuracy = 100,
	pp = 15,
	description = "Inflicts damage equal to user's level.")

PAY_DAY = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 40,
	accuracy = 100,
	pp = 20,
	description = "A small amount of money is gained after the battle resolves.")

PECK = dict(
 	ELEMENT_TYPE = "Flying",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.FLYING,
	category = "Physical",
	POWER = 35,
	accuracy = 100,
	pp = 35,
	description = "")

PETAL_DANCE = dict(
	ELEMENT_TYPE = "Grass",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.GRASS,
	category = "Special",
	POWER = 120, 
	accuracy = 100,
	pp = 10,
	description = "User attacks for 2-3 turns but then becomes confused.")

PIN_MISSILE = dict(
	ELEMENT_TYPE = "Bug",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.BUG,
	category = "Physical",
	POWER = 25,
	accuracy = 95,
	pp = 20,
	description = "Hits 2-5 times in one turn.")

POISON_GAS = dict(
	ELEMENT_TYPE = "Poison",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.POISON,
	category = "Status",
	POWER = None, 
	accuracy = 90,
	pp = 40,
	description = "Poisons opponent.")

POISON_POWDER = dict(
	ELEMENT_TYPE = "Poison",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.POISON,
	category = "Status",
	POWER = None, 
	accuracy = 75,
	pp = 35,
	description = "Poisons opponent.")

POISON_STING = dict(
	ELEMENT_TYPE = "Poison",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.POISON,
	category = "Physical",
	POWER = 15,
	accuracy = 100,
	pp = 35,
	description = "May poison the opponent.")

POUND = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 40,
	accuracy = 100,
	pp = 35,
	description = "")

PSYBEAM = dict(
 	ELEMENT_TYPE = "Psychic",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.PSYCHIC,
	category = "Special",
	POWER = 65,
	accuracy = 100,
	pp = 20,
	description = "May confuse opponent.")

PSYCHIC = dict(
 	ELEMENT_TYPE = "Psychic",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.PSYCHIC,
	category = "Special",
	POWER = 90,
	accuracy = 100,
	pp = 10,
	description = "May lower opponent's Special Defense.")

PSYWAVE = dict(
 	ELEMENT_TYPE = "Psychic",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.PSYCHIC,
	category = "Special",
	POWER = None,
	accuracy = 80,
	pp = 15,
	description = "Inflicts damage 50-150% of user's level.")

QUICK_ATTACK = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 40,
	accuracy = 100,
	pp = 30,
	description = "User attacks first.")

RAGE = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 20,
	accuracy = 100,
	pp = 20,
	description = "Raises user's Attack when hit.")

RAZOR_LEAF = dict(
	ELEMENT_TYPE = "Grass",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.GRASS,
	category = "Physical",
	POWER = 55,
	accuracy = 95,
	pp = 25,
	description = "High critical hit ratio.")

RAZOR_WIND = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Special",
	POWER = 80, 
	accuracy = 100,
	pp = 10,
	description = "Charges on first turn, attacks on second. High critical hit ratio.")

RECOVER = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 10,
	description = "User recovers half its max HP.")

REFLECT = dict(
 	ELEMENT_TYPE = "Psychic",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.PSYCHIC,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 20,
	description = "Halves damage from Physical attacks for 5 turns.")

REST = dict(
 	ELEMENT_TYPE = "Psychic",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.PSYCHIC,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 10,
	description = "User sleeps for 2 turns, but user is fully healed.")

ROAR = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 20,
	description = "In battles, the opponent switches. In the wild, the Pokemon runs.")

ROCK_SLIDE = dict(
	ELEMENT_TYPE = "Rock",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.ROCK,
	category = "Physical",
	POWER = 75,
	accuracy = 90,
	pp = 10,
	description = "May cause flinching.")

ROCK_THROW = dict(
	ELEMENT_TYPE = "Rock",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.ROCK,
	category = "Physical",
	POWER = 50,
	accuracy = 90,
	pp = 15,
	description = "")

ROLLING_KICK = dict(
	ELEMENT_TYPE = "Fighting",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.FIGHTING,
	category = "Physical",
	POWER = 60,
	accuracy = 85,
	pp = 15,
	description = "May cause flinching.")

SAND_ATTACK = dict(
	ELEMENT_TYPE = "Ground",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.GROUND,
	category = "Status",
	POWER = None, 
	accuracy = 100,
	pp = 15,
	description = "Lowers opponent's ACCURACY.")

SCRATCH = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 40,
	accuracy = 100,
	pp = 35,
	description = "")

SCREECH = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = 85,
	pp = 40,
	description = "Sharply lowers opponent's Defense.")

SEISMIC_TOSS = dict(
	ELEMENT_TYPE = "Fighting",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.FIGHTING,
	category = "Physical",
	POWER = None,
	accuracy = 100,
	pp = 20,
	description = "Inflicts damage equal to user's level.")

SELF_DESTRUCT = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 200, 
	accuracy = 100,
	pp = 5,
	description = "User faints.")

SHARPEN = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 30,
	description = "Raises user's Attack.")

SING = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = 55,
	pp = 15,
	description = "Puts opponent to sleep.")

SKULL_BASH = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 130, 
	accuracy = 100,
	pp = 10,
	description = "Raises Defense on first turn, attacks on second.")

SKY_ATTACK = dict(
	ELEMENT_TYPE = "Flying",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.FLYING,
	category = "Physical",
	POWER = 140, 
	accuracy = 90,
	pp = 5,
	description = "Charges on first turn, attacks on second. May cause flinching.")

SLAM = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 80,
	accuracy = 75,
	pp = 20,
	description = "")

SLASH = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 70,
	accuracy = 100,
	pp = 20,
	description = "High critical hit ratio.")

SLEEP_POWDER = dict(
	ELEMENT_TYPE = "Grass",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.GRASS,
	category = "Status",
	POWER = None, 
	accuracy = 75,
	pp = 15,
	description = "Puts opponent to sleep.")

SLUDGE = dict(
 	ELEMENT_TYPE = "Poison",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.POISON,
	category = "Special",
	POWER = 65,
	accuracy = 100,
	pp = 20,
	description = "May poison opponent.")

SMOG = dict(
 	ELEMENT_TYPE = "Poison",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.POISON,
	category = "Special",
	POWER = 30,
	accuracy = 70,
	pp = 20,
	description = "May poison opponent.")

SMOKESCREEN = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = 100,
	pp = 20,
	description = "Lowers opponent's ACCURACY.")

SOFT_BOILED = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None, 
	accuracy = None,
	pp = 10,
	description = "User recovers half its max HP.")

SOLAR_BEAM = dict(
	ELEMENT_TYPE = "Grass",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.GRASS,
	category = "Special",
	POWER = 120, 
	accuracy = 100,
	pp = 10,
	description = "Charges on first turn, attacks on second.")

SONIC_BOOM = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Special",
	POWER = None,
	accuracy = 90,
	pp = 20,
	description = "Always inflicts 20 HP.")

SPIKE_CANNON = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 20,
	accuracy = 100,
	pp = 15,
	description = "Hits 2-5 times in one turn.")

SPLASH = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 40,
	description = "Doesn't do ANYTHING.")

SPORE = dict(
 	ELEMENT_TYPE = "Grass",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.GRASS,
	category = "Status",
	POWER = None,
	accuracy = 100,
	pp = 15,
	description = "Puts opponent to sleep.")

STOMP = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 65,
	accuracy = 100,
	pp = 20,
	description = "May cause flinching.")

STRENGTH = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 80,
	accuracy = 100,
	pp = 15,
	description = "")

STRING_SHOT = dict(
	ELEMENT_TYPE = "Bug",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.BUG,
	category = "Status",
	POWER = None, 
	accuracy = 95,
	pp = 40,
	description = "Sharply lowers opponent's Speed.")

STRUGGLE = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 50,
	accuracy = 100,
	pp = None,
	description = "Only usable when all PP are gone. Hurts the user.")

STUN_SPORE = dict(
	ELEMENT_TYPE = "Grass",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.GRASS,
	category = "Status",
	POWER = None, 
	accuracy = 75,
	pp = 30,
	description = "Paralyzes opponent.")

SUBMISSION = dict(
 	ELEMENT_TYPE = "Fighting",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.FIGHTING,
	category = "Physical",
	POWER = 80,
	accuracy = 80,
	pp = 20,
	description = "User receives recoil damage.")

SUBSTITUTE = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 10,
	description = "Uses HP to creates a decoy that takes hits.")

SUPER_FANG = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = None,
	accuracy = 90,
	pp = 10,
	description = "Always takes off half of the opponent's HP.")

SUPERSONIC = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = 55,
	pp = 20,
	description = "Confuses opponent.")

SURF = dict(
 	ELEMENT_TYPE = "Water",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.WATER,
	category = "Special",
	POWER = 90,
	accuracy = 100,
	pp = 15,
	description = "Hits all adjacent Pokemon.")

SWIFT = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Special",
	POWER = 60,
	accuracy = 100,
	pp = 20,
	description = "Ignores ACCURACY and Evasiveness.")

SWORDS_DANCE = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None, 
	accuracy = None,
	pp = 20,
	description = "Sharply raises user's Attack.")

TACKLE = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 40,
	accuracy = 100,
	pp = 35,
	description = "")

TAIL_WHIP = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None, 
	accuracy = 100,
	pp = 30,
	description = "Lowers opponent's Defense.")

TAKE_DOWN = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 90,
	accuracy = 85,
	pp = 20,
	description = "User receives recoil damage.")

TELEPORT = dict(
 	ELEMENT_TYPE = "Psychic",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.PSYCHIC,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 20,
	description = "Allows user to flee wild battles; also warps player to last PokeCenter.")

THRASH = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 120,
	accuracy = 100,
	pp = 10,
	description = "User attacks for 2-3 turns but then becomes confused.")

THUNDER = dict(
 	ELEMENT_TYPE = "Electric",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.ELECTRIC,
	category = "Special",
	POWER = 110,
	accuracy = 70,
	pp = 10,
	description = "May paralyze opponent.")

THUNDER_PUNCH = dict(
	ELEMENT_TYPE = "Electric",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.ELECTRIC,
	category = "Physical",
	POWER = 75,
	accuracy = 100,
	pp = 15,
	description = "May paralyze opponent.")

THUNDER_SHOCK = dict(
	ELEMENT_TYPE = "Electric",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.ELECTRIC,
	category = "Special",
	POWER = 40, 
	accuracy = 100,
	pp = 30,
	description = "May paralyze opponent.")

THUNDER_WAVE = dict(
	ELEMENT_TYPE = "Electric",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.ELECTRIC,
	category = "Status",
	POWER = None, 
	accuracy = 90,
	pp = 20,
	description = "Paralyzes opponent.")

THUNDERBOLT = dict(
 	ELEMENT_TYPE = "Electric",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.ELECTRIC,
	category = "Special",
	POWER = 90,
	accuracy = 100,
	pp = 15,
	description = "May paralyze opponent.")

TOXIC = dict(
 	ELEMENT_TYPE = "Poison",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.POISON,
	category = "Status",
	POWER = None,
	accuracy = 90,
	pp = 10,
	description = "Badly poisons opponent.")

TRANSFORM = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 10,
	description = "User takes on the form and attacks of the opponent.")

TRI_ATTACK = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Special",
	POWER = 80, 
	accuracy = 100,
	pp = 10,
	description = "May paralyze, burn or freeze opponent.")

TWINEEDLE = dict(
 	ELEMENT_TYPE = "Bug",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.BUG,
	category = "Physical",
	POWER = 25,
	accuracy = 100,
	pp = 20,
	description = "Hits twice in one turn. May poison opponent.")

VICE_GRIP = dict(
	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 55,
	accuracy = 100,
	pp = 30,
	description = "")

VINE_WHIP = dict(
	ELEMENT_TYPE = "Grass",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.GRASS,
	category = "Physical",
	POWER = 45,
	accuracy = 100,
	pp = 25,
	description = "")

WATER_GUN = dict(
	ELEMENT_TYPE = "Water",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.WATER,
	category = "Special",
	POWER = 40, 
	accuracy = 100,
	pp = 25,
	description = "")

WATERFALL = dict(
 	ELEMENT_TYPE = "Water",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.WATER,
	category = "Physical",
	POWER = 80,
	accuracy = 100,
	pp = 15,
	description = "May cause flinching.")

WHIRLWIND = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 20,
	description = "In battles, the opponent switches. In the wild, the Pokemon runs.")

WING_ATTACK = dict(
	ELEMENT_TYPE = "Flying",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.FLYING,
	category = "Physical",
	POWER = 60,
	accuracy = 100,
	pp = 35,
	description = "")

WITHDRAW = dict(
 	ELEMENT_TYPE = "Water",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.WATER,
	category = "Status",
	POWER = None,
	accuracy = None,
	pp = 40,
	description = "Raises user's Defense.")

WRAP = dict(
 	ELEMENT_TYPE = "Normal",
	ELEMENT_TYPE_PROPERTIES = pokemon_types.NORMAL,
	category = "Physical",
	POWER = 15,
	accuracy = 90,
	pp = 20,
	description = "Traps opponent, damaging them for 4-5 turns.")

"""Dictionary containing the primary Pokemon moves.

Key contains collection of dictionaries containing move properties and statistics.
"""

GROUPS = {
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

"""Tuple containing strings of Pokemon moves.

Names are generated from initialised names. Requires Pokemon move is defined in Moveset dictionary.
"""

NAMES = tuple(dict.keys(GROUPS))

"""String comprised of the different Pokemon moves."""

NAMES_STRS = " ".join(NAMES)


class Generate (namedtuple("Props", NAMES_STRS)):
	"""Generates moveset properties."""

	def __new__ (self, pokemon_type):
		
		return super(Generate, self).__new__(self, **{})
