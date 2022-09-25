from PIL import Image
import os

def crop_img(name,new_dimension):

	load_path= '/Users/deebthik/Desktop/bag_dataset_8/Segmentation/'
	save_path = '/Users/deebthik/Desktop/bag_dataset_8/SegmentationSliced/'
	img = Image.open(load_path+name)
	old_dimension = img.size[0]

	if old_dimension==new_dimension:
	    img.save(save_path+name,quality=100)

	if old_dimension > new_dimension:
	    num_row = int(old_dimension/new_dimension)
	    crop = pow(num_row,2)

	    for i in range(crop):

	        x = (i*new_dimension)%old_dimension
	        y = (i//num_row)*new_dimension

	        cropped = img.crop((x,y,x+new_dimension,y+new_dimension))
	        cropped.save(save_path + name.strip('.png') +  "-" + str(i) + ".png",quality=100)

path = '/Users/deebthik/Desktop/bag_dataset_8/Segmentation'
arr = os.listdir(path)

for name in arr:
    if name.endswith('png'):
        crop_img(name,64)
