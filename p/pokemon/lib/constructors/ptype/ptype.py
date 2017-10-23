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

__all__ = ["Ptype"]

###########################
### Constants #############
###########################

PTYPE_TUPLE_ATTRIBUTES_KEYS = " ".join([
	"BUG",
	"DARK",
	"DRAGON",
	"ELECTRIC",
	"FAIRY",
	"FIGHTING",
	"FIRE",
	"FLYING",
	"GHOST",
	"GRASS",
	"GROUND",
	"ICE",
	"NORMAL",
	"POISON",
	"PSYCHIC",
	"ROCK",
	"STEEL",
	"WATER"])

###########################
### Classes ###############
###########################

Ptype = namedtuple("PType", 
	PTYPE_TUPLE_ATTRIBUTES_KEYS)