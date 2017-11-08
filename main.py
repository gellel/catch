#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

###########################
### Required ##############
###########################

import sys

import os

import re

import random

###########################
### Supports ##############
###########################

from catch.pokemon.generation import generation

###########################
### About #################
###########################

__author__ = "Lindsay Gelle (gellel)"

###########################
### Constants #############
###########################

###########################
### Module ################
###########################

def parenthesize (arg): 
	"""Sets argument to string and encases in parentheses."""

	# set argument to contain substring formatting.
	string = str.join("", ("(", str(arg), ")"))

	# @return: @type: @string.
	return string

def concatenate (*args):
	"""Joins sequence arguments as a single string.
	
	Concatenates arguments by white-space string.
	"""

	# set argument strings to concatenated string.
	string = str.join(" ", map(str, args))
	
	# @return: @type: @string.
	return string

def concatenate_number (number, generation):

	return concatenate(number, parenthesize(generation))

def concatenate_names (en_name = "EN", jp_name = "JP"):
	"""Sets formatted string for POKEMON name.

	Uses Japanese and English names to compose contents of returned string.
	Created string does not contain formatting.
	"""

	# set japanese name to contain parentheses.
	jp_name = parenthesize(jp_name)

	# concatenate english and japanese names.
	name = concatenate(en_name, jp_name)

	# @return: @type: @string.
	return name

def concatenate_about (version = "SAMPLE", description = "Lorem Ipsum"):

	# set japanese name to contain parentheses.
	version = parenthesize(re.sub(r"_", " ", version))

	# concatenate version version and corresponding description.
	about = concatenate(version, description)
	
	# @return: @type: @string.
	return about

def concatenate_height (metric, imperial):

	metric = concatenate(str(metric["SUM"]), metric["UNITS"])

	imperial = parenthesize(concatenate(imperial["SUM"], imperial["UNITS"]))

	return concatenate("HEIGHT", metric, imperial)

def concatenate_weight (metric, imperial):

	metric = concatenate(str(metric["SUM"]), metric["UNITS"])

	imperial = parenthesize(concatenate(imperial["SUM"], imperial["UNITS"]))

	return concatenate("WEIGHT", metric, imperial)

def get_general_message (pokemon, generation):

	about = { key: value for (key, value) in pokemon["ABOUT"].iteritems() 
		if value is not None }

	key = random.choice(list(about.keys()))

	pokedex_num = concatenate_number(pokemon["POKEDEX"], generation)

	pokemon_name = concatenate_names(pokemon["EN_NAME"], pokemon["JP_NAME"])

	description = concatenate_about(key, about[key])

	height_size = concatenate_height(pokemon["SIZE"]["METRIC"]["HEIGHT"], pokemon["SIZE"]["IMPERIAL"]["HEIGHT"])

	weight_size = concatenate_height(pokemon["SIZE"]["METRIC"]["WEIGHT"], pokemon["SIZE"]["IMPERIAL"]["WEIGHT"])


	return concatenate(pokedex_num, pokemon_name, height_size, weight_size, description)


def get_attribute_message (attribute, key, source):

	return attribute


def process_attributes_sequence (current, target, sequence, source):

	key = sequence.pop(0)

	if target == key and not len(sequence):

		if key in current:

			return get_attribute_message(current[key], key, source)

	elif key in current and type(current[key]) is dict:
		
		return process_attributes_sequence(current[key], target, sequence, source)
	
	return dict()


def get_attribute (pokemon, args):

	return process_attributes_sequence(pokemon, args[-1], args, pokemon)


def main (args):

	if len(args):

		args = map(str.upper, map(str, args))

		if args[0] == "GET":
			
			if args[1] and args[1] == "PKMN":
				
				if args[2]:
					
					for key in generation.GENERATIONS:
						
						if args[2] in generation.GENERATIONS[key]:

							if len(args[3:]):

								return get_attribute(generation.GENERATIONS[key][args[2]], args[3:])

							return get_general_message(generation.GENERATIONS[key][args[2]], key)


if __name__ == '__main__':

	print(main(sys.argv[1:]))