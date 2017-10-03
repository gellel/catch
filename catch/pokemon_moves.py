#!/usr/bin/env python3

# -*- coding: utf-8 -*- 

# from collections import named tuple module.
from collections import namedtuple
# import random
import random
# import pokemon types
import pokemon_types

########################
### File information ###
########################

__author__  = "Lindsay Gelle (https://github.com/gellel)"

__version__ = "1.0"

########################
### Module constants ###
########################


Move = namedtuple("Move", " ".join((
	"element_type",
	"category",
	"power",
	"accuracy",
	"pp",
	"description")))

ABSORB = Move(
	element_type = "GRASS", 
	category = "SPECIAL", 
	power = 20, 
	accuracy = 100, 
	pp = 25, 
	description = "User recovers half the HP inflicted on opponent.")

