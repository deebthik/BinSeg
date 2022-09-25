import image_slicer
import os
import re

def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

a = os.listdir("/Users/deebthik/Desktop/bag_dataset_7/SegmentationClassRaw")
a = natural_sort(a)
a.remove(".DS_Store")

for i in a:
    image_slicer.slice("/Users/deebthik/Desktop/bag_dataset_7/SegmentationClassRaw/"+i, 4)
