from enumeration import enum
import re
DOCS_PATH = "./../docs/"

def identify_log_days(files):
    """Uses regex to find Log Days in Roam, and exclude them from the main file list. 
    To ensure that the view is not overly cluttered

    Args:
        files (list): The list of all files given by enumeration

    Returns:
        list: a list of all the log days
    """
    onlylogs = []
    for i in files:
        regex = r"(\b\d\d[trns][thd], 20\d\d.md|\b\d[trns][thd], 20\d\d.md)"
        text = re.findall(regex, i)
        if text != [] and text is not None and text != '':
            onlylogs.append(i)
    return onlylogs


def create_index():
    """Creates the index.md file by going over all the files and removing the log days. 
    A better system will be implemented in a future version. 


    Must be noted that this is for backup purposes only, and not for common use
    """
    global DOCS_PATH
    files = enum(DOCS_PATH)
    files.sort()
    logs = identify_log_days(files)
    for i in logs:
        files.remove(i)
    with open("./../docs/"+"index.md", 'w+') as f:
        f.write("# List of All Files.\n")
        f.write("## Pages\n")
        f.write("\n")
        for i in files:
            f.write(f"* [{i[:-3]}](./{i})\n")
        f.write("\n")
        f.write("# Log Days\n")
        for i in logs:
            f.write(f"* [{i[:-3]}](./{i})\n")
        f.write("\n")
