"""
Pushes all the files to github
"""


import os
from datetime import datetime

def push():
	os.system(f'git add ./../docs; git commit -m "backup_push {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}" && git push')
