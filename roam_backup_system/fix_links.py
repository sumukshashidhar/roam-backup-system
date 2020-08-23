#!/usr/local/bin/python3
import re


# this is to tell it how deep it should look for references
LEVEL = 3
reference_map = {}
filename = ''
def reference_fix(txt):
	"""
	Fixes roam research references
	"""
	global LEVEL
	global reference_map
	global filename
	for i in range(LEVEL):
		file_references = re.findall("\[\[(.*?)\]\]", txt)
		if file_references != []:
			try:
				for i in file_references:
					reference_map[i].append(filename[3:])
			except KeyError:
				reference_map[i] = [filename[3:]]
		txt = re.sub("\[\[(.*?)\]\]","[\\1](\\1.md)",txt)
	print(reference_map)
	return txt

def set_filename(fname):
	global filename
	filename = fname
	return


# example test case
#txt = "This is a [[reference]] in a [[text file]]" 
