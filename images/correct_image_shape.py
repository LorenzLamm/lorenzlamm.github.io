from matplotlib import pyplot as plt
import numpy as np
import sys
import os
from PIL import Image





def make_images_squared(in_path):
    if len(in_path) < 1:
        in_path = ['/Users/lorenz.lamm/PhD_projects/group_website/lorenzlamm.github.io/images/basic_squared.png']
    for cur_path in in_path:

        img = Image.open(cur_path)

        print(img.size)
        desired_shape = (2200, 1001)
        img = img.resize(desired_shape, Image.ANTIALIAS)
        print(img.size)
        img.save(os.path.splitext(cur_path)[0] + '_shaped.png', "PNG")







if __name__ == '__main__':
    make_images_squared(sys.argv[1:])