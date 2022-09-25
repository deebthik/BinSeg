from PIL import Image
import os

directory = r'/Users/deebthik/Documents/NYUAD Internship/deeplab/models-master/research/deeplab/datasets/custom_datasets/canvas_dataset/segmentation_color'
c=1
for filename in os.listdir(directory):
    if filename.endswith(".jpeg"):
        im = Image.open("/Users/deebthik/Documents/NYUAD Internship/deeplab/models-master/research/deeplab/datasets/custom_datasets/canvas_dataset/segmentation_color/"+filename)
        name='img'+str(c)+'.png'
        rgb_im = im.convert('RGB')
        rgb_im.save(name)
        c+=1
        print(os.path.join(directory, filename))
        continue
    else:
        continue
