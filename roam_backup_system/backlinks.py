import re

from fix_links import reference_map

def add_backlink():

    # now we get the entire reference map
    
    for i in reference_map.keys():
        # TODO: HAS TO BE CHANGED IN THE FUTURE. VERY MESSY FILEPATH
        with open("./../docs/"+i+".md", 'a') as f:
            f.write('\n \n # Backlinks  ')
            f.write('\n \n')
            for j in reference_map[i]:
                f.write(f'- [{j[:-3]}]({j}) \n')
    
    print("Finished Updating References")

