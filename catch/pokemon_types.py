#!/usr/bin/env python3

# -*- coding: utf-8 -*- 

from collections import namedtuple

import random

########################
### File information ###
########################

__author__  = "Lindsay Gelle (https://github.com/gellel)"

__version__ = "1.0"

########################
### Module constants ###
########################

BUG = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 0.5, "NOT_VERY_EFFECTIVE"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 2, "SUPER_EFFECTIVE"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 0.5, "NOT_VERY_EFFECTIVE"),
	("POISON", 0.5, "NOT_VERY_EFFECTIVE"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 0.5, "NOT_VERY_EFFECTIVE"),
	("PSYCHIC", 2, "SUPER_EFFECTIVE"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 1, "NORMAL_EFFECT"),
	("GHOST", 0.5, "NOT_VERY_EFFECTIVE"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 0.5, "NOT_VERY_EFFECTIVE"),
	("FAIRY", 0.5, "NOT_VERY_EFFECTIVE"))

DARK = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 1, "NORMAL_EFFECT"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 1, "NORMAL_EFFECT"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 0.5, "NOT_VERY_EFFECTIVE"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 2, "SUPER_EFFECTIVE"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 1, "NORMAL_EFFECT"),
	("GHOST", 2, "SUPER_EFFECTIVE"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 0.5, "NOT_VERY_EFFECTIVE"),
	("STEEL", 1, "NORMAL_EFFECT"),
	("FAIRY", 0.5, "NOT_VERY_EFFECTIVE"))

DRAGON = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 1, "NORMAL_EFFECT"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 1, "NORMAL_EFFECT"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 1, "NORMAL_EFFECT"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 2, "SUPER_EFFECTIVE"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 0.5, "NOT_VERY_EFFECTIVE"),
	("FAIRY", 0, "NO_EFFECT"))

ELECTRIC = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 1, "NORMAL_EFFECT"),
	("WATER", 2, "SUPER_EFFECTIVE"),
	("ELECTRIC", 0.5, "NOT_VERY_EFFECTIVE"),
	("GRASS", 0.5, "NOT_VERY_EFFECTIVE"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 0, "NO_EFFECT"),
	("FLYING", 2, "SUPER_EFFECTIVE"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 1, "NORMAL_EFFECT"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 0.5, "NOT_VERY_EFFECTIVE"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 1, "NORMAL_EFFECT"),
	("FAIRY", 1, "NORMAL_EFFECT"))

FAIRY = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 0.5, "NOT_VERY_EFFECTIVE"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 1, "NORMAL_EFFECT"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 2, "SUPER_EFFECTIVE"),
	("POISON", 0.5, "NOT_VERY_EFFECTIVE"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 1, "NORMAL_EFFECT"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 2, "SUPER_EFFECTIVE"),
	("DARK", 2, "SUPER_EFFECTIVE"),
	("STEEL", 0.5, "NOT_VERY_EFFECTIVE"),
	("FAIRY", 1, "NORMAL_EFFECT"))

FIGHTING = (
	("NORMAL", 2, "SUPER_EFFECTIVE"),
	("FIRE", 1, "NORMAL_EFFECT"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 1, "NORMAL_EFFECT"),
	("ICE", 2, "SUPER_EFFECTIVE"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 0.5, "NOT_VERY_EFFECTIVE"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 0.5, "NOT_VERY_EFFECTIVE"),
	("PSYCHIC", 0.5, "NOT_VERY_EFFECTIVE"),
	("BUG", 0.5, "NOT_VERY_EFFECTIVE"),
	("ROCK", 2, "SUPER_EFFECTIVE"),
	("GHOST", 0, "NO_EFFECT"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 2, "SUPER_EFFECTIVE"),
	("STEEL", 2, "SUPER_EFFECTIVE"),
	("FAIRY", 0.5, "NOT_VERY_EFFECTIVE"))

FIRE = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 0.5, "NOT_VERY_EFFECTIVE"),
	("WATER", 0.5, "NOT_VERY_EFFECTIVE"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 2, "SUPER_EFFECTIVE"),
	("ICE", 2, "SUPER_EFFECTIVE"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 2, "SUPER_EFFECTIVE"),
	("ROCK", 0.5, "NOT_VERY_EFFECTIVE"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 0.5, "NOT_VERY_EFFECTIVE"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 2, "SUPER_EFFECTIVE"),
	("FAIRY", 1, "NORMAL_EFFECT"))

FLYING = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 1, "NORMAL_EFFECT"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 0.5, "NOT_VERY_EFFECTIVE"),
	("GRASS", 2, "SUPER_EFFECTIVE"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 2, "SUPER_EFFECTIVE"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 2, "SUPER_EFFECTIVE"),
	("ROCK", 0.5, "NOT_VERY_EFFECTIVE"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 0.5, "NOT_VERY_EFFECTIVE"),
	("FAIRY", 1, "NORMAL_EFFECT"))

GHOST = (
	("NORMAL", 0, "NO_EFFECT"),
	("FIRE", 1, "NORMAL_EFFECT"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 1, "NORMAL_EFFECT"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 2, "SUPER_EFFECTIVE"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 1, "NORMAL_EFFECT"),
	("GHOST", 2, "SUPER_EFFECTIVE"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 0.5, "NOT_VERY_EFFECTIVE"),
	("STEEL", 1, "NORMAL_EFFECT"),
	("FAIRY", 1, "NORMAL_EFFECT"))

GRASS = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 0.5, "NOT_VERY_EFFECTIVE"),
	("WATER", 2, "SUPER_EFFECTIVE"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 0.5, "NOT_VERY_EFFECTIVE"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 0.5, "NOT_VERY_EFFECTIVE"),
	("GROUND", 2, "SUPER_EFFECTIVE"),
	("FLYING", 0.5, "NOT_VERY_EFFECTIVE"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 0.5, "NOT_VERY_EFFECTIVE"),
	("ROCK", 2, "SUPER_EFFECTIVE"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 0.5, "NOT_VERY_EFFECTIVE"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 0.5, "NOT_VERY_EFFECTIVE"),
	("FAIRY", 1, "NORMAL_EFFECT"))

GROUND = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 2, "SUPER_EFFECTIVE"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 2, "SUPER_EFFECTIVE"),
	("GRASS", 0.5, "NOT_VERY_EFFECTIVE"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 2, "SUPER_EFFECTIVE"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 0, "NO_EFFECT"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 0.5, "NOT_VERY_EFFECTIVE"),
	("ROCK", 2, "SUPER_EFFECTIVE"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 2, "SUPER_EFFECTIVE"),
	("FAIRY", 1, "NORMAL_EFFECT"))

ICE = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 0.5, "NOT_VERY_EFFECTIVE"),
	("WATER", 0.5, "NOT_VERY_EFFECTIVE"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 2, "SUPER_EFFECTIVE"),
	("ICE", 0.5, "NOT_VERY_EFFECTIVE"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 2, "SUPER_EFFECTIVE"),
	("FLYING", 2, "SUPER_EFFECTIVE"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 1, "NORMAL_EFFECT"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 2, "SUPER_EFFECTIVE"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 0.5, "NOT_VERY_EFFECTIVE"),
	("FAIRY", 1, "NORMAL_EFFECT"))

NORMAL = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 1, "NORMAL_EFFECT"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 1, "NORMAL_EFFECT"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 2, "SUPER_EFFECTIVE"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 0.5, "NOT_VERY_EFFECTIVE"),
	("GHOST", 0, "NO_EFFECT"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 0.5, "NOT_VERY_EFFECTIVE"),
	("FAIRY", 1, "NORMAL_EFFECT"))

POISON = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 1, "NORMAL_EFFECT"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 2, "SUPER_EFFECTIVE"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 0.5, "NOT_VERY_EFFECTIVE"),
	("GROUND", 0.5, "NOT_VERY_EFFECTIVE"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 0.5, "NOT_VERY_EFFECTIVE"),
	("GHOST", 0.5, "NOT_VERY_EFFECTIVE"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 0, "NO_EFFECT"),
	("FAIRY", 1, "NORMAL_EFFECT"))

PSYCHIC = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 1, "NORMAL_EFFECT"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 1, "NORMAL_EFFECT"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 2, "SUPER_EFFECTIVE"),
	("POISON", 2, "SUPER_EFFECTIVE"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 0.5, "NOT_VERY_EFFECTIVE"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 1, "NORMAL_EFFECT"),
	("GHOST", 2, "SUPER_EFFECTIVE"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 0, "NO_EFFECT"),
	("STEEL", 0.5, "NOT_VERY_EFFECTIVE"),
	("FAIRY", 1, "NORMAL_EFFECT"))

ROCK = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 2, "SUPER_EFFECTIVE"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 1, "NORMAL_EFFECT"),
	("ICE", 2, "SUPER_EFFECTIVE"),
	("FIGHTING", 0.5, "NOT_VERY_EFFECTIVE"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 0.5, "NOT_VERY_EFFECTIVE"),
	("FLYING", 2, "SUPER_EFFECTIVE"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 2, "SUPER_EFFECTIVE"),
	("ROCK", 1, "NORMAL_EFFECT"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 0.5, "NOT_VERY_EFFECTIVE"),
	("FAIRY", 1, "NORMAL_EFFECT"))

STEEL = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 0.5, "NOT_VERY_EFFECTIVE"),
	("WATER", 0.5, "NOT_VERY_EFFECTIVE"),
	("ELECTRIC", 0.5, "NOT_VERY_EFFECTIVE"),
	("GRASS", 1, "NORMAL_EFFECT"),
	("ICE", 2, "SUPER_EFFECTIVE"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 2, "SUPER_EFFECTIVE"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 0.5, "NOT_VERY_EFFECTIVE"),
	("FAIRY", 2, "SUPER_EFFECTIVE"))

WATER = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 2, "SUPER_EFFECTIVE"),
	("WATER", 0.5, "NOT_VERY_EFFECTIVE"),
	("ELECTRIC", 0.5, "NOT_VERY_EFFECTIVE"),
	("GRASS", 0.5, "NOT_VERY_EFFECTIVE"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 2, "SUPER_EFFECTIVE"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 2, "SUPER_EFFECTIVE"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 0.5, "NOT_VERY_EFFECTIVE"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 1, "NORMAL_EFFECT"),
	("FAIRY", 1, "NORMAL_EFFECT"))

"""Dictionary containing the primary Pokemon types.

Key contains collection of tuples containing element type resistances and strengths.
Strengths and resistances are presented as the same float or integer.
"""

GROUPS = {
	"BUG": BUG,
	"DARK": DARK,
	"DRAGON": DRAGON,
	"ELECTRIC": ELECTRIC,
	"FAIRY": FAIRY,
	"FIGHTING": FIGHTING,
	"FIRE": FIRE,
	"FLYING": FLYING,
	"GHOST": GHOST,
	"GRASS": GRASS,
	"GROUND": GROUND,
	"ICE": ICE,
	"NORMAL": NORMAL,
	"POISON": POISON,
	"PSYCHIC": PSYCHIC,
	"ROCK": ROCK,
	"STEEL": STEEL,
	"WATER": WATER }

"""Dictionary containing the primary Pokemon types.

Key value is collection of dictionaries containing element type numerical scale.
Strengths and resistances are presented as the same float or integer for the corresponding key.
"""

GROUPS_SUMS = { k: { v[i][0]: v[i][1] 
	for i in range(0, len(v)) } 
	for (k,v) in GROUPS.iteritems() }

"""Dictionary containing the primary Pokemon types.

Key value is collection of dictionaries containing element type numerical scale representation as string.
Strengths and resistances are presented as either "no_effect", "not_very_effective", "normal_effect", "super_effective".
"""

GROUPS_EFFECTS = { k: { v[i][0]: v[i][2] 
	for i in range(0, len(v)) } 
	for (k,v) in GROUPS.iteritems() }


"""Tuple containing strings of primary Pokemon types.

Names are generated from initialised names. Requires Pokemon type is defined in Groups dictionary.
"""

NAMES = tuple(dict.keys(GROUPS))

"""String comprised of the different Pokemon type names."""

NAMES_STRS = " ".join(NAMES)


def generate_type_sum_class (pokemon_type):
	"""Construct psuedo-class property. Contains type numerical scale for property parent.
	
	Pokemon type constructed using Bug as the Pokemon type argument contains sums as defined in Bug constant.
	"""

	"""
	>>> import pokemon_types
	>>> pokemon_types.generate_type_sum_class("BUG")

	BUG(GHOST=0.5, STEEL=0.5, ELECTRIC=1, 
		NORMAL=1, FIRE=0.5, WATER=1, 
		PSYCHIC=2, FLYING=0.5, FIGHTING=0.5, 
		DRAGON=1, DARK=1, POISON=0.5, 
		ICE=1, ROCK=1, FAIRY=0.5, 
		GRASS=2, BUG=1, GROUND=1)
	"""

	# Named arguments #

	# @parameter: <pokemon_type>, @type: <str>, @required: <true>
	# @description: Pokemon element type to generate.


	# set pokemon type argument as string and uppercase for comparisons and collections.
	pokemon_type = str.upper(str(pokemon_type))

	# confirm pokemon type is defined type otherwise select type at random.
	pokemon_type = pokemon_type if pokemon_type in NAMES else random.choice(NAMES)

	# construct pseudo-class constant from named tuple. sets integer sums as corresponding type pair value.
	pokemon_generated_type = namedtuple(pokemon_type, " ".join(NAMES))(**GROUPS_SUMS[pokemon_type])

	# return: @type: @class.__main__.STR_ARG_AS_CLS_NAME
	return pokemon_generated_type


def generate_type_effect_class (pokemon_type):
	"""Construct psuedo-class property. Contains type string effectivness for property parent.
	
	Pokemon type constructed using Bug as the Pokemon type argument contains string as defined in Bug constant.
	"""

	"""
	>>> import pokemon_types
	>>> pokemon_types.generate_type_effect_class("BUG")

	BUG(
		GHOST='NOT_VERY_EFFECTIVE', 
		STEEL='NOT_VERY_EFFECTIVE', 
		ELECTRIC='NORMAL_EFFECT', 
		...)
	"""

	# Named arguments #

	# @parameter: <pokemon_type>, @type: <str>, @required: <true>
	# @description: Pokemon element type to generate.


	# set pokemon type argument as string and uppercase for comparisons and collections.
	pokemon_type = str.upper(str(pokemon_type))

	# confirm pokemon type is defined type otherwise select type at random.
	pokemon_type = pokemon_type if pokemon_type in NAMES else random.choice(NAMES)

	# construct pseudo-class constant from named tuple. sets integer sums as corresponding type pair value.
	pokemon_generated_type = namedtuple(pokemon_type, NAMES_STRS)(**GROUPS_EFFECTS[pokemon_type])

	# return: @type: @class.__main__.STR_ARG_AS_CLS_NAME
	return pokemon_generated_type


def generate_type_stats_class (pokemon_type):
	"""Construct psuedo-class property. Contains type string effectivness for property parent.
	
	Pokemon type constructed using Bug as the Pokemon type argument contains string as defined in Bug constant.
	"""
	
	"""
	>>> import pokemon_types
	>>> pokemon_types.generate_type_stats_class("BUG")

	BUG(
		GHOST=Statistics(
			EFFECT='NORMAL_EFFECT', SUM=1), 
		STEEL=Statistics(
			EFFECT='SUPER_EFFECTIVE', SUM=2), 
		ELECTRIC=Statistics(
			EFFECT='SUPER_EFFECTIVE', SUM=2),
			...)
	"""

	# Named arguments #

	# @parameter: <pokemon_type>, @type: <str>, @required: <true>
	# @description: Pokemon element type to generate.

	# set pokemon type argument as string and uppercase for comparisons and collections.
	pokemon_type = str.upper(str(pokemon_type))

	# confirm pokemon type is defined type otherwise select type at random.
	pokemon_type = pokemon_type if pokemon_type in NAMES else random.choice(NAMES)

	# construct dictionary to contain collection of named tuples.
	pokemon_type_stats = dict()

	# set sub group of properties for specific Pokemon type.
	pokemon_type_subgroups = GROUPS[pokemon_type]

	# iterate for keys of pokemon type groups.
	for i in range(0, len(pokemon_type_subgroups)):

		# append pokemon types dictionary to contain constructed named tuple.
		pokemon_type_stats.update({
				# set dictionary key for item at index as named tuple.
				pokemon_type_subgroups[i][0]: namedtuple("Attribute", "EFFECT SUM")(
					# set properties from current index tuple.
					EFFECT = pokemon_type_subgroups[i][2], SUM = pokemon_type_subgroups[i][1])})

	# return: @type: @class.__main__.STR_ARG_AS_CLS_NAME
	return namedtuple(pokemon_type, NAMES_STRS)(**pokemon_type_stats)





print(generate_type_stats_class("BUG").FIRE)
print("\n")
print(generate_type_stats_class("FIRE").BUG)


