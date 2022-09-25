import os
import re

def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

a = os.listdir("/Users/deebthik/Desktop/plc_binaries/JPEGImages")
a = natural_sort(a)
a = [a.pop()] + a

train = a[:40712:]
val = a[40712::]

file = open("/Users/deebthik/Desktop/plc_binaries/ImageSets/Segmentation/val.txt", "w")
for line in a:
    file.write(line[:-4:])
    file.write("\n")
file.close()
