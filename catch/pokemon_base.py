#!/usr/bin/env python3

# -*- coding: utf-8 -*- 

# from collections import named tuple module.
from collections import namedtuple
# import random
import random
# import system
import sys

from pokemon_types import generate_types_class

from pokemon_moves import generate_abilities_class

########################
### File information ###
########################

__author__  = "Lindsay Gelle (https://github.com/gellel)"

__version__ = "1.0"

__all__ = []

######################
### Module methods ###
######################


def generate_training_class ():
	pass

def generate_breeding_class ():
	pass

def generate_stats_class ():
	pass

def generate_evolution_class ():
	pass


def generate_training_ev_yield_stats_class (pokemon_ev_yield_sum, pokemon_ev_yield_str):
	""""""
	# @return: @type: @class.__main__.EvYield
	return namedtuple("EvYield", " ".join(["SUM", "STR"]))(
		SUM = pokemon_ev_yield_sum, STR = pokemon_ev_yield_str)

def generate_training_catch_rate_stats_class (pokemon_catch_rate_sum, pokemon_catch_rate_hp_rate, pokemon_catch_rate_ball):
	""""""
	# @return: @type: @class.__main__.Catch
	return namedtuple("Catch", " ".join(["SUM", "HP_RATE", "POKEBALL"]))(
		SUM = pokemon_catch_rate_sum, HP_RATE = pokemon_catch_rate_hp_rate, POKEBALL = pokemon_catch_rate_ball)

def generate_training_happiness_stats_class (pokemon_happiness_sum, pokemon_happiness_str):
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

	groups = { pokemon_groups_sequence[i][0]: namedtuple("Props", " ".join(["SUM"]))(SUM = pokemon_groups_sequence[i][1])
		for i in range(0, len(pokemon_groups_sequence)) }
	
	# @return: @type: @class.__main__.Groups
	return namedtuple("Groups", " ".join(dict.keys(groups)))(**groups)

def generate_breeding_gender_stats_class (pokemon_gender_sequence):

	groups = { pokemon_gender_sequence[i][0]: namedtuple("Props", " ".join(["SUM"]))(SUM = pokemon_gender_sequence[i][1])
		for i in range(0, len(pokemon_gender_sequence)) }
	
	# @return: @type: @class.__main__.Gender
	return namedtuple("Gender", " ".join(dict.keys(groups)))(**groups)

def generate_breeding_egg_cycles_stats_class (pokemon_egg_cycles_sum, pokemon_egg_cycles_steps):

	# @return: @type: @class.__main__.EggCycles
	return namedtuple("EggCycles", " ".join(["SUM", "STEPS"]))(
		SUM = pokemon_egg_cycles_sum, STEPS = pokemon_egg_cycles_steps)

def generate_stats_attack_stats_class (pokemon_attack_stats_base, pokemon_attack_stats_min, pokemon_attack_stats_max):

	return namedtuple("Attack", " ".join(["BASE", "MIN", "MAX"]))(
		BASE = pokemon_attack_stats_base, MIN = pokemon_attack_stats_min, MAX = pokemon_attack_stats_max)

def generate_stats_defense_stats_class (pokemon_defense_stats_base, pokemon_defense_stats_min, pokemon_defense_stats_max):

	return namedtuple("Defense", " ".join(["BASE", "MIN", "MAX"]))(
		BASE = pokemon_defense_stats_base, MIN = pokemon_defense_stats_min, MAX = pokemon_defense_stats_max)
	
def generate_stats_sp_attack_stats_class (pokemon_sp_attack_stats_base, pokemon_sp_attack_stats_min, pokemon_sp_attack_stats_max):

	return namedtuple("SpAttack", " ".join(["BASE", "MIN", "MAX"]))(
		BASE = pokemon_sp_attack_stats_base, MIN = pokemon_sp_attack_stats_min, MAX = pokemon_sp_attack_stats_max)

def generate_stats_sp_defense_stats_class (pokemon_sp_defense_stats_base, pokemon_sp_defense_stats_min, pokemon_sp_defense_stats_max):

	return namedtuple("SpDefense", " ".join(["BASE", "MIN", "MAX"]))(
		BASE = pokemon_sp_defense_stats_base, MIN = pokemon_sp_defense_stats_min, MAX = pokemon_sp_defense_stats_max)
	


	"""

	
	STATS = (
		("HP", 45, 200, 294),
		("ATTACK", 49, 92, 216),
		("DEFENSE", 49, 92, 216),
		("SP_ATTACK", 65, 121, 251),
		("SP_DEFENSE", 65, 121, 251),
		("SPEED", 45, 85, 207)),

	EVOLUTION = (
		("IVYSAUR", 2, "002", 16),
		("VENUSAUR", 3, "003", 32)))
	
	TRAINING
		("EV_YIELD", 1, "SPECIAL_ATTACK"),
		("CATCH_RATE", 45, 5.9, "POKEBALL"),
		("BASE_HAPPINESS", 70, "NORMAL"),
		("BASE_EXP" 64),
		("GROWTH_RATE", "MEDIUM_SLOW")),

	BREEDING = (
		("GROUPS", (("GRASS", 1), ("MONSTER", 2))),
		("GENDER", (("MALE", 87.5), ("FEMALE", 12.5))),
		("EGG_CYCLES", 20, 5120)),
	"""

print(
	generate_gender_stats_class((("MALE", 87.5), ("FEMALE", 12.5)))
)

