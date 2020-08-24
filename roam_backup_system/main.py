# CONSTANTS: MODIFY FOR YOUR NEEDS


import git_push as gitpusher
from enumeration import enum
from remove_whitespace import rem_whitespaces as rw
from remove_whitespace import remove_question_marks as rq
import fs
from backlinks import add_backlink as add_backlinks
from index_creator import create_index as create_index

GITPUSH = False 


if __name__ == "__main__":
	# let us run the whitespace remover first, to ensure everything
	# has an underscore - GH pages does not recognize links without it
	# rw() # appears as though whitespaces are being handled well. No need of this random stuff
	rq()
	# first enumerate the directories
	files = enum()
	# make the backup dir if it doesn't exist at first
	fs.make_dir()
	# then enumerate over the files
	for i in files:
		fs.fix_file("../"+i)

	# add backlinks
	add_backlinks()

	# create index
	create_index()

	if GITPUSH:
		gitpusher.push()
