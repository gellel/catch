#!/usr/bin/env python3

# -*- coding: utf-8 -*- 

from collections import namedtuple

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

