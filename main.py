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
### Module ################
###########################

def main (args):

	if len(args):
		if str.upper(args[0]) == "GET":
			if str.upper(args[1]) == "PKMN":
				if str.upper(args[2]) in []:
					print("hi")


if __name__ == '__main__':

	main(sys.argv[1:])