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

__all__ = []

########################
### Module constants ###
########################

TRAINING_KEYS_STRS = " ".join([
	"EV_YIELD", 
	"CATCH_RATE", 
	"BASE_HAPPINESS", 
	"BASE_EXP", 
	"GROWTH_RATE"])

BREEDING_KEYS_STRS = " ".join([
	"GROUPS",
	"GENDER",
	"EGG_CYCLES"])

STATS_KEYS_STRS = " ".join([
	"HP",
	"ATTACK",
	"DEFENSE",
	"SP_ATTACK",
	"SP_DEFENSE",
	"SPEED"])

ARCHETYPE_KEY_STRS = " ".join([
	"POKEDEX",
	"EN_NAME",
	"JP_NAME",
	"SPECIES",
	"TYPES",
	"ABILITIES",
	"EVOLUTION",
	"TRAINING",
	"BREEDING",
	"STATS"])

	
def generate_training_class (pokemon_training):

	# @return: @type: @class.__main__.Training
	return namedtuple("Training", TRAINING_KEYS_STRS)(
		EV_YIELD = generate_training_ev_yield_stats_class(*pokemon_training["EV_YIELD"]),
		CATCH_RATE = generate_training_catch_rate_stats_class(*pokemon_training["CATCH_RATE"]),
		BASE_HAPPINESS = generate_training_happiness_stats_class(*pokemon_training["BASE_HAPPINESS"]),
		BASE_EXP = generate_training_exp_stats_class(pokemon_training["BASE_EXP"]),
		GROWTH_RATE = generate_training_growth_rate_stats_class(pokemon_training["GROWTH_RATE"]))

def generate_breeding_class (pokemon_breeding):

	# @return: @type: @class.__main__.Breeding
	return namedtuple("Breeding", BREEDING_KEYS_STRS)(
		GROUPS = generate_breeding_groups_stats_class(pokemon_breeding["GROUPS"]), 
		GENDER = generate_breeding_gender_stats_class(pokemon_breeding["GENDER"]), 
		EGG_CYCLES = generate_breeding_egg_cycles_stats_class(*pokemon_breeding["EGG_CYCLES"]))

def generate_stats_class (pokemon_stats):

	# @return: @type: @class.__main__.Stats
	return namedtuple("Stats", STATS_KEYS_STRS)(**{ 
		key: namedtuple(re.sub(r'\s|_', "", str.title(key)), "BASE MIN MAX")(*value) 
		for key, value in pokemon_stats.iteritems() })

def generate_training_ev_yield_stats_class (pokemon_ev_yield_sum, 
	pokemon_ev_yield_str):
	""""""
	# @return: @type: @class.__main__.EvYield
	return namedtuple("EvYield", " ".join(["SUM", "STR"]))(
		SUM = pokemon_ev_yield_sum, STR = pokemon_ev_yield_str)

def generate_training_catch_rate_stats_class (pokemon_catch_rate_sum, 
	pokemon_catch_rate_hp_rate, pokemon_catch_rate_ball):
	""""""
	# @return: @type: @class.__main__.Catch
	return namedtuple("Catch", " ".join(["SUM", "HP_RATE", "POKEBALL"]))(
		SUM = pokemon_catch_rate_sum, HP_RATE = pokemon_catch_rate_hp_rate, 
			POKEBALL = pokemon_catch_rate_ball)

def generate_training_happiness_stats_class (pokemon_happiness_sum, 
	pokemon_happiness_str):
	""""""
	# @return: @type: @class.__main__.Happiness
	return namedtuple("Happiness", " ".join(["SUM", "STR"]))(
		SUM = pokemon_happiness_sum, STR = pokemon_happiness_str)

def generate_training_exp_stats_class (pokemon_exp_sum):
	""""""
	# @return: @type: @class.__main__.Exp
	return namedtuple("Exp", " ".join(["SUM"]))(
		SUM = pokemon_exp_sum)
	
def generate_training_growth_rate_stats_class (pokemon_growth_rate_str):
	""""""
	# @return: @type: @class.__main__.Growth
	return namedtuple("Growth", " ".join(["STR"]))(
		STR = pokemon_growth_rate_str)
	
def generate_breeding_groups_stats_class (pokemon_groups_sequence):

	groups = { pokemon_groups_sequence[i][0]: namedtuple("Props", " ".join(["SUM"]))(
		SUM = pokemon_groups_sequence[i][1]) for i in range(0, len(pokemon_groups_sequence)) }
	
	# @return: @type: @class.__main__.Groups
	return namedtuple("Groups", " ".join(dict.keys(groups)))(**groups)

def generate_breeding_gender_stats_class (pokemon_gender_sequence):

	groups = { pokemon_gender_sequence[i][0]: namedtuple("Props", " ".join(["SUM"]))(
		SUM = pokemon_gender_sequence[i][1]) for i in range(0, len(pokemon_gender_sequence)) }
	
	# @return: @type: @class.__main__.Gender
	return namedtuple("Gender", " ".join(dict.keys(groups)))(**groups)

def generate_breeding_egg_cycles_stats_class (pokemon_egg_cycles_sum, 
	pokemon_egg_cycles_steps):

	# @return: @type: @class.__main__.Eggs
	return namedtuple("Eggs", " ".join(["SUM", "STEPS"]))(
		SUM = pokemon_egg_cycles_sum, STEPS = pokemon_egg_cycles_steps)

def generate_stats_hp_stats_class (pokemon_hp_stats_base, 
		pokemon_hp_stats_min, pokemon_hp_stats_max):

	# @return: @type: @class.__main__.Hp
	return namedtuple("Hp", " ".join(["BASE", "MIN", "MAX"]))(
		BASE = pokemon_hp_stats_base, MIN = pokemon_hp_stats_min, 
			MAX = pokemon_hp_stats_max)

def generate_stats_attack_stats_class (pokemon_attack_stats_base, 
		pokemon_attack_stats_min, pokemon_attack_stats_max):

	# @return: @type: @class.__main__.Attack
	return namedtuple("Attack", " ".join(["BASE", "MIN", "MAX"]))(
		BASE = pokemon_attack_stats_base, MIN = pokemon_attack_stats_min, 
			MAX = pokemon_attack_stats_max)

def generate_stats_defense_stats_class (pokemon_defense_stats_base, 
		pokemon_defense_stats_min, pokemon_defense_stats_max):
	
	# @return: @type: @class.__main__.Defense
	return namedtuple("Defense", " ".join(["BASE", "MIN", "MAX"]))(
		BASE = pokemon_defense_stats_base, MIN = pokemon_defense_stats_min, 
			MAX = pokemon_defense_stats_max)
	
def generate_stats_sp_attack_stats_class (pokemon_sp_attack_stats_base, 
		pokemon_sp_attack_stats_min, pokemon_sp_attack_stats_max):

	# @return: @type: @class.__main__.SpAttack
	return namedtuple("SpAttack", " ".join(["BASE", "MIN", "MAX"]))(
		BASE = pokemon_sp_attack_stats_base, MIN = pokemon_sp_attack_stats_min, 
			MAX = pokemon_sp_attack_stats_max)

def generate_stats_sp_defense_stats_class (pokemon_sp_defense_stats_base, 
		pokemon_sp_defense_stats_min, pokemon_sp_defense_stats_max):

	# @return: @type: @class.__main__.SpDefense
	return namedtuple("SpDefense", " ".join(["BASE", "MIN", "MAX"]))(
		BASE = pokemon_sp_defense_stats_base, MIN = pokemon_sp_defense_stats_min, 
			MAX = pokemon_sp_defense_stats_max)

def generate_stats_speed_stats_class (pokemon_speed_stats_base, 
		pokemon_speed_stats_min, pokemon_speed_stats_max):

	# @return: @type: @class.__main__.Speed
	return namedtuple("Speed", " ".join(["BASE", "MIN", "MAX"]))(
		BASE = pokemon_speed_stats_base, MIN = pokemon_speed_stats_min, 
			MAX = pokemon_speed_stats_max)

######################
### Module classes ###
######################

class Archetype (namedtuple("Props", ARCHETYPE_KEY_STRS)):

	def __new__ (self, 
			POKEDEX,
			EN_NAME,
			JP_NAME,
			SPECIES,
			TYPES,
			ABILITIES,
			EVOLUTION,
			TRAINING,
			BREEDING,
			STATS):

		return super(Archetype, self).__new__(self, 
			POKEDEX = POKEDEX,
			EN_NAME = EN_NAME,
			JP_NAME = JP_NAME,
			SPECIES = SPECIES,
			TYPES = TYPES,
			ABILITIES = ABILITIES,
			EVOLUTION = EVOLUTION,
			TRAINING = generate_training_class(TRAINING),
			BREEDING = generate_breeding_class(BREEDING),
			STATS = generate_stats_class(STATS))
		



B = Archetype(

		POKEDEX = 1,
		EN_NAME = "BULBASAUR",
		JP_NAME = "FUSHIGIDANE",
		SPECIES = "SEED",
		TYPES = (
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
		EVOLUTION = (
			("IVYSAUR", 2, 16),
			("VENUSAUR", 3, 32)),
		TRAINING = dict(
			EV_YIELD = (1, "SPECIAL_ATTACK"),
			CATCH_RATE = (45, 5.9, "POKEBALL"),
			BASE_HAPPINESS = (70, "NORMAL"),
			BASE_EXP = (64),
			GROWTH_RATE = ("MEDIUM_SLOW")),
		BREEDING = dict(
			GROUPS = (("GRASS", 1), ("MONSTER", 2)),
			GENDER = (("MALE", 87.5), ("FEMALE", 12.5)),
			EGG_CYCLES = (20, 5120)),
		STATS = dict(
			HP = (45, 200, 294),
			ATTACK = (49, 92, 216),
			DEFENSE = (49, 92, 216),
			SP_ATTACK = (65, 121, 251),
			SP_DEFENSE = (65, 121, 251),
			SPEED = (45, 85, 207))
	)


