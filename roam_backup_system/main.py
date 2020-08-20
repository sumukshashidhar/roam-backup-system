# CONSTANTS: MODIFY FOR YOUR NEEDS


import git_push as gitpusher
from enumeration import enum
import fs
GITPUSH = False 



if __name__ == "__main__":
	# first enumerate the directories
	files = enum()
	print(files)
	# make the backup dir if it doesn't exist at first
	fs.make_dir()
	# then enumerate over the files
	for i in files:
		fs.fix_file("../"+i)
	if GITPUSH:
		gitpusher.push()
