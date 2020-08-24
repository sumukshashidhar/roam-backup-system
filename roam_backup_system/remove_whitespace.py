from enumeration import enum
import os

def rem_whitespaces():
	files = enum()
	for i in files:
		print(i)
		os.rename("./../"+i, "./../"+i.replace(" ", "_"))

def remove_question_marks():
	files = enum()
	for i in files:
		if i.find('?') != -1:
			lines = []
			with open("./../"+i, 'r') as f:
				lines = f.readlines()
			with open("./../"+i.replace("?", ""), 'w+') as f:
				f.writelines(lines)
			os.remove("./../"+i)
