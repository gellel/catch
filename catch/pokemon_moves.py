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
	element_type = "Grass",
	element_type_data = pokemon_types.Grass(),
	category = "Special",
	power = 20,
	accuracy = 100,
	pp = 25,
	description = "User recovers half the HP inflicted on opponent.")

ACID = dict(
	element_type = "Poison",
	element_type_data = pokemon_types.Poison(),
	category = "Special",
	power = 40,
	accuracy = 100,
	pp = 30,
	description = "May lower opponent's Special Defense.")

ACID_ARMOUR = dict(
	element_type = "Poison",
	element_type_data = pokemon_types.Poison(),
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 20,
	description = "Sharply raises user's Defense.")

AGILITY = dict(
	element_type = "Psychic",
	element_type_data = pokemon_types.Psychic(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 30,
	description = "Sharply raises user's Speed.")

AMNESIA = dict(
	element_type = "Psychic",
	element_type_data = pokemon_types.Psychic(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 20,
	description = "Sharply raises user's Special Defense.")

AURORA_BEAM = dict(
	element_type = "Ice",
	element_type_data = pokemon_types.Ice(),
	category = "Special",
	power = 65, 
	accuracy = 100,
	pp = 20,
	description = "May lower opponent's Attack.")

BARRAGE = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 15,
	accuracy = 85,
	pp = 20,
	description = "Hits 2-5 times in one turn.")

BARRIER = dict(
 	element_type = "Psychic",
	element_type_data = pokemon_types.Psychic(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 20,
	description = "Sharply raises user's Defense.")

BIDE = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = None,
	accuracy = None,
	pp = 10,
	description = "User takes damage for two turns then strikes back double.")

BIND = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 15,
	accuracy = 85,
	pp = 20,
	description = "Traps opponent, damaging them for 4-5 turns.")

BITE = dict(
 	element_type = "Dark",
	element_type_data = pokemon_types.Dark(),
	category = "Physical",
	power = 60,
	accuracy = 100,
	pp = 25,
	description = "May cause flinching.")

BLIZZARD = dict(
 	element_type = "Ice",
	element_type_data = pokemon_types.Ice(),
	category = "Special",
	power = 110,
	accuracy = 70,
	pp = 5,
	description = "May freeze opponent.")

BODY_SLAM = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 85,
	accuracy = 100,
	pp = 15,
	description = "May paralyze opponent.")

BONE_CLUB = dict(
	element_type = "Ground",
	element_type_data = pokemon_types.Ground(),
	category = "Physical",
	power = 65,
	accuracy = 85,
	pp = 20,
	description = "May cause flinching.")

BONEMERANG = dict(
 	element_type = "Ground",
	element_type_data = pokemon_types.Ground(),
	category = "Physical",
	power = 50,
	accuracy = 90,
	pp = 10,
	description = "Hits twice in one turn.")

BUBBLE = dict(
 	element_type = "Water",
	element_type_data = pokemon_types.Water(),
	category = "Special",
	power = 40,
	accuracy = 100,
	pp = 30,
	description = "May lower opponent's Speed.")

BUBBLE_BEAM = dict(
	element_type = "Water",
	element_type_data = pokemon_types.Water(),
	category = "Special",
	power = 65, 
	accuracy = 100,
	pp = 20,
	description = "May lower opponent's Speed.")

CLAMP = dict(
 	element_type = "Water",
	element_type_data = pokemon_types.Water(),
	category = "Physical",
	power = 35,
	accuracy = 85,
	pp = 10,
	description = "Traps opponent, damaging them for 4-5 turns.")

COMET_PUNCH = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 18,
	accuracy = 85,
	pp = 15,
	description = "Hits 2-5 times in one turn.")

CONFUSE_RAY = dict(
	element_type = "Ghost",
	element_type_data = pokemon_types.Ghost(),
	category = "Status",
	power = None, 
	accuracy = 100,
	pp = 10,
	description = "Confuses opponent.")

CONFUSION = dict(
 	element_type = "Psychic",
	element_type_data = pokemon_types.Psychic(),
	category = "Special",
	power = 50,
	accuracy = 100,
	pp = 25,
	description = "May confuse opponent.")

CONSTRICT = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 10,
	accuracy = 100,
	pp = 35,
	description = "May lower opponent's Speed by one stage.")

CONVERSION = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 30,
	description = "Changes user's type to that of its first move.")

COUNTER = dict(
 	element_type = "Fighting",
	element_type_data = pokemon_types.Fighting(),
	category = "Physical",
	power = None,
	accuracy = 100,
	pp = 20,
	description = "When hit by a Physical Attack, user strikes back with 2x POWER.")

CRABHAMMER = dict(
 	element_type = "Water",
	element_type_data = pokemon_types.Water(),
	category = "Physical",
	power = 100,
	accuracy = 90,
	pp = 10,
	description = "High critical hit ratio.")

CUT = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 50,
	accuracy = 95,
	pp = 30,
	description = "")

DEFENSE_CURL = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 40,
	description = "Raises user's Defense.")

DIG = dict(
 	element_type = "Ground",
	element_type_data = pokemon_types.Ground(),
	category = "Physical",
	power = 80,
	accuracy = 100,
	pp = 10,
	description = "Digs underground on first turn, attacks on second. Can also escape from caves.")

DISABLE = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = 100,
	pp = 20,
	description = "Opponent can't use its last attack for a few turns.")

DIZZY_PUNCH = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 70,
	accuracy = 100,
	pp = 10,
	description = "May confuse opponent.")

DOUBLE_KICK = dict(
	element_type = "Fighting",
	element_type_data = pokemon_types.Fighting(),
	category = "Physical",
	power = 30,
	accuracy = 100,
	pp = 30,
	description = "Hits twice in one turn.")

DOUBLE_SLAP = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 15,
	accuracy = 85,
	pp = 10,
	description = "Hits 2-5 times in one turn.")

DOUBLE_TEAM = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 15,
	description = "Raises user's Evasiveness.")

DOUBLE_EDGE = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 120, 
	accuracy = 100,
	pp = 15,
	description = "User receives recoil damage.")

DRAGON_RAGE = dict(
	element_type = "Dragon",
	element_type_data = pokemon_types.Dragon(),
	category = "Special",
	power = None,
	accuracy = 100,
	pp = 10,
	description = "Always inflicts 40 HP.")

DREAM_EATER = dict(
	element_type = "Psychic",
	element_type_data = pokemon_types.Psychic(),
	category = "Special",
	power = 100,
	accuracy = 100,
	pp = 15,
	description = "User recovers half the HP inflicted on a sleeping opponent.")

DRILL_PECK = dict(
	element_type = "Flying",
	element_type_data = pokemon_types.Flying(),
	category = "Physical",
	power = 80,
	accuracy = 100,
	pp = 20,
	description = "")

EARTHQUAKE = dict(
 	element_type = "Ground",
	element_type_data = pokemon_types.Ground(),
	category = "Physical",
	power = 100,
	accuracy = 100,
	pp = 10,
	description = "POWER is doubled if opponent is underground from using Dig.")

EGG_BOMB = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 100, 
	accuracy = 75,
	pp = 10,
	description = "")

EMBER = dict(
 	element_type = "Fire",
	element_type_data = pokemon_types.Fire(),
	category = "Special",
	power = 40,
	accuracy = 100,
	pp = 25,
	description = "May burn opponent.")

EXPLOSION = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 250,
	accuracy = 100,
	pp = 5,
	description = "User faints.")

FIRE_BLAST = dict(
	element_type = "Fire",
	element_type_data = pokemon_types.Fire(),
	category = "Special",
	power = 110, 
	accuracy = 85,
	pp = 5,
	description = "May burn opponent.")

FIRE_PUNCH = dict(
	element_type = "Fire",
	element_type_data = pokemon_types.Fire(),
	category = "Physical",
	power = 75,
	accuracy = 100,
	pp = 15,
	description = "May burn opponent.")

FIRE_SPIN = dict(
	element_type = "Fire",
	element_type_data = pokemon_types.Fire(),
	category = "Special",
	power = 35, 
	accuracy = 85,
	pp = 15,
	description = "Traps opponent, damaging them for 4-5 turns.")

FISSURE = dict(
 	element_type = "Ground",
	element_type_data = pokemon_types.Ground(),
	category = "Physical",
	power = None,
	accuracy = None,
	pp = 5,
	description = "One-Hit-KO, if it hits.")

FLAMETHROWER = dict(
 	element_type = "Fire",
	element_type_data = pokemon_types.Fire(),
	category = "Special",
	power = 90,
	accuracy = 100,
	pp = 15,
	description = "May burn opponent.")

FLASH = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = 100,
	pp = 20,
	description = "Lowers opponent's ACCURACY.")

FLY = dict(
 	element_type = "Flying",
	element_type_data = pokemon_types.Flying(),
	category = "Physical",
	power = 90,
	accuracy = 95,
	pp = 15,
	description = "Flies up on first turn, attacks on second turn.")

FOCUS_ENERGY = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 30,
	description = "Increases critical hit ratio.")

FURY_ATTACK = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 15,
	accuracy = 85,
	pp = 20,
	description = "Hits 2-5 times in one turn.")

FURY_SWIPES = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 18,
	accuracy = 80,
	pp = 15,
	description = "Hits 2-5 times in one turn.")

GLARE = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = 100,
	pp = 30,
	description = "Paralyzes opponent.")

GROWL = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = 100,
	pp = 40,
	description = "Lowers opponent's Attack.")

GROWTH = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 40,
	description = "Raises user's Attack and Special Attack.")

GUILLOTINE = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = None,
	accuracy = None,
	pp = 5,
	description = "One-Hit-KO, if it hits.")

GUST = dict(
 	element_type = "Flying",
	element_type_data = pokemon_types.Flying(),
	category = "Special",
	power = 40,
	accuracy = 100,
	pp = 35,
	description = "Hits Pokemon using Fly/Bounce with double POWER.")

HARDEN = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 30,
	description = "Raises user's Defense.")

HAZE = dict(
 	element_type = "Ice",
	element_type_data = pokemon_types.Ice(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 30,
	description = "Resets all stat changes.")

HEADBUTT = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 70,
	accuracy = 100,
	pp = 15,
	description = "May cause flinching.")

HIGH_JUMP_KICK = dict(
	element_type = "Fighting",
	element_type_data = pokemon_types.Fighting(),
	category = "Physical",
	power = 130, 
	accuracy = 90,
	pp = 10,
	description = "If it misses, the user loses half their HP.")

HORN_ATTACK = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 65,
	accuracy = 100,
	pp = 25,
	description = "")

HORN_DRILL = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = None,
	accuracy = None,
	pp = 5,
	description = "One-Hit-KO, if it hits.")

HYDRO_PUMP = dict(
	element_type = "Water",
	element_type_data = pokemon_types.Water(),
	category = "Special",
	power = 110, 
	accuracy = 80,
	pp = 5,
	description = "")

HYPER_BEAM = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Special",
	power = 150, 
	accuracy = 90,
	pp = 5,
	description = "User must recharge next turn.")

HYPER_Fang = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 80,
	accuracy = 90,
	pp = 15,
	description = "May cause flinching.")

HYPNOSIS = dict(
 	element_type = "Psychic",
	element_type_data = pokemon_types.Psychic(),
	category = "Status",
	power = None,
	accuracy = 60,
	pp = 20,
	description = "Puts opponent to sleep.")

ICE_BEAM = dict(
	element_type = "Ice",
	element_type_data = pokemon_types.Ice(),
	category = "Special",
	power = 90, 
	accuracy = 100,
	pp = 10,
	description = "May freeze opponent.")

ICE_PUNCH = dict(
	element_type = "Ice",
	element_type_data = pokemon_types.Ice(),
	category = "Physical",
	power = 75,
	accuracy = 100,
	pp = 15,
	description = "May freeze opponent.")

JUMP_KICK = dict(
	element_type = "Fighting",
	element_type_data = pokemon_types.Fighting(),
	category = "Physical",
	power = 100, 
	accuracy = 95,
	pp = 10,
	description = "If it misses, the user loses half their HP.")

KARATE_CHOP = dict(
	element_type = "Fighting",
	element_type_data = pokemon_types.Fighting(),
	category = "Physical",
	power = 50,
	accuracy = 100,
	pp = 25,
	description = "High critical hit ratio.")

KINESIS = dict(
 	element_type = "Psychic",
	element_type_data = pokemon_types.Psychic(),
	category = "Status",
	power = None,
	accuracy = 80,
	pp = 15,
	description = "Lowers opponent's ACCURACY.")

LEECH_LIFE = dict(
	element_type = "Bug",
	element_type_data = pokemon_types.Bug(),
	category = "Physical",
	power = 80,
	accuracy = 100,
	pp = 10,
	description = "User recovers half the HP inflicted on opponent.")

LEECH_SEED = dict(
	element_type = "Grass",
	element_type_data = pokemon_types.Grass(),
	category = "Status",
	power = None, 
	accuracy = 90,
	pp = 10,
	description = "User steals HP from opponent each turn.")

LEER = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = 100,
	pp = 30,
	description = "Lowers opponent's Defense.")

LICK = dict(
 	element_type = "Ghost",
	element_type_data = pokemon_types.Ghost(),
	category = "Physical",
	power = 30,
	accuracy = 100,
	pp = 30,
	description = "May paralyze opponent.")

LIGHT_SCREEN = dict(
	element_type = "Psychic",
	element_type_data = pokemon_types.Psychic(),
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 30,
	description = "Halves damage from Special attacks for 5 turns.")

LOVELY_KISS = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None, 
	accuracy = 75,
	pp = 10,
	description = "Puts opponent to sleep.")

LOW_KICK = dict(
	element_type = "Fighting",
	element_type_data = pokemon_types.Fighting(),
	category = "Physical",
	power = None,
	accuracy = 100,
	pp = 20,
	description = "The heavier the opponent, the stronger the attack.")

MEDITATE = dict(
 	element_type = "Psychic",
	element_type_data = pokemon_types.Psychic(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 40,
	description = "Raises user's Attack.")

MEGA_DRAIN = dict(
	element_type = "Grass",
	element_type_data = pokemon_types.Grass(),
	category = "Special",
	power = 40, 
	accuracy = 100,
	pp = 15,
	description = "User recovers half the HP inflicted on opponent.")

MEGA_KICK = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 120, 
	accuracy = 75,
	pp = 5,
	description = "")

MEGA_PUNCH = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 80,
	accuracy = 85,
	pp = 20,
	description = "")

METRONOME = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 10,
	description = "User performs any move in the game at random.")

MIMIC = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 10,
	description = "Copies the opponent's last move.")

MINIMIZE = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 10,
	description = "Sharply raises user's Evasiveness.")

MIRROR_MOVE = dict(
	element_type = "Flying",
	element_type_data = pokemon_types.Flying(),
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 20,
	description = "User performs the opponent's last move.")

MIST = dict(
 	element_type = "Ice",
	element_type_data = pokemon_types.Ice(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 30,
	description = "User's stats cannot be changed for a period of time.")

NIGHT_SHADE = dict(
	element_type = "Ghost",
	element_type_data = pokemon_types.Ghost(),
	category = "Special",
	power = None,
	accuracy = 100,
	pp = 15,
	description = "Inflicts damage equal to user's level.")

PAY_DAY = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 40,
	accuracy = 100,
	pp = 20,
	description = "A small amount of money is gained after the battle resolves.")

PECK = dict(
 	element_type = "Flying",
	element_type_data = pokemon_types.Flying(),
	category = "Physical",
	power = 35,
	accuracy = 100,
	pp = 35,
	description = "")

PETAL_DANCE = dict(
	element_type = "Grass",
	element_type_data = pokemon_types.Grass(),
	category = "Special",
	power = 120, 
	accuracy = 100,
	pp = 10,
	description = "User attacks for 2-3 turns but then becomes confused.")

PIN_MISSILE = dict(
	element_type = "Bug",
	element_type_data = pokemon_types.Bug(),
	category = "Physical",
	power = 25,
	accuracy = 95,
	pp = 20,
	description = "Hits 2-5 times in one turn.")

POISON_GAS = dict(
	element_type = "Poison",
	element_type_data = pokemon_types.Poison(),
	category = "Status",
	power = None, 
	accuracy = 90,
	pp = 40,
	description = "Poisons opponent.")

POISON_POWDER = dict(
	element_type = "Poison",
	element_type_data = pokemon_types.Poison(),
	category = "Status",
	power = None, 
	accuracy = 75,
	pp = 35,
	description = "Poisons opponent.")

POISON_STING = dict(
	element_type = "Poison",
	element_type_data = pokemon_types.Poison(),
	category = "Physical",
	power = 15,
	accuracy = 100,
	pp = 35,
	description = "May poison the opponent.")

POUND = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 40,
	accuracy = 100,
	pp = 35,
	description = "")

PSYBEAM = dict(
 	element_type = "Psychic",
	element_type_data = pokemon_types.Psychic(),
	category = "Special",
	power = 65,
	accuracy = 100,
	pp = 20,
	description = "May confuse opponent.")

PSYCHIC = dict(
 	element_type = "Psychic",
	element_type_data = pokemon_types.Psychic(),
	category = "Special",
	power = 90,
	accuracy = 100,
	pp = 10,
	description = "May lower opponent's Special Defense.")

PSYWAVE = dict(
 	element_type = "Psychic",
	element_type_data = pokemon_types.Psychic(),
	category = "Special",
	power = None,
	accuracy = 80,
	pp = 15,
	description = "Inflicts damage 50-150% of user's level.")

QUICK_ATTACK = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 40,
	accuracy = 100,
	pp = 30,
	description = "User attacks first.")

RAGE = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 20,
	accuracy = 100,
	pp = 20,
	description = "Raises user's Attack when hit.")

RAZOR_LEAF = dict(
	element_type = "Grass",
	element_type_data = pokemon_types.Grass(),
	category = "Physical",
	power = 55,
	accuracy = 95,
	pp = 25,
	description = "High critical hit ratio.")

RAZOR_WIND = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Special",
	power = 80, 
	accuracy = 100,
	pp = 10,
	description = "Charges on first turn, attacks on second. High critical hit ratio.")

RECOVER = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 10,
	description = "User recovers half its max HP.")

REFLECT = dict(
 	element_type = "Psychic",
	element_type_data = pokemon_types.Psychic(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 20,
	description = "Halves damage from Physical attacks for 5 turns.")

REST = dict(
 	element_type = "Psychic",
	element_type_data = pokemon_types.Psychic(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 10,
	description = "User sleeps for 2 turns, but user is fully healed.")

ROAR = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 20,
	description = "In battles, the opponent switches. In the wild, the Pokemon runs.")

ROCK_SLIDE = dict(
	element_type = "Rock",
	element_type_data = pokemon_types.Rock(),
	category = "Physical",
	power = 75,
	accuracy = 90,
	pp = 10,
	description = "May cause flinching.")

ROCK_THROW = dict(
	element_type = "Rock",
	element_type_data = pokemon_types.Rock(),
	category = "Physical",
	power = 50,
	accuracy = 90,
	pp = 15,
	description = "")

ROLLING_KICK = dict(
	element_type = "Fighting",
	element_type_data = pokemon_types.Fighting(),
	category = "Physical",
	power = 60,
	accuracy = 85,
	pp = 15,
	description = "May cause flinching.")

SAND_ATTACK = dict(
	element_type = "Ground",
	element_type_data = pokemon_types.Ground(),
	category = "Status",
	power = None, 
	accuracy = 100,
	pp = 15,
	description = "Lowers opponent's ACCURACY.")

SCRATCH = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 40,
	accuracy = 100,
	pp = 35,
	description = "")

SCREECH = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = 85,
	pp = 40,
	description = "Sharply lowers opponent's Defense.")

SEISMIC_TOSS = dict(
	element_type = "Fighting",
	element_type_data = pokemon_types.Fighting(),
	category = "Physical",
	power = None,
	accuracy = 100,
	pp = 20,
	description = "Inflicts damage equal to user's level.")

SELF_DESTRUCT = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 200, 
	accuracy = 100,
	pp = 5,
	description = "User faints.")

SHARPEN = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 30,
	description = "Raises user's Attack.")

SING = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = 55,
	pp = 15,
	description = "Puts opponent to sleep.")

SKULL_BASH = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 130, 
	accuracy = 100,
	pp = 10,
	description = "Raises Defense on first turn, attacks on second.")

SKY_ATTACK = dict(
	element_type = "Flying",
	element_type_data = pokemon_types.Flying(),
	category = "Physical",
	power = 140, 
	accuracy = 90,
	pp = 5,
	description = "Charges on first turn, attacks on second. May cause flinching.")

SLAM = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 80,
	accuracy = 75,
	pp = 20,
	description = "")

SLASH = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 70,
	accuracy = 100,
	pp = 20,
	description = "High critical hit ratio.")

SLEEP_POWDER = dict(
	element_type = "Grass",
	element_type_data = pokemon_types.Grass(),
	category = "Status",
	power = None, 
	accuracy = 75,
	pp = 15,
	description = "Puts opponent to sleep.")

SLUDGE = dict(
 	element_type = "Poison",
	element_type_data = pokemon_types.Poison(),
	category = "Special",
	power = 65,
	accuracy = 100,
	pp = 20,
	description = "May poison opponent.")

SMOG = dict(
 	element_type = "Poison",
	element_type_data = pokemon_types.Poison(),
	category = "Special",
	power = 30,
	accuracy = 70,
	pp = 20,
	description = "May poison opponent.")

SMOKESCREEN = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = 100,
	pp = 20,
	description = "Lowers opponent's ACCURACY.")

SOFT_BOILED = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 10,
	description = "User recovers half its max HP.")

SOLAR_BEAM = dict(
	element_type = "Grass",
	element_type_data = pokemon_types.Grass(),
	category = "Special",
	power = 120, 
	accuracy = 100,
	pp = 10,
	description = "Charges on first turn, attacks on second.")

SONIC_BOOM = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Special",
	power = None,
	accuracy = 90,
	pp = 20,
	description = "Always inflicts 20 HP.")

SPIKE_CANNON = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 20,
	accuracy = 100,
	pp = 15,
	description = "Hits 2-5 times in one turn.")

SPLASH = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 40,
	description = "Doesn't do ANYTHING.")

SPORE = dict(
 	element_type = "Grass",
	element_type_data = pokemon_types.Grass(),
	category = "Status",
	power = None,
	accuracy = 100,
	pp = 15,
	description = "Puts opponent to sleep.")

STOMP = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 65,
	accuracy = 100,
	pp = 20,
	description = "May cause flinching.")

STRENGTH = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 80,
	accuracy = 100,
	pp = 15,
	description = "")

STRING_SHOT = dict(
	element_type = "Bug",
	element_type_data = pokemon_types.Bug(),
	category = "Status",
	power = None, 
	accuracy = 95,
	pp = 40,
	description = "Sharply lowers opponent's Speed.")

STRUGGLE = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 50,
	accuracy = 100,
	pp = None,
	description = "Only usable when all PP are gone. Hurts the user.")

STUN_SPORE = dict(
	element_type = "Grass",
	element_type_data = pokemon_types.Grass(),
	category = "Status",
	power = None, 
	accuracy = 75,
	pp = 30,
	description = "Paralyzes opponent.")

SUBMISSION = dict(
 	element_type = "Fighting",
	element_type_data = pokemon_types.Fighting(),
	category = "Physical",
	power = 80,
	accuracy = 80,
	pp = 20,
	description = "User receives recoil damage.")

SUBSTITUTE = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 10,
	description = "Uses HP to creates a decoy that takes hits.")

SUPER_FANG = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = None,
	accuracy = 90,
	pp = 10,
	description = "Always takes off half of the opponent's HP.")

SUPERSONIC = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = 55,
	pp = 20,
	description = "Confuses opponent.")

SURF = dict(
 	element_type = "Water",
	element_type_data = pokemon_types.Water(),
	category = "Special",
	power = 90,
	accuracy = 100,
	pp = 15,
	description = "Hits all adjacent Pokemon.")

SWIFT = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Special",
	power = 60,
	accuracy = 100,
	pp = 20,
	description = "Ignores ACCURACY and Evasiveness.")

SWORDS_DANCE = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 20,
	description = "Sharply raises user's Attack.")

TACKLE = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 40,
	accuracy = 100,
	pp = 35,
	description = "")

TAIL_WHIP = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None, 
	accuracy = 100,
	pp = 30,
	description = "Lowers opponent's Defense.")

TAKE_DOWN = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 90,
	accuracy = 85,
	pp = 20,
	description = "User receives recoil damage.")

TELEPORT = dict(
 	element_type = "Psychic",
	element_type_data = pokemon_types.Psychic(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 20,
	description = "Allows user to flee wild battles; also warps player to last PokeCenter.")

THRASH = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 120,
	accuracy = 100,
	pp = 10,
	description = "User attacks for 2-3 turns but then becomes confused.")

THUNDER = dict(
 	element_type = "Electric",
	element_type_data = pokemon_types.Electric(),
	category = "Special",
	power = 110,
	accuracy = 70,
	pp = 10,
	description = "May paralyze opponent.")

THUNDER_PUNCH = dict(
	element_type = "Electric",
	element_type_data = pokemon_types.Electric(),
	category = "Physical",
	power = 75,
	accuracy = 100,
	pp = 15,
	description = "May paralyze opponent.")

THUNDER_SHOCK = dict(
	element_type = "Electric",
	element_type_data = pokemon_types.Electric(),
	category = "Special",
	power = 40, 
	accuracy = 100,
	pp = 30,
	description = "May paralyze opponent.")

THUNDER_WAVE = dict(
	element_type = "Electric",
	element_type_data = pokemon_types.Electric(),
	category = "Status",
	power = None, 
	accuracy = 90,
	pp = 20,
	description = "Paralyzes opponent.")

THUNDERBOLT = dict(
 	element_type = "Electric",
	element_type_data = pokemon_types.Electric(),
	category = "Special",
	power = 90,
	accuracy = 100,
	pp = 15,
	description = "May paralyze opponent.")

TOXIC = dict(
 	element_type = "Poison",
	element_type_data = pokemon_types.Poison(),
	category = "Status",
	power = None,
	accuracy = 90,
	pp = 10,
	description = "Badly poisons opponent.")

TRANSFORM = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 10,
	description = "User takes on the form and attacks of the opponent.")

TRI_ATTACK = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Special",
	power = 80, 
	accuracy = 100,
	pp = 10,
	description = "May paralyze, burn or freeze opponent.")

TWINEEDLE = dict(
 	element_type = "Bug",
	element_type_data = pokemon_types.Bug(),
	category = "Physical",
	power = 25,
	accuracy = 100,
	pp = 20,
	description = "Hits twice in one turn. May poison opponent.")

VICE_GRIP = dict(
	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 55,
	accuracy = 100,
	pp = 30,
	description = "")

VINE_WHIP = dict(
	element_type = "Grass",
	element_type_data = pokemon_types.Grass(),
	category = "Physical",
	power = 45,
	accuracy = 100,
	pp = 25,
	description = "")

WATER_GUN = dict(
	element_type = "Water",
	element_type_data = pokemon_types.Water(),
	category = "Special",
	power = 40, 
	accuracy = 100,
	pp = 25,
	description = "")

WATERFALL = dict(
 	element_type = "Water",
	element_type_data = pokemon_types.Water(),
	category = "Physical",
	power = 80,
	accuracy = 100,
	pp = 15,
	description = "May cause flinching.")

WHIRLWIND = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 20,
	description = "In battles, the opponent switches. In the wild, the Pokemon runs.")

WING_ATTACK = dict(
	element_type = "Flying",
	element_type_data = pokemon_types.Flying(),
	category = "Physical",
	power = 60,
	accuracy = 100,
	pp = 35,
	description = "")

WITHDRAW = dict(
 	element_type = "Water",
	element_type_data = pokemon_types.Water(),
	category = "Status",
	power = None,
	accuracy = None,
	pp = 40,
	description = "Raises user's Defense.")

WRAP = dict(
 	element_type = "Normal",
	element_type_data = pokemon_types.Normal(),
	category = "Physical",
	power = 15,
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
