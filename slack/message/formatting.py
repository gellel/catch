#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

###########################
### Required ##############
###########################

import re

###########################
### About #################
###########################

__author__ = "Lindsay Gelle (gellel)"

###########################
### Exports ###############
###########################

__all__ = [
	"bold",
	"block",
	"code",
	"emphasis",
	"emoji",
	"mono",
	"numbers",
	"points",
	"quote",
	"strike"]

###########################
### Module ################
###########################

def address (*args):
	"""Creates hyperlink references for arguments.

	Encases arguments with <address|title> to generate web address.
	Argument are joined by spaces."""

	# @return: @type: @string.
	return str.join(" ", (str.join("", ("<", 
		(str.join("|", i) if type(i) in (list, tuple) else (i["href"], i["text"])), ">")) 
			for i in args))

def bold (*args):
	"""Creates emphasis for arguments.

	Surround arguments in sequence with *asterisks* to create bold text.
	Arguments are joined by spaces.
	"""

	# @return: @type: @string.
	return str.join(" ", (str.join("", 
		("*", str(i), "*")) for i in args))

def block (*args):
	"""Creates blockquote for arguments.

	Separates arguments in sequence using new line to create blockquote formatting.
	Arguments are joined by new line spaces.
	"""

	# @return: @type: @string.
	return str.join("", (">>>", 
		str.join("\n", args)))

def code (*args):
	"""Creates code snippet for arguments.

	Separates arguments in sequence using new line to create code snippet formatting.
	Arguments are joined by new line spaces.
	"""

	# @return: @type: @string.	
	return str.join("", ("```", 
		str.join("\n", args), "```"))

def emphasis (*args):
	"""Creates italics for arguments.

	Surround arguments in sequence with _underlines_ to create italic text.
	Arguments are joined by spaces.
	"""

	# @return: @type: @string.	
	return str.join(" ", (str.join("", 
		("_", str(i), "_")) for i in args))

def emoji (*args):
	"""Create emoji formatting for arguments.
	
	Surrounds arguments in sequence with :colons: to create emoji character.
	Arguments are joined by spaces.
	"""

	# @return: @type: @string.	
	return str.join(" ", (str.join("", 
		(":", str(i), ":")) for i in args))

def mono (*args):
	"""Creates monospace for arguments.

	Surround arguments in sequence with `backticks` to create monospace text.
	Arguments are joined by spaces.
	"""

	# @return: @type: @string.	
	return str.join(" ", (str.join("", 
		("`", str(i), "`")) for i in args))

def numbers (*args):
	"""Creates numbered points for arguments.

	Separates arguments in sequence using numerals to create ordered list.
	Arguments are joined by new line spaces.
	"""

	# @return: @type: @string.	
	return str.join("\n", (str.join("", 
		(str((i + 1)), ".", " ", args[i])) 
			for i in range(0, len(args))))

def points (*args):
	"""Creates bulleted points for arguments.

	Separates arguments in sequence using bullet points to create unordered list.
	Arguments are joined by new line spaces.
	"""

	# @return: @type: @string.	
	return str.join("\n", (str.join("", 
		("•", " ", str(i))) for i in args))

def quote (*args):
	"""Creates quotation formatting for arguments.

	Separates arguments in sequence using quote formatting to list of quoted strings.
	Arguments are joined by new line spaces.
	"""

	# @return: @type: @string.	
	return str.join("\n", (str.join("", 
		(">", str(i),)) for i in args))

def strike (*args):
	"""Creates strike through for arguments.

	Surround arguments in sequence with ~tildes~ to create strike through text.
	Arguments are joined by spaces.
	"""

	# @return: @type: @string.	
	return str.join(" ", (str.join("", 
		("~", str(i), "~")) for i in args))



print(address(("https://site.com", "site"),))
