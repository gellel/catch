#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

###########################
### Required ##############
###########################

import sys

import os

import re

import json

import random

import requests

###########################
### Supports ##############
###########################

from slack.message.formatting import formatting

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


def concatenate (*args):
	"""Joins sequence arguments as a single string."""

	# @return: @type: @string.
	return str.join(" ", map(str, args))

def concatenate_number (number, generation):
	"""Sets formatted string for POKEMON POKEDEX number."""

	# @return: @type: @string.
	return concatenate(number, 
		formatting.parentheses(generation))

def concatenate_names (english, japanese):
	"""Sets formatted string for english and japanese POKEMON names."""

	# @return: @type: @string.
	return concatenate(english, 
		formatting.parentheses(japanese))

def concatenate_types (types):
	"""Sets formatting string for element types for POKEMON."""
	
	# @return: @type: @string.
	return concatenate("TYPES", 
		*dict.keys(types))

def concatenate_about (version, description):
	"""Sets formatted string for POKEMON description and game it's from."""

	# @return: @type: @string.
	return concatenate("ABOUT", 
		formatting.parentheses(re.sub("_", " ", version)), description)

def concatenate_height (metric, imperial):

	# @return: @type: @string.
	return concatenate("HEIGHT", concatenate(metric["SUM"], metric["UNITS"]), 
		formatting.parentheses(concatenate(imperial["SUM"], imperial["UNITS"])))

def concatenate_weight (metric, imperial):

	# @return: @type: @string.
	return concatenate("WEIGHT", concatenate(metric["SUM"], metric["UNITS"]), 
		formatting.parentheses(concatenate(imperial["SUM"], imperial["UNITS"])))

def concatenate_found (version, found):

	# @return: @type: @string.
	return concatenate("FOUND", formatting.parentheses(re.sub("_", " ", version)), 
		", ".join([re.sub("_", " ", i) for i in found]))


def concatenate_stats (stats):

	# @return: @type: @string.
	return "\n".join([concatenate(re.sub("_", " ", key), stats[key]["BASE"], 
		stats[key]["MIN"], stats[key]["MAX"]) for key in stats])


	


def get_general_message (pokemon, generation):

	about = { key: value for (key, value) in pokemon["ABOUT"].iteritems() 
		if value is not None }

	key = random.choice(list(about.keys()))


	pokedex_num = concatenate_number(pokemon["POKEDEX"], generation)

	pokemon_name = concatenate_names(pokemon["EN_NAME"], pokemon["JP_NAME"])

	pokemon_types = concatenate_types(pokemon["TYPES"])

	description = concatenate_about(key, about[key])

	height_size = concatenate_height(pokemon["SIZE"]["METRIC"]["HEIGHT"], pokemon["SIZE"]["IMPERIAL"]["HEIGHT"])

	weight_size = concatenate_height(pokemon["SIZE"]["METRIC"]["WEIGHT"], pokemon["SIZE"]["IMPERIAL"]["WEIGHT"])

	found = concatenate_found(key, pokemon["FOUND"][key])

	stats = concatenate_stats(pokemon["STATS"])


	return "\n".join((pokedex_num, pokemon_name, pokemon_types, height_size, weight_size, description, found, stats))


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

	post = main(sys.argv[1:])

	response = requests.post("https://hooks.slack.com/services/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", 
		headers = {"Content-Type": "application/json"},
		data = json.dumps({"channel": "@lindsaygelle", "username": "lul", "text": post, "icon_emoji": ":feelsbadman:"}))

	print(response)


