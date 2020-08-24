import re

from fix_links import reference_map

def add_backlink():
    """Adds backlinks to all files as in roam_research

    Uses the reference map prepared while fixing the files in the fs module, and using it, adds backlinks
    to other files
    """
    for i in reference_map.keys():
        # TODO: HAS TO BE CHANGED IN THE FUTURE. VERY MESSY FILEPATH
        with open("./../docs/"+i+".md", 'a') as f:
            f.write('\n \n# Backlinks')
            f.write('\n \n')
            for j in reference_map[i]:
                f.write(f'- [{j[:-3]}]({j}) \n')
    
    print("Finished Updating References")

