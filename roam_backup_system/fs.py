"""
Will read a file, and then subsequently create another file with 
fixed references
"""


# since i'm using github pages, I will use the docs/ directory
BACKUP_DIR = './../docs'

import os

from fix_links import reference_fix as rf
from fix_links import set_filename as sf
import shutil
def make_dir():
	"""Removed the existing backup directory and makes a new one in its place. 

	The old one is removed as it may contain deleted files that are hard to track. 
	"""
	global BACKUP_DIR
	if not os.path.exists(BACKUP_DIR):
		os.makedirs(BACKUP_DIR)
	else:
		shutil.rmtree(BACKUP_DIR)
		os.makedirs(BACKUP_DIR)



def fix_file(filename):
	"""Abstraction for fixing a file and its references, as well as saving it in the backup directory. 
	Opens the file, fixes each line and its references induvidually, and writes it in the backup directory

	Args:
		filename (String): The name of the file that must be modified
	"""
	global BACKUP_DIR
	# open the file first
	lines = [] # store the lines of the file in a list
	# print("Working with file: ", filename)
	sf(filename)
	with open(filename, 'r') as f:
		lines = f.readlines()
	fixed_lines = []
	for i in lines:
		fixed_lines.append(rf(i))
	with open(BACKUP_DIR+'/'+filename[3:], 'w+') as f:
		f.writelines(fixed_lines)



#fix_file('test')
