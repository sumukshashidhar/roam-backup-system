"""
To enumerate all files in the given directory only

Version 2: Will support sub directories

"""


from os import listdir
from os.path import isfile, join


# ignore all files that you don't want to commit
IGNORE = ['.DS_Store', '.gitignore', '.git', 'docs']
PATH = '../'

def enum():
	mypath = '.'
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	
	for i in IGNORE:
		try:
			onlyfiles.remove(i)
		except:
			pass
	
	return onlyfiles


# print(enum())

