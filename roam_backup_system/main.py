# CONSTANTS: MODIFY FOR YOUR NEEDS

import argparse
import git_push as gitpusher
from enumeration import enum
import fs
from backlinks import add_backlink as add_backlinks
from index_creator import create_index as create_index
from github_config_update import add_yml as ymladd

GITPUSH = True


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-p", "--push", help="Push to Github")
	args = parser.parse_args()
	GITPUSH = args.push if args.push is not None else True
	# let us run the whitespace remover first, to ensure everything
	# has an underscore - GH pages does not recognize links without it
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

	# add the yml file
	ymladd()

	if GITPUSH:
		gitpusher.push()
