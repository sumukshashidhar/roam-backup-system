# module imports
import argparse

# file imports
import git_push as gitpusher
from enumeration import enum
import fs
from backlinks import add_backlink as add_backlinks
from index_creator import create_index as create_index
from github_config_update import add_yml as ymladd


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-p", "--push", help="Push to Github")
	args = parser.parse_args()
	GITPUSH = args.push if args.push is not None else True
	# first enumerate the directories and get all filenames
	files = enum()
	# make the backup dir. 
	fs.make_dir()
	# then enumerate over the files, and fix them
	for i in files:
		fs.fix_file("../"+i)

	# add backlinks to all files
	add_backlinks()

	# create index in all files
	create_index()

	# add the yml file
	ymladd()

	# push to github if needed
	if GITPUSH:
		gitpusher.push()
