from hilbertcurve.hilbertcurve import HilbertCurve
from PIL import Image


def hc_coords(p, n):
    coords = []
    hilbert_curve = HilbertCurve(p, n)
    for i in range(65536):
        coord = hilbert_curve.coordinates_from_distance(i)
        coords += [coord]
    return (coords)



coords = hc_coords(8, 2) #for 256x256 images

bin_l = [] #list of binaries

#img = Image.open()

for i in range(len(65536)) #for 256x256 images
    img.putpixel((coords[i][0], coords[i][1]), (bin_l[i], bin_l[i], bin_l[i]))

#img.save()
