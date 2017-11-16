#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

###########################
### Required ##############
###########################

import math

import sys

###########################
### About #################
###########################

__author__ = "Lindsay Gelle (gellel)"

###########################
### Exports ###############
###########################

__all__ = []

###########################
### Module ################
###########################

"""Pokémon stats are, in short, governed by a formula. 

For Attack, Defense, Special Attack, Special Defense and Speed, the formula is this:
"""

def hp (B, I, E, L):

	return math.floor((2 * B + I + E) * L / 100 + L + 10)

def base (B, I, E, L, N):

	return math.floor(math.floor((2 * B + I + E) * L / 100 + 5) * N)