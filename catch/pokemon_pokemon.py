#!/usr/bin/env python3

# -*- coding: utf-8 -*- 

# from collections import named tuple module.
from collections import namedtuple
# import random
import random
# import system
import sys
# import pokemon_types
from pokemon_types import *
# import pokemon_moves
from pokemon_moves import *

########################
### File information ###
########################

__author__  = "Lindsay Gelle (https://github.com/gellel)"

__version__ = "1.0"

########################
### Module constants ###
########################

BULBASAUR = dict(
	EN_NAME = "BULBASAUR",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GRASS, 
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 1,
	HASH_ID = "#001"
)
IVYSAUR = dict(
	EN_NAME = "IVYSAUR",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GRASS, 
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 2,
	HASH_ID = "#002"
)
VENUSAUR = dict(
	EN_NAME = "VENUSAUR",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GRASS, 
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 3,
	HASH_ID = "#003"
)
CHARMANDER = dict(
	EN_NAME = "CHARMANDER",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		FIRE),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 4,
	HASH_ID = "#004"
)
CHARMELEON = dict(
	EN_NAME = "CHARMELEON",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		FIRE),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 5,
	HASH_ID = "#005"
)
CHARIZARD = dict(
	EN_NAME = "CHARIZARD",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		FIRE, 
		FLYING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 6,
	HASH_ID = "#006"
)
SQUIRTLE = dict(
	EN_NAME = "SQUIRTLE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 7,
	HASH_ID = "#007"
)
WARTORTLE = dict(
	EN_NAME = "WARTORTLE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 8,
	HASH_ID = "#008"
)
BLASTOISE = dict(
	EN_NAME = "BLASTOISE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 9,
	HASH_ID = "#009"
)
CATERPIE = dict(
	EN_NAME = "CATERPIE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		BUG),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 10,
	HASH_ID = "#010"
)
METAPOD = dict(
	EN_NAME = "METAPOD",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		BUG),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 11,
	HASH_ID = "#011"
)
BUTTERFREE = dict(
	EN_NAME = "BUTTERFREE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		BUG, 
		FLYING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 12,
	HASH_ID = "#012"
)
WEEDLE = dict(
	EN_NAME = "WEEDLE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		BUG, 
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 13,
	HASH_ID = "#013"
)
KAKUNA = dict(
	EN_NAME = "KAKUNA",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		BUG, 
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 14,
	HASH_ID = "#014"
)
BEEDRILL = dict(
	EN_NAME = "BEEDRILL",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		BUG, 
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 15,
	HASH_ID = "#015"
)
PIDGEY = dict(
	EN_NAME = "PIDGEY",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL, 
		FLYING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 16,
	HASH_ID = "#016"
)
PIDGEOTTO = dict(
	EN_NAME = "PIDGEOTTO",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL, 
		FLYING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 17,
	HASH_ID = "#017"
)
PIDGEOT = dict(
	EN_NAME = "PIDGEOT",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL, 
		FLYING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 18,
	HASH_ID = "#018"
)
RATTATA = dict(
	EN_NAME = "RATTATA",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 19,
	HASH_ID = "#019"
)
RATICATE = dict(
	EN_NAME = "RATICATE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 20,
	HASH_ID = "#020"
)
SPEAROW = dict(
	EN_NAME = "SPEAROW",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL, 
		FLYING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 21,
	HASH_ID = "#021"
)
FEAROW = dict(
	EN_NAME = "FEAROW",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL, 
		FLYING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 22,
	HASH_ID = "#022"
)
EKANS = dict(
	EN_NAME = "EKANS",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 23,
	HASH_ID = "#023"
)
ARBOK = dict(
	EN_NAME = "ARBOK",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 24,
	HASH_ID = "#024"
)
PIKACHU = dict(
	EN_NAME = "PIKACHU",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		ELECTRIC),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 25,
	HASH_ID = "#025"
)
RAICHU = dict(
	EN_NAME = "RAICHU",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		ELECTRIC),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 26,
	HASH_ID = "#026"
)
SANDSHREW = dict(
	EN_NAME = "SANDSHREW",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GROUND),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 27,
	HASH_ID = "#027"
)
SANDSLASH = dict(
	EN_NAME = "SANDSLASH",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GROUND),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 28,
	HASH_ID = "#028"
)
NIDORAN_MALE = dict(
	EN_NAME = "NIDORAN",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 29,
	HASH_ID = "#029"
)
NIDORINA = dict(
	EN_NAME = "NIDORINA",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 30,
	HASH_ID = "#030"
)
NIDOQUEEN = dict(
	EN_NAME = "NIDOQUEEN",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		POISON, 
		GROUND),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 31,
	HASH_ID = "#031"
)
NIDORAN_FEMALE = dict(
	EN_NAME = "NIDORAN",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 32,
	HASH_ID = "#032"
)
NIDORINO = dict(
	EN_NAME = "NIDORINO",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 33,
	HASH_ID = "#033"
)
NIDOKING = dict(
	EN_NAME = "NIDOKING",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		POISON, 
		GROUND),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 34,
	HASH_ID = "#034"
)
CLEFAIRY = dict(
	EN_NAME = "CLEFAIRY",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		FAIRY),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 35,
	HASH_ID = "#035"
)
CLEFABLE = dict(
	EN_NAME = "CLEFABLE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		FAIRY),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 36,
	HASH_ID = "#036"
)
VULPIX = dict(
	EN_NAME = "VULPIX",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		FIRE),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 37,
	HASH_ID = "#037"
)
NINETALES = dict(
	EN_NAME = "NINETALES",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		FIRE),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 38,
	HASH_ID = "#038"
)
JIGGLYPUFF = dict(
	EN_NAME = "JIGGLYPUFF",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL, 
		FAIRY),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 39,
	HASH_ID = "#039"
)
WIGGLYTUFF = dict(
	EN_NAME = "WIGGLYTUFF",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL, 
		FAIRY),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 40,
	HASH_ID = "#040"
)
ZUBAT = dict(
	EN_NAME = "ZUBAT",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		POISON, 
		FLYING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 41,
	HASH_ID = "#041"
)
GOLBAT = dict(
	EN_NAME = "GOLBAT",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		POISON, 
		FLYING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 42,
	HASH_ID = "#042"
)
ODDISH = dict(
	EN_NAME = "ODDISH",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GRASS, 
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 43,
	HASH_ID = "#043"
)
GLOOM = dict(
	EN_NAME = "GLOOM",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GRASS, 
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 44,
	HASH_ID = "#044"
)
VILEPLUME = dict(
	EN_NAME = "VILEPLUME",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GRASS, 
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 45,
	HASH_ID = "#045"
)
PARAS = dict(
	EN_NAME = "PARAS",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		BUG, 
		GRASS),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 46,
	HASH_ID = "#046"
)
PARASECT = dict(
	EN_NAME = "PARASECT",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		BUG, 
		GRASS),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 47,
	HASH_ID = "#047"
)
VENONAT = dict(
	EN_NAME = "VENONAT",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		BUG, 
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 48,
	HASH_ID = "#048"
)
VENOMOTH = dict(
	EN_NAME = "VENOMOTH",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		BUG, 
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 49,
	HASH_ID = "#049"
)
DIGLETT = dict(
	EN_NAME = "DIGLETT",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GROUND),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 50,
	HASH_ID = "#050"
)
DUGTRIO = dict(
	EN_NAME = "DUGTRIO",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GROUND),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 51,
	HASH_ID = "#051"
)
MEOWTH = dict(
	EN_NAME = "MEOWTH",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 52,
	HASH_ID = "#052"
)
PERSIAN = dict(
	EN_NAME = "PERSIAN",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 53,
	HASH_ID = "#053"
)
PSYDUCK = dict(
	EN_NAME = "PSYDUCK",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 54,
	HASH_ID = "#054"
)
GOLDUCK = dict(
	EN_NAME = "GOLDUCK",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 55,
	HASH_ID = "#055"
)
MANKEY = dict(
	EN_NAME = "MANKEY",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		FIGHTING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 56,
	HASH_ID = "#056"
)
PRIMEAPE = dict(
	EN_NAME = "PRIMEAPE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		FIGHTING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 57,
	HASH_ID = "#057"
)
GROWLITHE = dict(
	EN_NAME = "GROWLITHE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		FIRE),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 58,
	HASH_ID = "#058"
)
ARCANINE = dict(
	EN_NAME = "ARCANINE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		FIRE),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 59,
	HASH_ID = "#059"
)
POLIWAG = dict(
	EN_NAME = "POLIWAG",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 60,
	HASH_ID = "#060"
)
POLIWHIRL = dict(
	EN_NAME = "POLIWHIRL",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 61,
	HASH_ID = "#061"
)
POLIWRATH = dict(
	EN_NAME = "POLIWRATH",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER, 
		FIGHTING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 62,
	HASH_ID = "#062"
)
ABRA = dict(
	EN_NAME = "ABRA",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		PSYCHIC),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 63,
	HASH_ID = "#063"
)
KADABRA = dict(
	EN_NAME = "KADABRA",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		PSYCHIC),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 64,
	HASH_ID = "#064"
)
ALAKAZAM = dict(
	EN_NAME = "ALAKAZAM",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		PSYCHIC),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 65,
	HASH_ID = "#065"
)
MACHOP = dict(
	EN_NAME = "MACHOP",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		FIGHTING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 66,
	HASH_ID = "#066"
)
MACHOKE = dict(
	EN_NAME = "MACHOKE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		FIGHTING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 67,
	HASH_ID = "#067"
)
MACHAMP = dict(
	EN_NAME = "MACHAMP",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		FIGHTING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 68,
	HASH_ID = "#068"
)
BELLSPROUT = dict(
	EN_NAME = "BELLSPROUT",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GRASS, 
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 69,
	HASH_ID = "#069"
)
WEEPINBELL = dict(
	EN_NAME = "WEEPINBELL",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GRASS, 
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 70,
	HASH_ID = "#070"
)
VICTREEBEL = dict(
	EN_NAME = "VICTREEBEL",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GRASS, 
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 71,
	HASH_ID = "#071"
)
TENTACOOL = dict(
	EN_NAME = "TENTACOOL",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER, 
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 72,
	HASH_ID = "#072"
)
TENTACRUEL = dict(
	EN_NAME = "TENTACRUEL",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER, 
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 73,
	HASH_ID = "#073"
)
GEODUDE = dict(
	EN_NAME = "GEODUDE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		ROCK, 
		GROUND),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 74,
	HASH_ID = "#074"
)
GRAVELER = dict(
	EN_NAME = "GRAVELER",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		ROCK, 
		GROUND),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 75,
	HASH_ID = "#075"
)
GOLEM = dict(
	EN_NAME = "GOLEM",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		ROCK, 
		GROUND),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 76,
	HASH_ID = "#076"
)
PONYTA = dict(
	EN_NAME = "PONYTA",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		FIRE),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 77,
	HASH_ID = "#077"
)
RAPIDASH = dict(
	EN_NAME = "RAPIDASH",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		FIRE),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 78,
	HASH_ID = "#078"
)
SLOWPOKE = dict(
	EN_NAME = "SLOWPOKE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER, 
		PSYCHIC),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 79,
	HASH_ID = "#079"
)
SLOWBRO = dict(
	EN_NAME = "SLOWBRO",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER, 
		PSYCHIC),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 80,
	HASH_ID = "#080"
)
MAGNEMITE = dict(
	EN_NAME = "MAGNEMITE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		ELECTRIC, 
		STEEL),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 81,
	HASH_ID = "#081"
)
MAGNETON = dict(
	EN_NAME = "MAGNETON",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		ELECTRIC, 
		STEEL),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 82,
	HASH_ID = "#082"
)
FARFETCHD = dict(
	EN_NAME = "FARFETCHD",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL, 
		FLYING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 83,
	HASH_ID = "#083"
)
DODUO = dict(
	EN_NAME = "DODUO",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL, 
		FLYING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 84,
	HASH_ID = "#084"
)
DODRIO = dict(
	EN_NAME = "DODRIO",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL, 
		FLYING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 85,
	HASH_ID = "#085"
)
SEEL = dict(
	EN_NAME = "SEEL",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 86,
	HASH_ID = "#086"
)
DEWGONG = dict(
	EN_NAME = "DEWGONG",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER, 
		ICE),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 87,
	HASH_ID = "#087"
)
GRIMER = dict(
	EN_NAME = "GRIMER",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 88,
	HASH_ID = "#088"
)
MUK = dict(
	EN_NAME = "MUK",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 89,
	HASH_ID = "#089"
)
SHELLDER = dict(
	EN_NAME = "SHELLDER",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 90,
	HASH_ID = "#090"
)
CLOYSTER = dict(
	EN_NAME = "CLOYSTER",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER, 
		ICE),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 91,
	HASH_ID = "#091"
)
GASTLY = dict(
	EN_NAME = "GASTLY",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GHOST, 
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 92,
	HASH_ID = "#092"
)
HAUNTER = dict(
	EN_NAME = "HAUNTER",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GHOST, 
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 93,
	HASH_ID = "#093"
)
GENGAR = dict(
	EN_NAME = "GENGAR",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GHOST, 
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 94,
	HASH_ID = "#094"
)
ONIX = dict(
	EN_NAME = "ONIX",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		ROCK, 
		GROUND),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 95,
	HASH_ID = "#095"
)
DROWZEE = dict(
	EN_NAME = "DROWZEE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		PSYCHIC),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 96,
	HASH_ID = "#096"
)
HYPNO = dict(
	EN_NAME = "HYPNO",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		PSYCHIC),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 97,
	HASH_ID = "#097"
)
KRABBY = dict(
	EN_NAME = "KRABBY",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 98,
	HASH_ID = "#098"
)
KINGLER = dict(
	EN_NAME = "KINGLER",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 99,
	HASH_ID = "#099"
)
VOLTORB = dict(
	EN_NAME = "VOLTORB",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		ELECTRIC),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 100,
	HASH_ID = "#100"
)
ELECTRODE = dict(
	EN_NAME = "ELECTRODE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		ELECTRIC),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 101,
	HASH_ID = "#101"
)
EXEGGCUTE = dict(
	EN_NAME = "EXEGGCUTE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GRASS, 
		PSYCHIC),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 102,
	HASH_ID = "#102"
)
EXEGGUTOR = dict(
	EN_NAME = "EXEGGUTOR",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GRASS, 
		PSYCHIC),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 103,
	HASH_ID = "#103"
)
CUBONE = dict(
	EN_NAME = "CUBONE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GROUND),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 104,
	HASH_ID = "#104"
)
MAROWAK = dict(
	EN_NAME = "MAROWAK",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GROUND),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 105,
	HASH_ID = "#105"
)
HITMONLEE = dict(
	EN_NAME = "HITMONLEE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		FIGHTING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 106,
	HASH_ID = "#106"
)
HITMONCHAN = dict(
	EN_NAME = "HITMONCHAN",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		FIGHTING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 107,
	HASH_ID = "#107"
)
LICKITUNG = dict(
	EN_NAME = "LICKITUNG",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 108,
	HASH_ID = "#108"
)
KOFFING = dict(
	EN_NAME = "KOFFING",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 109,
	HASH_ID = "#109"
)
WEEZING = dict(
	EN_NAME = "WEEZING",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		POISON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 110,
	HASH_ID = "#110"
)
RHYHORN = dict(
	EN_NAME = "RHYHORN",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GROUND, 
		ROCK),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 111,
	HASH_ID = "#111"
)
RHYDON = dict(
	EN_NAME = "RHYDON",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GROUND, 
		ROCK),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 112,
	HASH_ID = "#112"
)
CHANSEY = dict(
	EN_NAME = "CHANSEY",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 113,
	HASH_ID = "#113"
)
TANGELA = dict(
	EN_NAME = "TANGELA",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		GRASS),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 114,
	HASH_ID = "#114"
)
KANGASKHAN = dict(
	EN_NAME = "KANGASKHAN",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 115,
	HASH_ID = "#115"
)
HORSEA = dict(
	EN_NAME = "HORSEA",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 116,
	HASH_ID = "#116"
)
SEADRA = dict(
	EN_NAME = "SEADRA",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 117,
	HASH_ID = "#117"
)
GOLDEEN = dict(
	EN_NAME = "GOLDEEN",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 118,
	HASH_ID = "#118"
)
SEAKING = dict(
	EN_NAME = "SEAKING",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 119,
	HASH_ID = "#119"
)
STARYU = dict(
	EN_NAME = "STARYU",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 120,
	HASH_ID = "#120"
)
STARMIE = dict(
	EN_NAME = "STARMIE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER, 
		PSYCHIC),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 121,
	HASH_ID = "#121"
)
MR_MIME = dict(
	EN_NAME = "MR",
	JP_NAME = "",	
	SPECIES = "",
	TYPES = (
		PSYCHIC, 
		FAIRY),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 122,
	HASH_ID = "#122"
)
SCYTHER = dict(
	EN_NAME = "SCYTHER",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		BUG, 
		FLYING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 123,
	HASH_ID = "#123"
)
JYNX = dict(
	EN_NAME = "JYNX",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		ICE, 
		PSYCHIC),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 124,
	HASH_ID = "#124"
)
ELECTABUZZ = dict(
	EN_NAME = "ELECTABUZZ",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		ELECTRIC),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 125,
	HASH_ID = "#125"
)
MAGMAR = dict(
	EN_NAME = "MAGMAR",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		FIRE),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 126,
	HASH_ID = "#126"
)
PINSIR = dict(
	EN_NAME = "PINSIR",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		BUG),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 127,
	HASH_ID = "#127"
)
TAUROS = dict(
	EN_NAME = "TAUROS",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 128,
	HASH_ID = "#128"
)
MAGIKARP = dict(
	EN_NAME = "MAGIKARP",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 129,
	HASH_ID = "#129"
)
GYARADOS = dict(
	EN_NAME = "GYARADOS",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER, 
		FLYING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 130,
	HASH_ID = "#130"
)
LAPRAS = dict(
	EN_NAME = "LAPRAS",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER, 
		ICE),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 131,
	HASH_ID = "#131"
)
DITTO = dict(
	EN_NAME = "DITTO",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 132,
	HASH_ID = "#132"
)
EEVEE = dict(
	EN_NAME = "EEVEE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 133,
	HASH_ID = "#133"
)
VAPOREON = dict(
	EN_NAME = "VAPOREON",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 134,
	HASH_ID = "#134"
)
JOLTEON = dict(
	EN_NAME = "JOLTEON",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		ELECTRIC),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 135,
	HASH_ID = "#135"
)
FLAREON = dict(
	EN_NAME = "FLAREON",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		FIRE),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 136,
	HASH_ID = "#136"
)
PORYGON = dict(
	EN_NAME = "PORYGON",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 137,
	HASH_ID = "#137"
)
OMANYTE = dict(
	EN_NAME = "OMANYTE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		ROCK, 
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 138,
	HASH_ID = "#138"
)
OMASTAR = dict(
	EN_NAME = "OMASTAR",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		ROCK, 
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 139,
	HASH_ID = "#139"
)
KABUTO = dict(
	EN_NAME = "KABUTO",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		ROCK, 
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 140,
	HASH_ID = "#140"
)
KABUTOPS = dict(
	EN_NAME = "KABUTOPS",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		ROCK, 
		WATER),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 141,
	HASH_ID = "#141"
)
AERODACTYL = dict(
	EN_NAME = "AERODACTYL",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		ROCK, 
		FLYING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 142,
	HASH_ID = "#142"
)
SNORLAX = dict(
	EN_NAME = "SNORLAX",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		NORMAL),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 143,
	HASH_ID = "#143"
)
ARTICUNO = dict(
	EN_NAME = "ARTICUNO",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		ICE, 
		FLYING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 144,
	HASH_ID = "#144"
)
ZAPDOS = dict(
	EN_NAME = "ZAPDOS",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		ELECTRIC, 
		FLYING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 145,
	HASH_ID = "#145"
)
MOLTRES = dict(
	EN_NAME = "MOLTRES",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		FIRE, 
		FLYING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 146,
	HASH_ID = "#146"
)
DRATINI = dict(
	EN_NAME = "DRATINI",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		DRAGON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 147,
	HASH_ID = "#147"
)
DRAGONAIR = dict(
	EN_NAME = "DRAGONAIR",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		DRAGON),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 148,
	HASH_ID = "#148"
)
DRAGONITE = dict(
	EN_NAME = "DRAGONITE",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		DRAGON, 
		FLYING),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 149,
	HASH_ID = "#149"
)
MEWTWO = dict(
	EN_NAME = "MEWTWO",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		PSYCHIC),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 150,
	HASH_ID = "#150"
)
MEW = dict(
	EN_NAME = "MEW",
	JP_NAME = "",
	SPECIES = "",
	TYPES = (
		PSYCHIC),
	ABILITIES = (
		),
	TRAINING = (
		),
	ID = 151,
	HASH_ID = "#151"
)