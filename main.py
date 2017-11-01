#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

###########################
### Required ##############
###########################

import sys

import os

###########################
### Paths #################
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

	if (len(args)):

		if str.upper(args[0]) == "GET":

			if str.upper(args[1]) == "GENERATIONS":

				print([str.upper(i) for i in generation.GENERATIONS])



if __name__ == '__main__':

	main(sys.argv[1:])