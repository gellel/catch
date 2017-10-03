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

"""Tuple containing strings of keys for Pokemon moves generator.

Key names are base from Pokemon DB.
"""

KEYS = (
	"ELEMENT_TYPE", 
	"CATEGORY", 
	"POWER", 
	"ACCURACY", 
	"PP", 
	"DESCRIPTION")

"""String comprised of the different Pokemon generator key substrings."""

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

Aurora_Beam = dict(
	element_type = "Ice",
	category = "Special",
	power = 65, 
	accuracy = 100,
	pp = 20,
	description = "May lower opponent's Attack.")

Barrage = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 15,
	accuracy = 85,
	pp = 20,
	description = "Hits 2-5 times in one turn.")

Barrier = dict(
 	element_type = "Psychic",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 20,
	description = "Sharply raises user's Defense.")

Bide = dict(
 	element_type = "Normal",
	category = "Physical",
	power = None,
	accuracy = None,
	pp = 10,
	description = "User takes damage for two turns then strikes back double.")

Bind = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 15,
	accuracy = 85,
	pp = 20,
	description = "Traps opponent, damaging them for 4-5 turns.")

Bite = dict(
 	element_type = "Dark",
	category = "Physical",
	power = 60,
	accuracy = 100,
	pp = 25,
	description = "May cause flinching.")

Blizzard = dict(
 	element_type = "Ice",
	category = "Special",
	power = 110,
	accuracy = 70,
	pp = 5,
	description = "May freeze opponent.")

Body_Slam = dict(
	element_type = "Normal",
	category = "Physical",
	power = 85,
	accuracy = 100,
	pp = 15,
	description = "May paralyze opponent.")

Bone_Club = dict(
	element_type = "Ground",
	category = "Physical",
	power = 65,
	accuracy = 85,
	pp = 20,
	description = "May cause flinching.")

Bonemerang = dict(
 	element_type = "Ground",
	category = "Physical",
	power = 50,
	accuracy = 90,
	pp = 10,
	description = "Hits twice in one turn.")

Bubble = dict(
 	element_type = "Water",
	category = "Special",
	power = 40,
	accuracy = 100,
	pp = 30,
	description = "May lower opponent's Speed.")

Bubble_Beam = dict(
	element_type = "Water",
	category = "Special",
	power = 65, 
	accuracy = 100,
	pp = 20,
	description = "May lower opponent's Speed.")

Clamp = dict(
 	element_type = "Water",
	category = "Physical",
	power = 35,
	accuracy = 85,
	pp = 10,
	description = "Traps opponent, damaging them for 4-5 turns.")

Comet_Punch = dict(
	element_type = "Normal",
	category = "Physical",
	power = 18,
	accuracy = 85,
	pp = 15,
	description = "Hits 2-5 times in one turn.")

Confuse_Ray = dict(
	element_type = "Ghost",
	category = "Status",
	power = None, 
	accuracy = 100,
	pp = 10,
	description = "Confuses opponent.")

Confusion = dict(
 	element_type = "Psychic",
	category = "Special",
	power = 50,
	accuracy = 100,
	pp = 25,
	description = "May confuse opponent.")

Constrict = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 10,
	accuracy = 100,
	pp = 35,
	description = "May lower opponent's Speed by one stage.")

Conversion = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 30,
	description = "Changes user's type to that of its first move.")

Counter = dict(
 	element_type = "Fighting",
	category = "Physical",
	power = None,
	accuracy = 100,
	pp = 20,
	description = "When hit by a Physical Attack, user strikes back with 2x power.")

Crabhammer = dict(
 	element_type = "Water",
	category = "Physical",
	power = 100,
	accuracy = 90,
	pp = 10,
	description = "High critical hit ratio.")

Cut = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 50,
	accuracy = 95,
	pp = 30,
	description = "")

Defense_Curl = dict(
	element_type = "Normal",
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 40,
	description = "Raises user's Defense.")

Dig = dict(
 	element_type = "Ground",
	category = "Physical",
	power = 80,
	accuracy = 100,
	pp = 10,
	description = "Digs underground on first turn, attacks on second. Can also escape from caves.")

Disable = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = 100,
	pp = 20,
	description = "Opponent can't use its last attack for a few turns.")

Dizzy_Punch = dict(
	element_type = "Normal",
	category = "Physical",
	power = 70,
	accuracy = 100,
	pp = 10,
	description = "May confuse opponent.")

Double_Kick = dict(
	element_type = "Fighting",
	category = "Physical",
	power = 30,
	accuracy = 100,
	pp = 30,
	description = "Hits twice in one turn.")

Double_Slap = dict(
	element_type = "Normal",
	category = "Physical",
	power = 15,
	accuracy = 85,
	pp = 10,
	description = "Hits 2-5 times in one turn.")

Double_Team = dict(
	element_type = "Normal",
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 15,
	description = "Raises user's Evasiveness.")

Double_Edge = dict(
	element_type = "Normal",
	category = "Physical",
	power = 120, 
	accuracy = 100,
	pp = 15,
	description = "User receives recoil damage.")

Dragon_Rage = dict(
	element_type = "Dragon",
	category = "Special",
	power = None,
	accuracy = 100,
	pp = 10,
	description = "Always inflicts 40 HP.")

Dream_Eater = dict(
	element_type = "Psychic",
	category = "Special",
	power = 10,0 
	accuracy = 100,
	pp = 15,
	description = "User recovers half the HP inflicted on a sleeping opponent.")

Drill_Peck = dict(
	element_type = "Flying",
	category = "Physical",
	power = 80,
	accuracy = 100,
	pp = 20,
	description = "")

Earthquake = dict(
 	element_type = "Ground",
	category = "Physical",
	power = 100,
	accuracy = 100,
	pp = 10,
	description = "Power is doubled if opponent is underground from using Dig.")

Egg_Bomb = dict(
	element_type = "Normal",
	category = "Physical",
	power = 100, 
	accuracy = 75,
	pp = 10,
	description = "")

Ember = dict(
 	element_type = "Fire",
	category = "Special",
	power = 40,
	accuracy = 100,
	pp = 25,
	description = "May burn opponent.")

Explosion = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 250,
	accuracy = 100,
	pp = 5,
	description = "User faints.")

Fire_Blast = dict(
	element_type = "Fire",
	category = "Special",
	power = 11,0 
	accuracy = 85,
	pp = 5,
	description = "May burn opponent.")

Fire_Punch = dict(
	element_type = "Fire",
	category = "Physical",
	power = 75,
	accuracy = 100,
	pp = 15,
	description = "May burn opponent.")

Fire_Spin = dict(
	element_type = "Fire",
	category = "Special",
	power = 35, 
	accuracy = 85,
	pp = 15,
	description = "Traps opponent, damaging them for 4-5 turns.")

Fissure = dict(
 	element_type = "Ground",
	category = "Physical",
	power = None,
	accuracy = None,
	pp = 5,
	description = "One-Hit-KO, if it hits.")

Flamethrower = dict(
 	element_type = "Fire",
	category = "Special",
	power = 90,
	accuracy = 100,
	pp = 15,
	description = "May burn opponent.")

Flash = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = 100,
	pp = 20,
	description = "Lowers opponent's Accuracy.")

Fly = dict(
 	element_type = "Flying",
	category = "Physical",
	power = 90,
	accuracy = 95,
	pp = 15,
	description = "Flies up on first turn, attacks on second turn.")

Focus_Energy = dict(
	element_type = "Normal",
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 30,
	description = "Increases critical hit ratio.")

Fury_Attack = dict(
	element_type = "Normal",
	category = "Physical",
	power = 15,
	accuracy = 85,
	pp = 20,
	description = "Hits 2-5 times in one turn.")

Fury_Swipes = dict(
	element_type = "Normal",
	category = "Physical",
	power = 18,
	accuracy = 80,
	pp = 15,
	description = "Hits 2-5 times in one turn.")

Glare = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = 100,
	pp = 30,
	description = "Paralyzes opponent.")

Growl = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = 100,
	pp = 40,
	description = "Lowers opponent's Attack.")

Growth = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 40,
	description = "Raises user's Attack and Special Attack.")

Guillotine = dict(
 	element_type = "Normal",
	category = "Physical",
	power = None,
	accuracy = None,
	pp = 5,
	description = "One-Hit-KO, if it hits.")

Gust = dict(
 	element_type = "Flying",
	category = "Special",
	power = 40,
	accuracy = 100,
	pp = 35,
	description = "Hits Pokémon using Fly/Bounce with double power.")

Harden = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 30,
	description = "Raises user's Defense.")

Haze = dict(
 	element_type = "Ice",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 30,
	description = "Resets all stat changes.")

Headbutt = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 70,
	accuracy = 100,
	pp = 15,
	description = "May cause flinching.")

High_Jump = dict( Kick
	element_type = "Fighting",
	category = "Physical",
	power = 130, 
	accuracy = 90,
	pp = 10,
	description = "If it misses, the user loses half their HP.")

Horn_Attack = dict(
	element_type = "Normal",
	category = "Physical",
	power = 65,
	accuracy = 100,
	pp = 25,
	description = "")

Horn_Drill = dict(
	element_type = "Normal",
	category = "Physical",
	power = None,
	accuracy = None,
	pp = 5,
	description = "One-Hit-KO, if it hits.")

Hydro_Pump = dict(
	element_type = "Water",
	category = "Special",
	power = 11,0 
	accuracy = 80,
	pp = 5,
	description = "")

Hyper_Beam = dict(
	element_type = "Normal",
	category = "Special",
	power = 15,0 
	accuracy = 90,
	pp = 5,
	description = "User must recharge next turn.")

Hyper_Fang = dict(
	element_type = "Normal",
	category = "Physical",
	power = 80,
	accuracy = 90,
	pp = 15,
	description = "May cause flinching.")

Hypnosis = dict(
 	element_type = "Psychic",
	category = "Status",
	power = None,
	accuracy = 60,
	pp = 20,
	description = "Puts opponent to sleep.")

Ice_Beam = dict(
	element_type = "Ice",
	category = "Special",
	power = 90, 
	accuracy = 100,
	pp = 10,
	description = "May freeze opponent.")

Ice_Punch = dict(
	element_type = "Ice",
	category = "Physical",
	power = 75,
	accuracy = 100,
	pp = 15,
	description = "May freeze opponent.")

Jump_Kick = dict(
	element_type = "Fighting",
	category = "Physical",
	power = 100, 
	accuracy = 95,
	pp = 10,
	description = "If it misses, the user loses half their HP.")

Karate_Chop = dict(
	element_type = "Fighting",
	category = "Physical",
	power = 50,
	accuracy = 100,
	pp = 25,
	description = "High critical hit ratio.")

Kinesis = dict(
 	element_type = "Psychic",
	category = "Status",
	power = None,
	accuracy = 80,
	pp = 15,
	description = "Lowers opponent's Accuracy.")

Leech_Life = dict(
	element_type = "Bug",
	category = "Physical",
	power = 80,
	accuracy = 100,
	pp = 10,
	description = "User recovers half the HP inflicted on opponent.")

Leech_Seed = dict(
	element_type = "Grass",
	category = "Status",
	power = None, 
	accuracy = 90,
	pp = 10,
	description = "User steals HP from opponent each turn.")

Leer = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = 100,
	pp = 30,
	description = "Lowers opponent's Defense.")

Lick = dict(
 	element_type=Ghost
	category = "Physical",
	power = 30,
	accuracy = 100,
	pp = 30,
	description = "May paralyze opponent.")

Light_Screen = dict(
	element_type = "Psychic",
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 30,
	description = "Halves damage from Special attacks for 5 turns.")

Lovely_Kiss = dict(
	element_type = "Normal",
	category = "Status",
	power = None, 
	accuracy = 75,
	pp = 10,
	description = "Puts opponent to sleep.")

Low_Kick = dict(
	element_type = "Fighting",
	category = "Physical",
	power = None,
	accuracy = 100,
	pp = 20,
	description = "The heavier the opponent, the stronger the attack.")

Meditate = dict(
 	element_type = "Psychic",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 40,
	description = "Raises user's Attack.")

Mega_Drain = dict(
	element_type = "Grass",
	category = "Special",
	power = 40, 
	accuracy = 100,
	pp = 15,
	description = "User recovers half the HP inflicted on opponent.")

Mega_Kick = dict(
	element_type = "Normal",
	category = "Physical",
	power = 120, 
	accuracy = 75,
	pp = 5,
	description = "")

Mega_Punch = dict(
	element_type = "Normal",
	category = "Physical",
	power = 80,
	accuracy = 85,
	pp = 20,
	description = "")

Metronome = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 10,
	description = "User performs any move in the game at random.")

Mimic = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 10,
	description = "Copies the opponent's last move.")

Minimize = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 10,
	description = "Sharply raises user's Evasiveness.")

Mirror_Move = dict(
	element_type = "Flying",
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 20,
	description = "User performs the opponent's last move.")

Mist = dict(
 	element_type = "Ice",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 30,
	description = "User's stats cannot be changed for a period of time.")

Night_Shade = dict(
	element_type = "Ghost",
	category = "Special",
	power = None,
	accuracy = 100,
	pp = 15,
	description = "Inflicts damage equal to user's level.")

Pay_Day = dict(
	element_type = "Normal",
	category = "Physical",
	power = 40,
	accuracy = 100,
	pp = 20,
	description = "A small amount of money is gained after the battle resolves.")

Peck = dict(
 	element_type = "Flying",
	category = "Physical",
	power = 35,
	accuracy = 100,
	pp = 35,
	description = "")

Petal_Dance = dict(
	element_type = "Grass",
	category = "Special",
	power = 12,0 
	accuracy = 100,
	pp = 10,
	description = "User attacks for 2-3 turns but then becomes confused.")

Pin_Missile = dict(
	element_type = "Bug",
	category = "Physical",
	power = 25,
	accuracy = 95,
	pp = 20,
	description = "Hits 2-5 times in one turn.")

Poison_Gas = dict(
	element_type = "Poison",
	category = "Status",
	power = None, 
	accuracy = 90,
	pp = 40,
	description = "Poisons opponent.")

Poison_Powder = dict(
	element_type = "Poison",
	category = "Status",
	power = None, 
	accuracy = 75,
	pp = 35,
	description = "Poisons opponent.")

Poison_Sting = dict(
	element_type = "Poison",
	category = "Physical",
	power = 15,
	accuracy = 100,
	pp = 35,
	description = "May poison the opponent.")

Pound = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 40,
	accuracy = 100,
	pp = 35,
	description = "")

Psybeam = dict(
 	element_type = "Psychic",
	category = "Special",
	power = 65,
	accuracy = 100,
	pp = 20,
	description = "May confuse opponent.")

Psychic = dict(
 	element_type = "Psychic",
	category = "Special",
	power = 90,
	accuracy = 100,
	pp = 10,
	description = "May lower opponent's Special Defense.")

Psywave = dict(
 	element_type = "Psychic",
	category = "Special",
	power = None,
	accuracy = 80,
	pp = 15,
	description = "Inflicts damage 50-150% of user's level.")

Quick_Attack = dict(
	element_type = "Normal",
	category = "Physical",
	power = 40,
	accuracy = 100,
	pp = 30,
	description = "User attacks first.")

Rage = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 20,
	accuracy = 100,
	pp = 20,
	description = "Raises user's Attack when hit.")

Razor_Leaf = dict(
	element_type = "Grass",
	category = "Physical",
	power = 55,
	accuracy = 95,
	pp = 25,
	description = "High critical hit ratio.")

Razor_Wind = dict(
	element_type = "Normal",
	category = "Special",
	power = 80, 
	accuracy = 100,
	pp = 10,
	description = "Charges on first turn, attacks on second. High critical hit ratio.")

Recover = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 10,
	description = "User recovers half its max HP.")

Reflect = dict(
 	element_type = "Psychic",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 20,
	description = "Halves damage from Physical attacks for 5 turns.")

Rest = dict(
 	element_type = "Psychic",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 10,
	description = "User sleeps for 2 turns, but user is fully healed.")

Roar = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 20,
	description = "In battles, the opponent switches. In the wild, the Pokémon runs.")

Rock_Slide = dict(
	Rock
	category = "Physical",
	power = 75,
	accuracy = 90,
	pp = 10,
	description = "May cause flinching.")

Rock_Throw = dict(
	Rock
	category = "Physical",
	power = 50,
	accuracy = 90,
	pp = 15,
	description = "")

Rolling_Kick = dict(
	element_type = "Fighting",
	category = "Physical",
	power = 60,
	accuracy = 85,
	pp = 15,
	description = "May cause flinching.")

Sand_Attack = dict(
	element_type = "Ground",
	category = "Status",
	power = None, 
	accuracy = 100,
	pp = 15,
	description = "Lowers opponent's Accuracy.")

Scratch = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 40,
	accuracy = 100,
	pp = 35,
	description = "")

Screech = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = 85,
	pp = 40,
	description = "Sharply lowers opponent's Defense.")

Seismic_Toss = dict(
	element_type = "Fighting",
	category = "Physical",
	power = None,
	accuracy = 100,
	pp = 20,
	description = "Inflicts damage equal to user's level.")

Self_Destruct = dict(
	element_type = "Normal",
	category = "Physical",
	power = 200, 
	accuracy = 100,
	pp = 5,
	description = "User faints.")

Sharpen = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 30,
	description = "Raises user's Attack.")

Sing = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = 55,
	pp = 15,
	description = "Puts opponent to sleep.")

Skull_Bash = dict(
	element_type = "Normal",
	category = "Physical",
	power = 130, 
	accuracy = 100,
	pp = 10,
	description = "Raises Defense on first turn, attacks on second.")

Sky_Attack = dict(
	element_type = "Flying",
	category = "Physical",
	power = 140, 
	accuracy = 90,
	pp = 5,
	description = "Charges on first turn, attacks on second. May cause flinching.")

Slam = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 80,
	accuracy = 75,
	pp = 20,
	description = "")

Slash = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 70,
	accuracy = 100,
	pp = 20,
	description = "High critical hit ratio.")

Sleep_Powder = dict(
	element_type = "Grass",
	category = "Status",
	power = None, 
	accuracy = 75,
	pp = 15,
	description = "Puts opponent to sleep.")

Sludge = dict(
 	element_type = "Poison",
	category = "Special",
	power = 65,
	accuracy = 100,
	pp = 20,
	description = "May poison opponent.")

Smog = dict(
 	element_type = "Poison",
	category = "Special",
	power = 30,
	accuracy = 70,
	pp = 20,
	description = "May poison opponent.")

Smokescreen = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = 100,
	pp = 20,
	description = "Lowers opponent's Accuracy.")

Soft_Boiled = dict(
	element_type = "Normal",
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 10,
	description = "User recovers half its max HP.")

Solar_Beam = dict(
	element_type = "Grass",
	category = "Special",
	power = 12,0 
	accuracy = 100,
	pp = 10,
	description = "Charges on first turn, attacks on second.")

Sonic_Boom = dict(
	element_type = "Normal",
	category = "Special",
	power = None,
	accuracy = 90,
	pp = 20,
	description = "Always inflicts 20 HP.")

Spike_Cannon = dict(
	element_type = "Normal",
	category = "Physical",
	power = 20,
	accuracy = 100,
	pp = 15,
	description = "Hits 2-5 times in one turn.")

Splash = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 40,
	description = "Doesn't do ANYTHING.")

Spore = dict(
 	element_type = "Grass",
	category = "Status",
	power = None,
	accuracy = 100,
	pp = 15,
	description = "Puts opponent to sleep.")

Stomp = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 65,
	accuracy = 100,
	pp = 20,
	description = "May cause flinching.")

Strength = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 80,
	accuracy = 100,
	pp = 15,
	description = "")

String_Shot = dict(
	element_type = "Bug",
	category = "Status",
	power = None, 
	accuracy = 95,
	pp = 40,
	description = "Sharply lowers opponent's Speed.")

Struggle = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 50,
	accuracy = 100,
	pp = None,
	description = "Only usable when all PP are gone. Hurts the user.")

Stun_Spore = dict(
	element_type = "Grass",
	category = "Status",
	power = None, 
	accuracy = 75,
	pp = 30,
	description = "Paralyzes opponent.")

Submission = dict(
 	element_type = "Fighting",
	category = "Physical",
	power = 80,
	accuracy = 80,
	pp = 20,
	description = "User receives recoil damage.")

Substitute = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 10,
	description = "Uses HP to creates a decoy that takes hits.")

Super_Fang = dict(
	element_type = "Normal",
	category = "Physical",
	power = None,
	accuracy = 90,
	pp = 10,
	description = "Always takes off half of the opponent's HP.")

Supersonic = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = 55,
	pp = 20,
	description = "Confuses opponent.")

Surf = dict(
 	element_type = "Water",
	category = "Special",
	power = 90,
	accuracy = 100,
	pp = 15,
	description = "Hits all adjacent Pokémon.")

Swift = dict(
 	element_type = "Normal",
	category = "Special",
	power = 60,
	accuracy = ∞,
	pp = 20,
	description = "Ignores Accuracy and Evasiveness.")

Swords_Dance = dict(
	element_type = "Normal",
	category = "Status",
	power = None, 
	accuracy = None,
	pp = 20,
	description = "Sharply raises user's Attack.")

Tackle = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 40,
	accuracy = 100,
	pp = 35,
	description = "")

Tail_Whip = dict(
	element_type = "Normal",
	category = "Status",
	power = None, 
	accuracy = 100,
	pp = 30,
	description = "Lowers opponent's Defense.")

Take_Down = dict(
	element_type = "Normal",
	category = "Physical",
	power = 90,
	accuracy = 85,
	pp = 20,
	description = "User receives recoil damage.")

Teleport = dict(
 	element_type = "Psychic",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 20,
	description = "Allows user to flee wild battles; also warps player to last PokéCenter.")

Thrash = dict(
 	element_type = "Normal",
	category = "Physical",
	power = 120,
	accuracy = 100,
	pp = 10,
	description = "User attacks for 2-3 turns but then becomes confused.")

Thunder = dict(
 	element_type = "Electric",
	category = "Special",
	power = 110,
	accuracy = 70,
	pp = 10,
	description = "May paralyze opponent.")

Thunder_Punch = dict(
	element_type = "Electric",
	category = "Physical",
	power = 75,
	accuracy = 100,
	pp = 15,
	description = "May paralyze opponent.")

Thunder_Shock = dict(
	element_type = "Electric",
	category = "Special",
	power = 40, 
	accuracy = 100,
	pp = 30,
	description = "May paralyze opponent.")

Thunder_Wave = dict(
	element_type = "Electric",
	category = "Status",
	power = None, 
	accuracy = 90,
	pp = 20,
	description = "Paralyzes opponent.")

Thunderbolt = dict(
 	element_type = "Electric",
	category = "Special",
	power = 90,
	accuracy = 100,
	pp = 15,
	description = "May paralyze opponent.")

Toxic = dict(
 	element_type = "Poison",
	category = "Status",
	power = None,
	accuracy = 90,
	pp = 10,
	description = "Badly poisons opponent.")

Transform = dict(
 	element_type = "Normal",
	category = "Status",
	power = None,
	accuracy = None,
	pp = 10,
	description = "User takes on the form and attacks of the opponent.")

Tri_Attack = dict(
	element_type = "Normal",
	category = "Special",
	power = 80, 
	accuracy = 100,
	pp = 10,
	description = "May paralyze, burn or freeze opponent.")

Twineedle = dict(
 	element_type = "Bug",
	category = "Physical",
	power = 25,
	accuracy = 100,
	pp = 20,
	description = "Hits twice in one turn. May poison opponent.")

Vice_Grip = dict(
	element_type = "Normal",
	category = "Physical",
	power = 55,
	accuracy = 100,
	pp = 30,
	description = "")

Vine_Whip = dict(
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
	description = "In battles, the opponent switches. In the wild, the Pokémon runs.")

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
