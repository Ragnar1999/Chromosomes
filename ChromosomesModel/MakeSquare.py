from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import os
def make_square(im, min_size=150, fill_color=(255, 255, 255, 0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

path="D:\\Learn\\大三下\\summer\\正常归类\\998正常染色体(5号)\\abnormal_100"
os.chdir(path)
image = os.listdir(path)
print(len(image))
#
for i in range(0,len(image)):
    path="D:\\Learn\\大三下\\summer\\正常归类\\998正常染色体(5号)\\abnormal_100"
    os.chdir(path)
    test_image = Image.open(image[i])
    new_image = make_square(test_image)
    path='D:\\Learn\\大三下\\summer\\正常归类\\998正常5_resized\\'
    os.chdir(path)
    new_image.save(image[i],dpi=(1000.0,1000.0,0))