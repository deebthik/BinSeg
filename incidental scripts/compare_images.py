from PIL import Image
from PIL import ImageChops
import os
import numpy as np

s = []

import os
import re

def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

a = os.listdir("/Users/deebthik/Desktop/predictions/plc_binaries_dataset_1/segmentation_results_1")
a = natural_sort(a)
a.remove(".DS_Store")


for i in a:

    print (i)

    if os.path.exists("/Users/deebthik/Desktop/predictions/plc_binaries_dataset_1/segmentation_results_1/"+i):

        img1 = Image.open("/Users/deebthik/Desktop/predictions/plc_binaries_dataset_1/segmentation_results_1/"+i)
        img2 = Image.open("/Users/deebthik/Desktop/predictions/plc_binaries_dataset_1/our_groundtruth/"+i)

        l1, l2 = [], []

        for y in range(img1.height):
          for x in range(img1.width):
            pixel = img1.getpixel((x, y))
            l1 += [pixel]

        for y in range(img2.height):
          for x in range(img2.width):
            pixel = img2.getpixel((x, y))
            l2 += [pixel]

        count = 0

        for i in range(len(l1)):
            if l1[i] == l2[i]:
                count += 1

        s += [float(count/len(l1))]

    else:
        pass








'''for i in range(0, 3576):

    print (i)

    if os.path.exists("/Users/deebthik/Desktop/predictions/bag_dataset_6/segmentation_results_1/decimal"+str(i)+".png"):

        img1 = Image.open("/Users/deebthik/Desktop/predictions/bag_dataset_6/segmentation_results_1/decimal"+str(i)+".png")
        img2 = Image.open("/Users/deebthik/Desktop/predictions/bag_dataset_6/our_groundtruth/decimal"+str(i)+".png")

        l1, l2 = [], []

        for y in range(img1.height):
          for x in range(img1.width):
            pixel = img1.getpixel((x, y))
            l1 += [pixel]

        for y in range(img2.height):
          for x in range(img2.width):
            pixel = img2.getpixel((x, y))
            l2 += [pixel]

        count = 0

        for i in range(len(l1)):
            if l1[i] == l2[i]:
                count += 1

        s += [float(count/len(l1))]

    else:
        pass'''


print (float(sum(s)/len(a)))
