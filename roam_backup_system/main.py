# CONSTANTS: MODIFY FOR YOUR NEEDS


import git_push as gitpusher
from enumeration import enum
from remove_whitespace import rem_whitespaces as rw
import fs
GITPUSH = False 



if __name__ == "__main__":
	# let us run the whitespace remover first, to ensure everything
	# has an underscore - GH pages does not recognize links without it
	rw()
	# first enumerate the directories
	files = enum()
	# make the backup dir if it doesn't exist at first
	fs.make_dir()
	# then enumerate over the files
	for i in files:
		fs.fix_file("../"+i)
	if GITPUSH:
		gitpusher.push()
