import os
BACKUP_DIR = "./../docs/"
def add_yml():
    global BACKUP_DIR
    with open(BACKUP_DIR+'_config.yml', 'w+') as f:
        f.write("theme: jekyll-theme-cayman")
