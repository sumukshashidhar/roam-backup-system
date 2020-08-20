# roam-backup-system
A simple roam research backup system written in python that backs up to git, and handles backlinks and references


# Instructions for Use

1. Download a markdown formatted backup from Roam Research
2. Create a repository on github, and clone it to your computer
3. Add the roam_backup_system folder to the github repository
4. Modify your gitignore to ignore the ```roam_backup_system``` folder and the regular markdown files in the root directory
5. Copy your files over to the repository
6. From the root of your repository, run ```python roam_backup_system/main.py```
7. ....
8. Profit!


# Word of Warning

In order to deal with markdown links and make github pages feasible, this program replaces all whitespaces in markdown files with an underscore. Please make another backup of your files before performing this operation to retain the whitespaces as they are in your markdown files. 

Alternatively, wait for the next update which will bring a back converter to the table which will convert your files back once the operations are done.



# Contributing

Contributions, either in the form of pull requests or issues or general suggesstions are welcome. 
