import os

import re

def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)





l_main = os.listdir("/Users/deebthik/Desktop/canvas_dataset/JPEGImages")
l_main = natural_sort(l_main)
l_main = l_main[:-1:]

l_seg = os.listdir("/Users/deebthik/Desktop/canvas_dataset/SegmentationClass")
l_seg = natural_sort(l_seg)

l_seg_raw = os.listdir("/Users/deebthik/Desktop/canvas_dataset/SegmentationClassRaw")
l_seg_raw = natural_sort(l_seg_raw)

os.chdir("/Users/deebthik/Desktop/canvas_dataset/SegmentationClass")

for i in range(len(l_main)):
    os.rename(l_seg[i], l_main[i][:-3:]+"png")
