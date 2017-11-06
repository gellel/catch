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

def get_primary_attribute (pkmn, args):

	if type(pkmn) is dict and type(args) in (list, tuple):

		args = map(str.upper, map(str, args))

		if len(args):
			
			if args[0] in pkmn:

				print(pkmn[str.upper(args[0])])

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