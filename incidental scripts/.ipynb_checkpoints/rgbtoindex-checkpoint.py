from PIL import Image
from PIL import ImageChops
import os
import numpy as np
import numpy

import re



color2index = {(0, 0, 0): 0, (255, 0, 0): 1, (0, 255, 0): 2}

def rgb_to_index(filename):
    index_data = numpy.zeros((256, 256), dtype=numpy.uint8)
    rgb_data = np.array(Image.open("/Users/deebthik/Documents/NYUAD Internship/images_256_fixed/col256/"+filename))
    for i in range(256):
        for j in range(256):
            index_data[i][j] = color2index[tuple(rgb_data[i][j])]
    img = Image.fromarray(index_data)
    img.save("/Users/deebthik/Documents/NYUAD Internship/images_256_fixed/segmentationclassraw/"+filename)




def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

a = os.listdir("/Users/deebthik/Documents/NYUAD Internship/images_256_fixed/col256")
a = natural_sort(a)

for i in a:
    rgb_to_index(i)
