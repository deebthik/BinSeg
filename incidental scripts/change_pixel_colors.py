#this script is used to change colors of image predicted by Deeplab (colors were flipped and were of different shade)

import numpy as np
from PIL import Image
import os


import os
import re

def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

a = os.listdir("/Users/deebthik/Desktop/predictions/plc_binaries_dataset_1/segmentation_results_3")
a = natural_sort(a)




'''for i in range(0, 3576):

    print (i)

    if os.path.exists("/Users/deebthik/Desktop/predictions/bag_dataset_7/segmentation_results_1/decimal"+str(i)+".png"):

        im = Image.open("/Users/deebthik/Desktop/predictions/bag_dataset_7/segmentation_results_1/decimal"+str(i)+".png")
        data = np.array(im)

        r1, g1, b1 = 128, 0, 0 # Original value
        r2, g2, b2 = 0, 255, 0 # Value that we want to replace it with

        red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
        mask = (red == r1) & (green == g1) & (blue == b1)
        data[:,:,:3][mask] = [r2, g2, b2]

        im = Image.fromarray(data)
        im.save("/Users/deebthik/Desktop/predictions/bag_dataset_7/segmentation_results_1/decimal"+str(i)+".png")'''





for i in a:

    print (i)

    if os.path.exists("/Users/deebthik/Desktop/predictions/plc_binaries_dataset_1/segmentation_results_3/"+i):

        im = Image.open("/Users/deebthik/Desktop/predictions/plc_binaries_dataset_1/segmentation_results_3/"+i)
        data = np.array(im)

        r1, g1, b1 = 0, 128, 0 # Original value
        r2, g2, b2 = 255, 0, 0 # Value that we want to replace it with

        red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
        mask = (red == r1) & (green == g1) & (blue == b1)
        data[:,:,:3][mask] = [r2, g2, b2]

        im = Image.fromarray(data)
        im.save("/Users/deebthik/Desktop/predictions/plc_binaries_dataset_1/segmentation_results_3/"+i)
