"""
Pushes all the files to github
"""


import os
from datetime import datetime

def push():
	"""Pushes your files to github. Prompts you for a password on the shell if needed else directly pushes
	in case of ssh keys
	"""
	os.system(f'git add ./../docs; git commit -m "backup_push {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}" && git push')
