#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

###########################
### Required ##############
###########################

from collections import namedtuple

###########################
### About #################
###########################

__author__ = "Lindsay Gelle (gellel)"

###########################
### Exports ###############
###########################

__all__ = ["Move"]

###########################
### Constants #############
###########################

MOVE_TUPLE_ATTRIBUTES_KEYS = " ".join([
	"ELEMENT_TYPE", 
	"CATEGORY", 
	"POWER", 
	"ACCURACY", 
	"POWER_POINTS", 
	"DESCRIPTION"])

###########################
### Classes ###############
###########################

Move = namedtuple("Move", 
	MOVE_TUPLE_ATTRIBUTES_KEYS)