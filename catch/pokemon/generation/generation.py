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
	"GENERATIONS"]

###########################
### Constants #############
###########################

GENERATIONS = { str.upper(i): getattr(
	importlib.import_module(".".join([i, "pokemon", "pokemon"])), "POKEMON") 
		for i in os.listdir(os.path.dirname(os.path.abspath(__file__)))
			if os.path.isfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), i, "pokemon", "pokemon.py")) }
