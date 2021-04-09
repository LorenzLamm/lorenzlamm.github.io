from matplotlib import pyplot as plt
import numpy as np
import sys
import os





def make_images_squared(in_path):
    if len(in_path) < 1:
        in_path = ['/Users/lorenz.lamm/PhD_projects/group_website/lorenzlamm.github.io/images/basic_squared.png']
    in_path = in_path[0]
    img = plt.imread(in_path)
    shape = img.shape
    for i in range(2):
        if shape[i] % 2 != 0:
            img = np.delete(img, (0), axis=i)
    shape = img.shape

    max_side = np.argmax(shape)
    max_len = shape[max_side]
    min_side = 1 - max_side
    min_len = shape[min_side]
    diff = max_len - min_len
    print(np.min(img))
    print(img.dtype)
    if diff > 0:
        new_img = np.zeros((max_len, max_len, shape[2]), dtype=img.dtype)
        for i in range(shape[2]):
            if min_side == 0:
                new_img[int(diff / 2):-int(diff / 2), :, i] = img[:, :, i]
            else:
                new_img[:, int(diff / 2):-int(diff / 2), i] = img[:, :, i]
    plt.imsave(os.path.splitext(in_path)[0] + '_squared.png', new_img)





if __name__ == '__main__':
    make_images_squared(sys.argv[1:])