from PIL import Image
import os
filenames = (os.listdir("/Users/deebthik/Desktop/bag_dataset_2/JPEGImages"))
filenames.remove(".DS_Store")

for i in range(len(filenames)):
    filenames[i] = "/Users/deebthik/Desktop/bag_dataset_2/JPEGImages/" + filenames[i]

sizes = [Image.open(f, 'r').size for f in filenames]
print (max(sizes))
