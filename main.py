#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

###########################
### Required ##############
###########################

import sys

import os

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
	string = str.join(" ", args)
	
	# @return: @type: @string.
	return string

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

def concatenate_about (game = "SAMPLE", description = "Lorem Ipsum"):

	# set japanese name to contain parentheses.
	game = parenthesize(game)

	# concatenate game version and corresponding description.
	about = concatenate(game, description)
	
	# @return: @type: @string.
	return about

def get_general_message (pokemon):

	about = { key: value for (key, value) in pokemon["ABOUT"].iteritems() 
		if value is not None }

	key = random.choice(list(about.keys()))

	return " ".join([concatenate_names(pokemon["EN_NAME"], pokemon["JP_NAME"]), concatenate_about(key, about[key])])


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

							return get_general_message(generation.GENERATIONS[key][args[2]])


if __name__ == '__main__':

	print(main(sys.argv[1:]))