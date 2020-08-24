import os
BACKUP_DIR = "./../docs/"
def add_yml():
    """Updates the github pages config. In this case, sets the cayman theme
    """
    global BACKUP_DIR
    with open(BACKUP_DIR+'_config.yml', 'w+') as f:
        f.write("theme: jekyll-theme-cayman")
