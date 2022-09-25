from PIL import Image
from PIL import ImageChops
import os
import numpy as np
import numpy

import re



color2index = {(0, 0, 0): 0, (255, 0, 0): 1, (0, 255, 0): 2}

def rgb_to_index(filename):
    imgg = Image.open("/Users/deebthik/Desktop/bag_dataset_4/Segmentation/"+filename)
    dim1, dim2 = imgg.size[0], imgg.size[1]
    index_data = numpy.zeros((dim1, dim2), dtype=numpy.uint8)
    rgb_data = np.array(Image.open("/Users/deebthik/Desktop/bag_dataset_4/Segmentation/"+filename))
    for i in range(dim1):
        for j in range(dim2):
            index_data[i][j] = color2index[tuple(rgb_data[i][j])]
    img = Image.fromarray(index_data)
    img.save("/Users/deebthik/Desktop/bag_dataset_4/SegmentationClassRaw/"+filename)




def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

a = os.listdir("/Users/deebthik/Desktop/bag_dataset_4/Segmentation")
a = natural_sort(a)

for i in a:
    rgb_to_index(i)
