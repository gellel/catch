#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

###########################
### Required ##############
###########################

import sys

import os

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

def g (source, target, sequence):

	key = sequence.pop(0)

	if target == key and len(sequence) is 0:

		return source[key]

	elif key in source and type(source[key]) is dict:
		
		return g(source[key], target, sequence)
	
	return dict()



def get_primary_attribute (pkmn, args):

	print(g(pkmn, args[-1], args))

	return pkmn


def main (args):

	if len(args):

		args = map(str.upper, map(str, args))

		if args[0] == "GET":
			
			if args[1] and args[1] == "PKMN":
				
				if args[2]:
					
					for key in generation.GENERATIONS:
						
						if args[2] in generation.GENERATIONS[key]:

							if len(args[3:]):

								get_primary_attribute(generation.GENERATIONS[key][args[2]], args[3:])

							return generation.GENERATIONS[key]


if __name__ == '__main__':

	main(sys.argv[1:])