#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

###########################
### Required ##############
###########################

from collections import namedtuple

###########################
### About #################
###########################

__author__ = "Lindsay Gelle (gellel)"

###########################
### Exports ###############
###########################

__all__ = [
	"ATTRIBUTES"]

###########################
### Constants #############
###########################

KEYS = (
	"POKEDEX",
	"EN_NAME",
	"JP_NAME",
	"SPECIES", 
	"SIZE", 
	"TYPES", 
	"ABILITIES", 
	"MOVESET", 
	"TRAINING",
	"BREEDING", 
	"STATS", 
	"EVOLUTION")

PROPERTIES = " ".join(
	KEYS)

PRIMARY_ATTRIBUTES = namedtuple("PRIMARY_ATTRIBUTES", 
	PROPERTIES)

###########################
### Classes ###############
###########################

class MEASUREMENT (namedtuple("MEASUREMENT", "SUM UNITS")):

	def __new__ (self, **kwargs):

		return super(MEASUREMENT, self).__new__(self, SUM = kwargs["SUM"],
			UNITS = kwargs["UNITS"])

class METRIC (namedtuple("METRIC", "HEIGHT WEIGHT")):

	def __new__ (self, **kwargs):

		return super(METRIC, self).__new__(self, HEIGHT = MEASUREMENT(**kwargs["HEIGHT"]),
			WEIGHT = MEASUREMENT(**kwargs["WEIGHT"]))

class IMPERIAL (namedtuple("IMPERIAL", "HEIGHT WEIGHT")):

	def __new__ (self, **kwargs):

		return super(IMPERIAL, self).__new__(self, HEIGHT = MEASUREMENT(**kwargs["HEIGHT"]),
			WEIGHT = MEASUREMENT(**kwargs["WEIGHT"]))

class SIZE (namedtuple("SIZE", "METRIC IMPERIAL")):

	def __new__ (self, **kwargs):

		return super(SIZE, self).__new__(self, METRIC = METRIC(**kwargs["METRIC"]), 
			IMPERIAL = IMPERIAL(**kwargs["IMPERIAL"]))

class TYPES (namedtuple("TYPES", "PRIMARY SECONDARY")):

	def __new__ (self, **kwargs):

		return super(TYPES, self).__new__(self, PRIMARY = kwargs["PRIMARY"],
			SECONDARY = kwargs["SECONDARY"])

class ABILITIES:

	def __new__ (self, **kwargs):

		return super(ATTRIBUTES, self).__new__(self)

class MOVESET:

	def __new__ (self, **kwargs):

		return super(MOVESET, self).__new__(self)

class EV_YIELD (namedtuple("EV_YIELD", "HP ATTACK DEFENSE SP_ATTACK SP_DEFENSE SPEED")):

	def __new__ (self, **kwargs):

		return super(EV_YIELD, self).__new__(self, HP = kwargs["HP"], ATTACK = kwargs["ATTACK"],
			DEFENSE = kwargs["DEFENSE"], SP_ATTACK = kwargs["SP_ATTACK"], 
				SP_DEFENSE = kwargs["SP_DEFENSE"], SPEED = kwargs["SPEED"])

class CATCH_RATE (namedtuple("CATCH_RATE", "SUM RATE BALL")):

	def __new__ (self, **kwargs):

		return super(CATCH_RATE, self).__new__(self, SUM = kwargs["SUM"], 
			RATE = kwargs["RATE"], BALL = kwargs["BALL"])

class BASE_HAPPINESS (namedtuple("BASE_HAPPINESS", "SUM STR")):

	def __new__ (self, **kwargs):

		return super(BASE_HAPPINESS, self).__new__(self, SUM = kwargs["SUM"],
			STR = kwargs["STR"])

class BASE_EXP (namedtuple("BASE_EXP", "SUM")):

	def __new__ (self, **kwargs):

		return super(BASE_EXP, self).__new__(self, SUM = kwargs["SUM"])

class GROWTH_RATE (namedtuple("GROWTH_RATE", "STR")):

	def __new__ (self, **kwargs):

		return super(GROWTH_RATE, self).__new__(self, STR = kwargs["STR"])

class TRAINING (namedtuple("TRAINING", "EV_YIELD CATCH_RATE BASE_HAPPINESS BASE_EXP GROWTH_RATE")):

	def __new__ (self, **kwargs):

		return super(TRAINING, self).__new__(self, EV_YIELD = EV_YIELD(**kwargs["EV_YIELD"]),
			CATCH_RATE = CATCH_RATE(**kwargs["CATCH_RATE"]), BASE_HAPPINESS = BASE_HAPPINESS(**kwargs["BASE_HAPPINESS"]),
				BASE_EXP = BASE_EXP(**kwargs["BASE_EXP"]), GROWTH_RATE = GROWTH_RATE(**kwargs["GROWTH_RATE"]))

class GROUPS (namedtuple("GROUPS", "PRIMARY SECONDARY")):

	def __new__ (self, **kwargs):

		return super(GROUPS, self).__new__(self, PRIMARY = kwargs["PRIMARY"],
			SECONDARY = kwargs["SECONDARY"])

class GENDERS (namedtuple("GENDERS", "MALE FEMALE GENDERLESS")):

	def __new__ (self, **kwargs):

		return super(GENDERS, self).__new__(self, MALE = kwargs["MALE"],
			FEMALE = kwargs["FEMALE"], GENDERLESS = kwargs["GENDERLESS"])

class EGG_CYCLES (namedtuple("EGG_CYCLES", "SUM STEPS")):

	def __new__ (self, **kwargs):

		return super(EGG_CYCLES, self).__new__(self, SUM = kwargs["SUM"],
			STEPS = kwargs["STEPS"])

class BREEDING (namedtuple("BREEDING", "GROUPS GENDERS EGG_CYCLES")):

	def __new__ (self, **kwargs):

		return super(BREEDING, self).__new__(self, GROUPS = GROUPS(**kwargs["GROUPS"]),
			GENDERS = GENDERS(**kwargs["GENDERS"]), EGG_CYCLES = EGG_CYCLES(**kwargs["EGG_CYCLES"]))

class STATS (namedtuple("STATS", "HP ATTACK DEFENSE SP_ATTACK SP_DEFENSE SPEED")):

	def __new__ (self, **kwargs):

		return super(STATS, self).__new__(self, **{ 
			key: namedtuple(key, "BASE MIN MAX")(**value) for (key, value) in kwargs.iteritems() })

class ATTRIBUTES (PRIMARY_ATTRIBUTES):

	def __new__ (self, **kwargs):

		return super(ATTRIBUTES, self).__new__(self, 
			POKEDEX = kwargs["POKEDEX"], EN_NAME = kwargs["EN_NAME"], JP_NAME = kwargs["JP_NAME"],
				SPECIES = kwargs["SPECIES"], SIZE = SIZE(**kwargs["SIZE"]), TYPES = TYPES(**kwargs["TYPES"]), 
					ABILITIES = kwargs["ABILITIES"], MOVESET = kwargs["MOVESET"], TRAINING = TRAINING(**kwargs["TRAINING"]), 
						BREEDING = BREEDING(**kwargs["BREEDING"]), STATS = STATS(**kwargs["STATS"]), EVOLUTION = kwargs["EVOLUTION"])
