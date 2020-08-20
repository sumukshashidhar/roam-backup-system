from enumeration import enum
import os

def rem_whitespaces():
	files = enum()
	for i in files:
		os.rename(i, "./../"+i.replace(" ", "_"))

