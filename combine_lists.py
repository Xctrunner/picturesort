from get_pictures import get_list_of_img_from_directory, is_left_img_better
from copy_pictures import copy_list_of_img
from mergesort import mergesort
import sys
import math

with open(sys.argv[1], 'r') as f:
    pic_list_1 = f.readlines()[1:]
    pic_list_1 = [x.strip() for x in pic_list_1]
percentage_1 = float(sys.argv[2])
pic_list_1 = pic_list_1[:math.ceil(len(pic_list_1) * percentage_1)]
with open(sys.argv[3], 'r') as f:
    pic_list_2 = f.readlines()[1:]
    pic_list_2 = [x.strip() for x in pic_list_2]
percentage_2 = float(sys.argv[4])
pic_list_2 = pic_list_2[:math.ceil(len(pic_list_2) * percentage_2)]

pic_list = [pic_list_1, pic_list_2]
sorted_pic_list = mergesort(pic_list, is_left_img_better, True)
sorted_pic_list = ['\n' + img for img in sorted_pic_list]
with open(sys.argv[5] + '.txt', 'w') as f:
    f.writelines(sorted_pic_list)

with open(sys.argv[5] + '.txt', 'r') as f:
    img_list = f.readlines()[1:]
img_list = [x.strip() for x in img_list]
copy_list_of_img(img_list, sys.argv[5])