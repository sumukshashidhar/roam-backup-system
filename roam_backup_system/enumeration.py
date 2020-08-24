"""
To enumerate all files in the given directory only

Version 2: Will support sub directories

"""


from os import listdir
from os.path import isfile, join


# ignore all files that you don't want to commit
IGNORE = ['.DS_Store', '.gitignore', '.git', 'docs', 'README.md', 'LICENSE.txt']

def enum(PATH=None):
	"""Returns all files in a given directory, except the ignored files

	Args:
		PATH (String, optional): The path that needs to be enumerated. Defaults to None.

	Returns:
		list: the list of all files in the path, except the ignore files
	"""
	paths = "./../" if PATH is None else PATH
	onlyfiles = [f for f in listdir(paths) if isfile(join(paths, f))]
	
	for i in IGNORE:
		try:
			onlyfiles.remove(i)
		except:
			pass
	
	return onlyfiles


# print(enum())

