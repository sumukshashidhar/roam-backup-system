#!/usr/local/bin/python3
import re


# this is to tell it how deep it should look for references
LEVEL = 3 




def space_remover(string):
	"""
	Simple Function to remove the spaces from file link
	"""
	# find the position of the beginning of the link
	return string.replace(" ", "_")
	


def reference_fix(txt):
	"""
	Fixes roam research references
	"""
	global LEVEL
	for i in range(LEVEL):
		txt = re.sub("\[\[(.*?)\]\]","[\\1](\\1.md)",txt)
	
	return txt


# example test case
#txt = "This is a [[reference]] in a [[text file]]" 
