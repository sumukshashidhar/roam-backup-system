from enumeration import enum
import re
DOCS_PATH = "./../docs/"

def identify_log_days(files):
    onlylogs = []
    for i in files:
        regex = r"(\b\d\d[trns][thd], 20\d\d.md|\b\d[trns][thd], 20\d\d.md)"
        text = re.findall(regex, i)
        if text != [] and text is not None and text != '':
            onlylogs.append(i)
    return onlylogs


def create_index():
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
