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

__all__ = [
	"MOVE"]

###########################
### Constants #############
###########################

CONSTRUCTOR_KEYS = " ".join([
	"ELEMENT_TYPE", 
	"CATEGORY", 
	"POWER", 
	"ACCURACY", 
	"POWER_POINTS", 
	"DESCRIPTION"])

MOVE = namedtuple("MOVE", 
	CONSTRUCTOR_KEYS)