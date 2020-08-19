#!/usr/local/bin/python3
import re


def space_remover(string):
	"""
	Simple Function to remove the spaces from file link
	"""
	# find the position of the beginning of the link
	print("Reaches")
	return string.replace(" ", "_")
	


txt = "This is a [[reference]] in a [[text file]]" 
txt = re.sub("\[\[(.*?)\]\]", "[\\1]({}.md)".format(space_remover("\\1")), txt)
print(txt)
