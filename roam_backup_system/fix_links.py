#!/usr/local/bin/python3
import re


# this is to tell it how deep it should look for references
LEVEL = 3
reference_map = {}
filename = ''
def reference_fix(txt):
	"""
	Fixes roam research references by using regex expressions. 
	Also prepares a reference map based on the links it encounters to add backlinks
	"""
	global LEVEL
	global reference_map
	global filename
	for i in range(LEVEL):
		file_references = re.findall("\[\[(.*?)\]\]", txt)
		if file_references != []:
			try:
				for i in file_references:
					if filename[3:] not in reference_map[i]:
						reference_map[i].append(filename[3:])
			except KeyError:
				reference_map[i] = [filename[3:]]
		txt = re.sub("\[\[(.*?)\]\]","[\\1](\\1.md)",txt)
	return txt

def set_filename(fname):
	"""Sets the filename of the current file that is being worked on. Essential for
	backlinks, as this filename is appended to the backlinks reference map

	Args:
		fname (String): the name of the file that is currently being parsed
	"""
	global filename
	filename = fname
	return


# example test case
#txt = "This is a [[reference]] in a [[text file]]" 
