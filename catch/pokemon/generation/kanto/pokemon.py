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

########################
### File information ###
########################

__author__  = "Lindsay Gelle (https://github.com/gellel)"

__version__ = "1.0"

__all__ = [
	"BULBASAUR",
	"IVYSAUR",
	"VENUSAUR",
	"CHARMANDER",
	"CHARMELEON",
	"CHARIZARD",
	"SQUIRTLE",
	"WARTORTLE",
	"BLASTOISE",
	"CATERPIE",
	"METAPOD",
	"BUTTERFREE",
	"WEEDLE",
	"KAKUNA",
	"BEEDRILL",
	"PIDGEY",
	"PIDGEOTTO",
	"PIDGEOT",
	"RATTATA",
	"RATICATE",
	"SPEAROW",
	"FEAROW",
	"EKANS",
	"ARBOK",
	"PIKACHU",
	"RAICHU",
	"SANDSHREW",
	"SANDSLASH",
	"NIDORAN_MALE",
	"NIDORINA",
	"NIDOQUEEN",
	"NIDORAN_FEMALE",
	"NIDORINO",
	"NIDOKING",
	"CLEFAIRY",
	"CLEFABLE",
	"VULPIX",
	"NINETALES",
	"JIGGLYPUFF",
	"WIGGLYTUFF",
	"ZUBAT",
	"GOLBAT",
	"ODDISH",
	"GLOOM",
	"VILEPLUME",
	"PARAS",
	"PARASECT",
	"VENONAT",
	"VENOMOTH",
	"DIGLETT",
	"DUGTRIO",
	"MEOWTH",
	"PERSIAN",
	"PSYDUCK",
	"GOLDUCK",
	"MANKEY",
	"PRIMEAPE",
	"GROWLITHE",
	"ARCANINE",
	"POLIWAG",
	"POLIWHIRL",
	"POLIWRATH",
	"ABRA",
	"KADABRA",
	"ALAKAZAM",
	"MACHOP",
	"MACHOKE",
	"MACHAMP",
	"BELLSPROUT",
	"WEEPINBELL",
	"VICTREEBEL",
	"TENTACOOL",
	"TENTACRUEL",
	"GEODUDE",
	"GRAVELER",
	"GOLEM",
	"PONYTA",
	"RAPIDASH",
	"SLOWPOKE",
	"SLOWBRO",
	"MAGNEMITE",
	"MAGNETON",
	"FARFETCHD",
	"DODUO",
	"DODRIO",
	"SEEL",
	"DEWGONG",
	"GRIMER",
	"MUK",
	"SHELLDER",
	"CLOYSTER",
	"GASTLY",
	"HAUNTER",
	"GENGAR",
	"ONIX",
	"DROWZEE",
	"HYPNO",
	"KRABBY",
	"KINGLER",
	"VOLTORB",
	"ELECTRODE",
	"EXEGGCUTE",
	"EXEGGUTOR",
	"CUBONE",
	"MAROWAK",
	"HITMONLEE",
	"HITMONCHAN",
	"LICKITUNG",
	"KOFFING",
	"WEEZING",
	"RHYHORN",
	"RHYDON",
	"CHANSEY",
	"TANGELA",
	"KANGASKHAN",
	"HORSEA",
	"SEADRA",
	"GOLDEEN",
	"SEAKING",
	"STARYU",
	"STARMIE",
	"MR_MIME",
	"SCYTHER",
	"JYNX",
	"ELECTABUZZ",
	"MAGMAR",
	"PINSIR",
	"TAUROS",
	"MAGIKARP",
	"GYARADOS",
	"LAPRAS",
	"DITTO",
	"EEVEE",
	"VAPOREON",
	"JOLTEON",
	"FLAREON",
	"PORYGON",
	"OMANYTE",
	"OMASTAR",
	"KABUTO",
	"KABUTOPS",
	"AERODACTYL",
	"SNORLAX",
	"ARTICUNO",
	"ZAPDOS",
	"MOLTRES",
	"DRATINI",
	"DRAGONAIR",
	"DRAGONITE",
	"MEWTWO",
	"MEW"]

########################
### Module constants ###
########################

BULBASAUR = dict(
	POKEDEX = 1,
	EN_NAME = "BULBASAUR",
	JP_NAME = "FUSHIGIDANE",
	SPECIES = "SEED",
	POKEMON_TYPES = (
		("GRASS", 1), 
		("POISON", 2)),
	ABILITIES = (
		("GROWL", 1),
		("GROWTH", 34),
		("LEECH_SEED", 7),
		("POISON_POWDER", 20),
		("RAZOR_LEAF", 27),
		("SLEEP_POWDER", 41),
		("SOLAR_BEAM", 48),
		("TACKLE", 1),
		("VINE_WHIP", 13)),
	TRAINING = dict(
		EV_YIELD = dict(
			SUM = 1,
			STR = "SPECIAL_ATTACK"),
		CATCH_RATE = dict(
			SUM = 45,
			POKEBALL = "POKEBALL",
			FULL_HP_RATE = 5.9),
		BASE_HAPPINESS = dict(
			SUM = 70,
			STR = "NORMAL"),
		BASE_EXP = dict(
			SUM = 64),
		GROWTH_RATE = dict(
			STR = "MEDIUM_SLOW")),
	BREEDING = dict(
		GROUPS = (
			("GRASS", 1), 
			("MONSTER", 2)),
		GENDER = dict(
			MALE = 87.5,
			FEMALE = 12.5),
		EGG_CYCLES = dict(
			SUM = 20,
			STEPS = 5120)),
	STATS = dict(
		HP = dict(
			BASE = 45,
			MIN = 200,
			MAX = 294),
		ATTACK = dict(
			BASE = 49,
			MIN = 92,
			MAX = 216),
		DEFENSE = dict(
			BASE = 49,
			MIN = 92,
			MAX = 216),
		SP_ATTACK = dict(
			BASE = 65,
			MIN = 121,
			MAX = 251),
		SP_DEFENSE = dict(
			BASE = 65,
			MIN = 121,
			MAX = 251),
		SPEED = dict(
			BASE = 45,
			MIN = 85,
			MAX = 207)),
	EVOLUTION = (
		("IVYSAUR", 2, "#002"),
		("VENUSAUR", 3, "#003")))


"""Dictionary containing the Pokemon names and their corresponding properties.

Contains properties for Pokemon that appeared in the Kanto region.
"""

POKEMON_KANTO_GROUP = {
	"BULBASAUR": BULBASAUR
}

"""Tuple containing strings of Kanto region Pokemon names.

Names are generated from initialised names. Requires Pokemon being defined in Kanto Groups dictionary.
"""

POKEMON_NAMES = tuple(dict.keys(POKEMON_KANTO_GROUP))

"""String containing the required keys for Pokemon base archetypes named tuple."""

POKEMON_KEYS_STRS = " ".join([
	"ABILITIES",
	"BREEDING",
	"EN_NAME",
	"EVOLUTION",
	"JP_NAME",
	"POKEDEX",
	"POKEMON_TYPES",
	"SPECIES",
	"STATS",
	"TRAINING"])

######################
### Module classes ###
######################

class Generate (namedtuple("Props", POKEMON_KEYS_STRS)):
	"""Generates base properties for defined Pokemon."""

	def __new__ (self, pokemon):

		"""Inherit constants for class from named tuple Props."""

		"""
		>>> import pokemon_moves
		>>> pokemon.Generate("BULBASAUR")
		Generate(
			)
		"""

		# Named arguments #

		# @parameter: <pokemon>, @type: <str>, @required: <true>
		# @description: Pokemon base to generate.

		# set pokemon type argument as string and uppercase for comparisons and collections.
		pokemon = str.upper(str(pokemon))

		# set substring substitution on whitespaces.
		pokemon = re.sub(r'\s', '_', pokemon)

		# confirm pokemon move is defined move otherwise select move at random.
		pokemon = pokemon if pokemon in POKEMON_NAMES else random.choice(POKEMON_NAMES)

		# return: @type: @class.__main__.Generate
		return super(Generate, self).__new__(self, **POKEMON_KANTO_GROUP[pokemon])


######################
### Module exports ###
######################

"""Generate constants from defined properties. Overwrites previous properties.

Composed to consume existing declerations.
"""

for i in range(0, len(POKEMON_NAMES)):
	"""Set module properties. Sets package variable using defined names in Pokemon names set."""
	setattr(sys.modules[__name__], POKEMON_NAMES[i], Generate(POKEMON_NAMES[i]))