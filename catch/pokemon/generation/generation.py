#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

###########################
### Required ##############
###########################

import importlib

import os

###########################
### About #################
###########################

__author__ = "Lindsay Gelle (gellel)"

###########################
### Exports ###############
###########################

__all__ = [
	"GENERATIONS",
	"POKEMON"]

###########################
### Constants #############
###########################

GENERATIONS = tuple([i for i in os.listdir(os.path.dirname(os.path.abspath(__file__)))
	if os.path.isfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), i, "pokemon", "pokemon.py"))])


POKEMON = {
	str.upper(GENERATIONS[i]): __import__(
		".".join([GENERATIONS[i], "pokemon", "pokemon"]), "__all__") 
			for i in range(0, len(GENERATIONS)) }

print(POKEMON["KANTO"])