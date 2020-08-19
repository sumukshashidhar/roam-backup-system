"""
Will read a file, and then subsequently create another file with 
fixed references
"""


# since i'm using github pages, I will use the docs/ directory
BACKUP_DIR = 'docs'

import os

def make_dir():
	global BACKUP_DIR
	if not os.path.exists(BACKUP_DIR):
		os.makedirs(BACKUP_DIR)


