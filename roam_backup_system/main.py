# CONSTANTS: MODIFY FOR YOUR NEEDS


import git_push as gitpusher
from enumeration import enum

GITPUSH = False 



if __name__ == "__main__":
	# first enumerate the directories
	files = enum()
	print(files)
	if GITPUSH:
		gitpusher.push()
