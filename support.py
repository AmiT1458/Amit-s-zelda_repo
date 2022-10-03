from csv import reader
import os
from os import walk

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map,delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

#print(import_csv_layout(os.path.join('map','map_FloorBlocks.csv')))

def import_folder(path):
    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + imaga
            print(full_path)

import_folder('..\graphics\grass')
