# roam-backup-system
A simple roam research backup system written in python that backs up to git, and handles backlinks and references


# Instructions for Use
## Initial Setup
**This is the hard part, once you get this out the way, regular backups are extremely easy to do!**
1. Download a markdown formatted backup from Roam Research
2. Create a repository on github, and clone it to your computer. While creating the repository, be sure to add the Python gitignore to make sure that temporary python and cache files are not commited. 
3. Add the `roam_backup_system` folder to the github repository that you have just clone to your computer. 
4. Export a markdown zip file from [Roam Research](https://roamresearch.com) and unzip the files. 
5. Copy all the files over to the repository that you just cloned with github. 
6. All files are pushed to github by default. If you want to change this behaviour, add the `-p` or `--push` flag along with your python file to stop autopushing!
7. Navigate inside the ```roam_backup_system``` and run the ```main.py``` file, with `python3 main.py` or `python main.py`.
8. Go onto GitHub Repository settings, and enable GitHub Pages to be served from the `master_branch/docs` folder


# Word of Warning

In order to deal with markdown links and make github pages feasible, this program replaces all whitespaces in markdown files with an underscore. Please make another backup of your files before performing this operation to retain the whitespaces as they are in your markdown files. 

Alternatively, wait for the next update which will bring a back converter to the table which will convert your files back once the operations are done.



# Contributing

Contributions, either in the form of pull requests or issues or general suggesstions are welcome. 
