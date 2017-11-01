#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

###########################
### About #################
###########################

__author__ = "Lindsay Gelle (gellel)"

###########################
### Exports ###############
###########################

__all__ = [
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
	"WATER"]

###########################
### Constants #############
###########################

BUG = dict(
	BUG = 1,
	DARK = 1,
	DRAGON = 1,
	ELECTRIC = 1,
	FAIRY = 0.5,
	FIGHTING = 0.5,
	FIRE = 0.5,
	FLYING = 0.5,
	GHOST = 0.5,
	GRASS = 2,
	GROUND = 1,
	ICE = 1,
	NORMAL = 1,
	POISON = 0.5,
	PSYCHIC = 2,
	ROCK = 1,
	STEEL = 0.5,
	WATER = 1)

DARK = dict(
	BUG = 1,
	DARK = 0.5,
	DRAGON = 1,
	ELECTRIC = 1,
	FAIRY = 0.5,
	FIGHTING = 0.5,
	FIRE = 1,
	FLYING = 1,
	GHOST = 2,	
	GRASS = 1,
	GROUND = 1,
	ICE = 1,
	NORMAL = 1,
	POISON = 1,
	PSYCHIC = 2,
	ROCK = 1,
	STEEL = 1,
	WATER = 1)

DRAGON = dict(
	BUG = 1,
	DARK = 1,
	DRAGON = 2,
	ELECTRIC = 1,
	FAIRY = 0,
	FIGHTING = 1,
	FIRE = 1,
	FLYING = 1,
	GHOST = 1,
	GRASS = 1,
	GROUND = 1,
	ICE = 1,
	NORMAL = 1,
	POISON = 1,
	PSYCHIC = 1,
	ROCK = 1,
	STEEL = 0.5,
	WATER = 1)

ELECTRIC = dict(
	BUG = 1,
	DARK = 1,
	DRAGON = 0.5,
	ELECTRIC = 0.5,
	FAIRY = 1,
	FIGHTING = 1,
	FIRE = 1,
	FLYING = 2,
	GHOST = 1,
	GRASS = 0.5,
	GROUND = 0,
	ICE = 1,
	NORMAL = 1,
	POISON = 1,
	PSYCHIC = 1,
	ROCK = 1,
	STEEL = 1,
	WATER = 2)

FAIRY = dict(
	BUG = 1,
	DARK = 2,
	DRAGON = 2,
	ELECTRIC = 1,
	FAIRY = 1,
	FIGHTING = 2,
	FIRE = 0.5,
	FLYING = 1,
	GHOST = 1,
	GRASS = 1,
	GROUND = 1,
	ICE = 1,
	NORMAL = 1,
	POISON = 0.5,
	PSYCHIC = 1,
	ROCK = 1,
	STEEL = 0.5,
	WATER = 1)

FIGHTING = dict(
	BUG = 0.5,
	DARK = 2,
	DRAGON = 1,
	ELECTRIC = 1,
	FAIRY = 0.5,
	FIGHTING = 1,
	FIRE = 1,
	FLYING = 0.5,
	GHOST = 0,
	GRASS = 1,
	GROUND = 1,
	ICE = 2,
	NORMAL = 2,
	POISON = 0.5,
	PSYCHIC = 0.5,
	ROCK = 2,
	STEEL = 2,
	WATER = 1)

FIRE = dict(
	BUG = 2,
	DARK = 1,
	DRAGON = 0.5,
	ELECTRIC = 1,
	FAIRY = 1,
	FIGHTING = 1,
	FIRE = 0.5,
	FLYING = 1,
	GHOST = 1,
	GRASS = 2,
	GROUND = 1,
	ICE = 2,
	NORMAL = 1,
	POISON = 1,
	PSYCHIC = 1,
	ROCK = 0.5,
	STEEL = 2,
	WATER = 0.5)

FLYING = dict(
	BUG = 2,
	DARK = 1,
	DRAGON = 1,
	ELECTRIC = 0.5,
	FAIRY = 1,
	FIGHTING = 2,
	FIRE = 1,
	GHOST = 1,
	GRASS = 2,
	GROUND = 1,
	ICE = 1,
	NORMAL = 1,
	POISON = 1,
	FLYING = 1,
	PSYCHIC = 1,
	ROCK = 0.5,
	STEEL = 0.5,
	WATER = 1)

GHOST = dict(
	BUG = 1,
	DARK = 0.5,
	DRAGON = 1,
	ELECTRIC = 1,
	FAIRY = 1,
	FIGHTING = 1,
	FIRE = 1,
	FLYING = 1,
	GHOST = 2,
	GRASS = 1,
	GROUND = 1,
	ICE = 1,
	NORMAL = 0,
	POISON = 1,
	PSYCHIC = 2,
	ROCK = 1,
	STEEL = 1,
	WATER = 1,)

GRASS = dict(
	BUG = 0.5,
	DARK = 1,
	DRAGON = 0.5,
	ELECTRIC = 1,
	FAIRY = 1,
	FIGHTING = 1,
	FIRE = 0.5,
	GHOST = 1,
	GRASS = 0.5,
	GROUND = 2,
	ICE = 1,
	NORMAL = 1,
	POISON = 0.5,
	FLYING = 0.5,
	PSYCHIC = 1,
	ROCK = 2,
	STEEL = 0.5,
	WATER = 2)

GROUND = dict(
	BUG = 0.5,
	DARK = 1,
	DRAGON = 1,
	ELECTRIC = 2,
	FAIRY = 1,
	FIGHTING = 1,
	FIRE = 2,
	FLYING = 0,
	GHOST = 1,
	GRASS = 0.5,
	GROUND = 1,
	ICE = 1,
	NORMAL = 1,
	POISON = 2,
	PSYCHIC = 1,
	ROCK = 2,
	STEEL = 2,
	WATER = 1)

ICE = dict(
	BUG = 1,
	DARK = 1,
	DRAGON = 2,
	ELECTRIC = 1,	
	FAIRY = 1,
	FIGHTING = 1,
	FIRE = 0.5,
	FLYING = 2,
	GHOST = 1,
	GRASS = 2,
	GROUND = 2,
	ICE = 0.5,
	NORMAL = 1,
	POISON = 1,
	PSYCHIC = 1,
	ROCK = 1,
	STEEL = 0.5,
	WATER = 0.5)

NORMAL = dict(
	BUG = 1,
	DARK = 1,
	DRAGON = 1,
	ELECTRIC = 1,
	FAIRY = 1,
	FIGHTING = 2,
	FIRE = 1,
	FLYING = 1,
	GHOST = 0,
	GRASS = 1,
	GROUND = 1,
	ICE = 1,
	NORMAL = 1,
	POISON = 1,
	PSYCHIC = 1,
	ROCK = 0.5,
	STEEL = 0.5,
	WATER = 1)

POISON = dict(
	BUG = 1,
	DARK = 1,
	DRAGON = 1,
	ELECTRIC = 1,
	FAIRY = 1,
	FIGHTING = 1,
	FIRE = 1,
	FLYING = 1,
	GHOST = 0.5,
	GRASS = 2,
	GROUND = 0.5,
	ICE = 1,
	NORMAL = 1,
	POISON = 0.5,
	PSYCHIC = 1,
	ROCK = 0.5,
	STEEL = 0,
	WATER = 1)

PSYCHIC = dict(
	BUG = 1,
	DARK = 0,
	DRAGON = 1,
	ELECTRIC = 1,	
	FAIRY = 1,
	FIGHTING = 2,
	FIRE = 1,
	FLYING = 1,
	GHOST = 2,
	GRASS = 1,
	GROUND = 1,
	ICE = 1,
	NORMAL = 1,
	POISON = 2,
	PSYCHIC = 0.5,
	ROCK = 1,
	STEEL = 0.5,
	WATER = 1)

ROCK = dict(
	BUG = 2,
	DARK = 1,
	DRAGON = 1,
	ELECTRIC = 1,
	FAIRY = 1,
	FIGHTING = 0.5,
	FIRE = 2,
	FLYING = 2,
	GHOST = 1,
	GRASS = 1,
	GROUND = 0.5,
	ICE = 2,
	NORMAL = 1,
	POISON = 1,
	PSYCHIC = 1,
	ROCK = 1,
	STEEL = 0.5,
	WATER = 1)

STEEL = dict(
	BUG = 1,
	DARK = 1,
	DRAGON = 1,
	ELECTRIC = 0.5,
	FAIRY = 2,
	FIGHTING = 1,
	FIRE = 0.5,
	FLYING = 1,
	GHOST = 1,
	GRASS = 1,
	GROUND = 1,
	ICE = 2,
	NORMAL = 1,
	POISON = 1,
	PSYCHIC = 1,
	ROCK = 2,
	STEEL = 0.5,
	WATER = 0.5)

WATER = dict(
	BUG = 1,
	DARK = 1,
	DRAGON = 0.5,
	ELECTRIC = 0.5,
	FAIRY = 1,
	FIGHTING = 1,
	FIRE = 2,
	FLYING = 1,
	GHOST = 1,
	GRASS = 0.5,
	GROUND = 2,
	ICE = 1,
	NORMAL = 1,
	POISON = 1,
	PSYCHIC = 1,
	ROCK = 2,
	STEEL = 1,
	WATER = 0.5)

ELEMENTS = dict(
	BUG = BUG,
	DARK = DARK,
	DRAGON = DRAGON,
	ELECTRIC = ELECTRIC,
	FAIRY = FAIRY,
	FIGHTING = FIGHTING,
	FIRE = FIRE,
	FLYING = FLYING,
	GHOST = GHOST,
	GRASS = GRASS,
	GROUND = GROUND,
	ICE = ICE,
	NORMAL = NORMAL,
	POISON = POISON,
	ROCK = ROCK,
	STEEL = STEEL,
	WATER = WATER)

NAMES = tuple(
	dict.keys(ELEMENTS))