#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

###########################
### Required ##############
###########################

import sys

###########################
### About #################
###########################

__author__ = "Lindsay Gelle (gellel)"

###########################
### Exports ###############
###########################

__all__ = [
	"search"]

###########################
### Module ################
###########################

def search (args, properties):
	"""Searchs across arguments sequence for nested key in linear dictionary.

	Assumes key names can be cast as uppercase without same name conflict. 
	Does not modify original dictionary supplied to search method.
	"""

	def dive (props, target, sequence, properties):
		"""Recursive method used to search linear dictionary."""

		# get first argument in sequence.
		key = sequence.pop(0)

		# confirm arguments sequence was emptied of arguments.
		if not len(sequence):

			# confirm current argument at index is the desired key in chain.
			if target is key:

				# confirm current dictionary key exists in dictionary keys.
				if key in map(str.upper, dict.keys(props)):

					# @return: @type: @dict.
					return props[key]

		# arguments are not empty. confirm argument key is in current dictionary.
		elif key in map(str.upper, dict.keys(props)):

			# confirm dictionary key value at index is dictionary type.
			if type(props[key]) is dict:
				
				# @return: @type: @dict
				return dive(props[key], target, sequence, properties)

	# filter non string arguments. cast argument keys to uppercase.
	args = map(str.upper, filter(str, args))

	# @return: @type: @mixed
	if len(args):
		return dive(properties, args[-1], args, properties)


def main (args = ("a", "b", "c"), 
		properties = dict(a = dict(B = dict(C = True)))):

	# @return: @type: @mixed
	return search(args, properties)


if __name__ == '__main__':
	
	print(main(sys.argv[1:]))
