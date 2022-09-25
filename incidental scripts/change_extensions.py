import os

import re

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)





l_main = os.listdir("/Users/deebthik/Desktop/canvas_dataset/SegmentationClassRaw")
l_main = natural_sort(l_main)

os.chdir("/Users/deebthik/Desktop/canvas_dataset/SegmentationClassRaw")

for i in range(len(l_main)):
    os.rename(l_main[i], l_main[i][:-4:]+"png")
