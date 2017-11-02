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

	print(generation.kanto.DITTO)


if __name__ == '__main__':

	main(sys.argv[1:])