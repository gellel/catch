#!/usr/bin/env python3

# -*- coding: utf-8 -*- 

########################
### File information ###
########################

__author__  = "Lindsay Gelle (https://github.com/gellel)"

__version__ = "1.0"

#############################
### Pokemon element types ###
#############################

BUG = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 0.5, "NOT_VERY_EFFECTIVE"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 2, "SUPER_EFFECTIVE"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 0.5, "NOT_VERY_EFFECTIVE"),
	("POISON", 0.5, "NOT_VERY_EFFECTIVE"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 0.5, "NOT_VERY_EFFECTIVE"),
	("PSYCHIC", 2, "SUPER_EFFECTIVE"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 1, "NORMAL_EFFECT"),
	("GHOST", 0.5, "NOT_VERY_EFFECTIVE"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 0.5, "NOT_VERY_EFFECTIVE"),
	("FAIRY", 0.5, "NOT_VERY_EFFECTIVE"))

DARK = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 1, "NORMAL_EFFECT"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 1, "NORMAL_EFFECT"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 0.5, "NOT_VERY_EFFECTIVE"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 2, "SUPER_EFFECTIVE"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 1, "NORMAL_EFFECT"),
	("GHOST", 2, "SUPER_EFFECTIVE"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 0.5, "NOT_VERY_EFFECTIVE"),
	("STEEL", 1, "NORMAL_EFFECT"),
	("FAIRY", 0.5, "NOT_VERY_EFFECTIVE"))

DRAGON = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 1, "NORMAL_EFFECT"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 1, "NORMAL_EFFECT"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 1, "NORMAL_EFFECT"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 2, "SUPER_EFFECTIVE"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 0.5, "NOT_VERY_EFFECTIVE"),
	("FAIRY", 0, "NO_EFFECT"))

ELECTRIC = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 1, "NORMAL_EFFECT"),
	("WATER", 2, "SUPER_EFFECTIVE"),
	("ELECTRIC", 0.5, "NOT_VERY_EFFECTIVE"),
	("GRASS", 0.5, "NOT_VERY_EFFECTIVE"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 0, "NO_EFFECT"),
	("FLYING", 2, "SUPER_EFFECTIVE"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 1, "NORMAL_EFFECT"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 0.5, "NOT_VERY_EFFECTIVE"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 1, "NORMAL_EFFECT"),
	("FAIRY", 1, "NORMAL_EFFECT"))

FAIRY = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 0.5, "NOT_VERY_EFFECTIVE"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 1, "NORMAL_EFFECT"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 2, "SUPER_EFFECTIVE"),
	("POISON", 0.5, "NOT_VERY_EFFECTIVE"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 1, "NORMAL_EFFECT"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 2, "SUPER_EFFECTIVE"),
	("DARK", 2, "SUPER_EFFECTIVE"),
	("STEEL", 0.5, "NOT_VERY_EFFECTIVE"),
	("FAIRY", 1, "NORMAL_EFFECT"))

FIGHTING = (
	("NORMAL", 2, "SUPER_EFFECTIVE"),
	("FIRE", 1, "NORMAL_EFFECT"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 1, "NORMAL_EFFECT"),
	("ICE", 2, "SUPER_EFFECTIVE"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 0.5, "NOT_VERY_EFFECTIVE"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 0.5, "NOT_VERY_EFFECTIVE"),
	("PSYCHIC", 0.5, "NOT_VERY_EFFECTIVE"),
	("BUG", 0.5, "NOT_VERY_EFFECTIVE"),
	("ROCK", 2, "SUPER_EFFECTIVE"),
	("GHOST", 0, "NO_EFFECT"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 2, "SUPER_EFFECTIVE"),
	("STEEL", 2, "SUPER_EFFECTIVE"),
	("FAIRY", 0.5, "NOT_VERY_EFFECTIVE"))

FIRE = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 0.5, "NOT_VERY_EFFECTIVE"),
	("WATER", 0.5, "NOT_VERY_EFFECTIVE"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 2, "SUPER_EFFECTIVE"),
	("ICE", 2, "SUPER_EFFECTIVE"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 2, "SUPER_EFFECTIVE"),
	("ROCK", 0.5, "NOT_VERY_EFFECTIVE"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 0.5, "NOT_VERY_EFFECTIVE"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 2, "SUPER_EFFECTIVE"),
	("FAIRY", 1, "NORMAL_EFFECT"))

FLYING = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 1, "NORMAL_EFFECT"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 0.5, "NOT_VERY_EFFECTIVE"),
	("GRASS", 2, "SUPER_EFFECTIVE"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 2, "SUPER_EFFECTIVE"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 2, "SUPER_EFFECTIVE"),
	("ROCK", 0.5, "NOT_VERY_EFFECTIVE"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 0.5, "NOT_VERY_EFFECTIVE"),
	("FAIRY", 1, "NORMAL_EFFECT"))

GHOST = (
	("NORMAL", 0, "NO_EFFECT"),
	("FIRE", 1, "NORMAL_EFFECT"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 1, "NORMAL_EFFECT"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 2, "SUPER_EFFECTIVE"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 1, "NORMAL_EFFECT"),
	("GHOST", 2, "SUPER_EFFECTIVE"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 0.5, "NOT_VERY_EFFECTIVE"),
	("STEEL", 1, "NORMAL_EFFECT"),
	("FAIRY", 1, "NORMAL_EFFECT"))

GRASS = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 0.5, "NOT_VERY_EFFECTIVE"),
	("WATER", 2, "SUPER_EFFECTIVE"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 0.5, "NOT_VERY_EFFECTIVE"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 0.5, "NOT_VERY_EFFECTIVE"),
	("GROUND", 2, "SUPER_EFFECTIVE"),
	("FLYING", 0.5, "NOT_VERY_EFFECTIVE"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 0.5, "NOT_VERY_EFFECTIVE"),
	("ROCK", 2, "SUPER_EFFECTIVE"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 0.5, "NOT_VERY_EFFECTIVE"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 0.5, "NOT_VERY_EFFECTIVE"),
	("FAIRY", 1, "NORMAL_EFFECT"))

GROUND = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 2, "SUPER_EFFECTIVE"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 2, "SUPER_EFFECTIVE"),
	("GRASS", 0.5, "NOT_VERY_EFFECTIVE"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 2, "SUPER_EFFECTIVE"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 0, "NO_EFFECT"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 0.5, "NOT_VERY_EFFECTIVE"),
	("ROCK", 2, "SUPER_EFFECTIVE"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 2, "SUPER_EFFECTIVE"),
	("FAIRY", 1, "NORMAL_EFFECT"))

ICE = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 0.5, "NOT_VERY_EFFECTIVE"),
	("WATER", 0.5, "NOT_VERY_EFFECTIVE"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 2, "SUPER_EFFECTIVE"),
	("ICE", 0.5, "NOT_VERY_EFFECTIVE"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 2, "SUPER_EFFECTIVE"),
	("FLYING", 2, "SUPER_EFFECTIVE"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 1, "NORMAL_EFFECT"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 2, "SUPER_EFFECTIVE"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 0.5, "NOT_VERY_EFFECTIVE"),
	("FAIRY", 1, "NORMAL_EFFECT"))

NORMAL = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 1, "NORMAL_EFFECT"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 1, "NORMAL_EFFECT"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 2, "SUPER_EFFECTIVE"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 0.5, "NOT_VERY_EFFECTIVE"),
	("GHOST", 0, "NO_EFFECT"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 0.5, "NOT_VERY_EFFECTIVE"),
	("FAIRY", 1, "NORMAL_EFFECT"))

POISON = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 1, "NORMAL_EFFECT"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 2, "SUPER_EFFECTIVE"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 0.5, "NOT_VERY_EFFECTIVE"),
	("GROUND", 0.5, "NOT_VERY_EFFECTIVE"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 0.5, "NOT_VERY_EFFECTIVE"),
	("GHOST", 0.5, "NOT_VERY_EFFECTIVE"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 0, "NO_EFFECT"),
	("FAIRY", 1, "NORMAL_EFFECT"))

PSYCHIC = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 1, "NORMAL_EFFECT"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 1, "NORMAL_EFFECT"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 2, "SUPER_EFFECTIVE"),
	("POISON", 2, "SUPER_EFFECTIVE"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 0.5, "NOT_VERY_EFFECTIVE"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 1, "NORMAL_EFFECT"),
	("GHOST", 2, "SUPER_EFFECTIVE"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 0, "NO_EFFECT"),
	("STEEL", 0.5, "NOT_VERY_EFFECTIVE"),
	("FAIRY", 1, "NORMAL_EFFECT"))

ROCK = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 2, "SUPER_EFFECTIVE"),
	("WATER", 1, "NORMAL_EFFECT"),
	("ELECTRIC", 1, "NORMAL_EFFECT"),
	("GRASS", 1, "NORMAL_EFFECT"),
	("ICE", 2, "SUPER_EFFECTIVE"),
	("FIGHTING", 0.5, "NOT_VERY_EFFECTIVE"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 0.5, "NOT_VERY_EFFECTIVE"),
	("FLYING", 2, "SUPER_EFFECTIVE"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 2, "SUPER_EFFECTIVE"),
	("ROCK", 1, "NORMAL_EFFECT"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 0.5, "NOT_VERY_EFFECTIVE"),
	("FAIRY", 1, "NORMAL_EFFECT"))

STEEL = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 0.5, "NOT_VERY_EFFECTIVE"),
	("WATER", 0.5, "NOT_VERY_EFFECTIVE"),
	("ELECTRIC", 0.5, "NOT_VERY_EFFECTIVE"),
	("GRASS", 1, "NORMAL_EFFECT"),
	("ICE", 2, "SUPER_EFFECTIVE"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 1, "NORMAL_EFFECT"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 2, "SUPER_EFFECTIVE"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 1, "NORMAL_EFFECT"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 0.5, "NOT_VERY_EFFECTIVE"),
	("FAIRY", 2, "SUPER_EFFECTIVE"))

WATER = (
	("NORMAL", 1, "NORMAL_EFFECT"),
	("FIRE", 2, "SUPER_EFFECTIVE"),
	("WATER", 0.5, "NOT_VERY_EFFECTIVE"),
	("ELECTRIC", 0.5, "NOT_VERY_EFFECTIVE"),
	("GRASS", 0.5, "NOT_VERY_EFFECTIVE"),
	("ICE", 1, "NORMAL_EFFECT"),
	("FIGHTING", 1, "NORMAL_EFFECT"),
	("POISON", 1, "NORMAL_EFFECT"),
	("GROUND", 2, "SUPER_EFFECTIVE"),
	("FLYING", 1, "NORMAL_EFFECT"),
	("PSYCHIC", 1, "NORMAL_EFFECT"),
	("BUG", 1, "NORMAL_EFFECT"),
	("ROCK", 2, "SUPER_EFFECTIVE"),
	("GHOST", 1, "NORMAL_EFFECT"),
	("DRAGON", 0.5, "NOT_VERY_EFFECTIVE"),
	("DARK", 1, "NORMAL_EFFECT"),
	("STEEL", 1, "NORMAL_EFFECT"),
	("FAIRY", 1, "NORMAL_EFFECT"))

########################################
### Pokemon element types dictionary ###
########################################

GROUPS = {
	"BUG": BUG,
	"DARK": DARK,
	"DRAGON": DRAGON,
	"ELECTRIC": ELECTRIC,
	"FAIRY": FAIRY,
	"FIGHTING": FIGHTING,
	"FIRE": FIRE,
	"FLYING": FLYING,
	"GHOST": GHOST,
	"GRASS": GRASS,
	"GROUND": GROUND,
	"ICE": ICE,
	"NORMAL": NORMAL,
	"POISON": POISON,
	"PSYCHIC": PSYCHIC,
	"ROCK": ROCK,
	"STEEL": STEEL,
	"WATER": WATER }

GROUPS_EFFECTS_SUMS = {k:v[1] for (k,v) in GROUPS.iteritems()}

##################################
### Pokemon element type names ###
##################################

NAMES = tuple(dict.keys(GROUPS))


print(GROUPS_EFFECTS_SUMS)

