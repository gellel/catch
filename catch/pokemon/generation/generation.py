#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

###########################
### Required ##############
###########################

import kanto.pokemon.pokemon as kanto

###########################
### About #################
###########################

__author__ = "Lindsay Gelle (gellel)"

###########################
### Constants #############
###########################

GENERATIONS = dict(
	KANTO = kanto.POKEMON)

###########################
### Exports ###############
###########################

__all__ = [
	kanto]