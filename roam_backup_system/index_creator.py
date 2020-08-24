from enumeration import enum

DOCS_PATH = "./../docs/"
def create_index():
    global DOCS_PATH
    files = enum(DOCS_PATH)
    with open("./../docs/"+"index.md", 'w+') as f:
        f.write("# List of All Files.\n")
        f.write("\n")
        for i in files:
            f.write(f"* [{i}](./{i}.md)\n")