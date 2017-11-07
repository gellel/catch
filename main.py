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


def get_general_message (pokemon):

	about = { key: value for (key, value) in pkmn["ABOUT"].iteritems() 
		if value is not None }

	key = random.choice(list(about.keys()))

	return " ".join([pokemon["EN_NAME"], "".join(["(", pokemon["JP_NAME"], ")"]), ":", "".join(["(", key, ")"]),  about[key]])


def get_attribute_message (attribute, key, source):
	
	return attribute


def descend_attribute_sequence (current, target, sequence, source):

	key = sequence.pop(0)


	if target == key and not len(sequence):

		if key in current:

			return get_attribute_message(current[key], key, source)

	elif key in current and type(current[key]) is dict:
		
		return descend_attribute_sequence(current[key], target, sequence, source)
	
	return dict()


def get_attribute (pokemon, args):

	return descend_attribute_sequence(pokemon, args[-1], args, pokemon)


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