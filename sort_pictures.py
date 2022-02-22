from get_pictures import get_list_of_img_from_directory, is_left_img_better
from copy_pictures import copy_list_of_img
from mergesort import mergesort
import sys

pic_list = get_list_of_img_from_directory(sys.argv[1])
# pic_list = ['C:\\Users\\xctru\\coding\\manual_download\\california_2022\\IMG_0573.HEIC', 'C:\\Users\\xctru\\coding\\manual_download\\california_2022\\IMG_0573.HEIC']
# pic_list = ['C:\\Users\\xctru\\coding\\manual_download\\california_2022\\IMG_0503.HEIC', 'C:\\Users\\xctru\\coding\\manual_download\\california_2022\\2022-01-10 15.32.31.jpg']
# pic_list = ['C:\\Users\\xctru\\coding\\manual_download\\california_2022\\2022-01-10 15.32.31.jpg', 'C:\\Users\\xctru\\coding\\manual_download\\california_2022\\2022-01-10 15.32.31.jpg']
sorted_pic_list = mergesort(pic_list, is_left_img_better, False)
sorted_pic_list = ['\n' + img for img in sorted_pic_list]
with open(sys.argv[2], 'w') as f:
    f.writelines(sorted_pic_list)

with open(sys.argv[2], 'r') as f:
    img_list = f.readlines()[1:]
img_list = [x.strip() for x in img_list]
copy_list_of_img(img_list, sys.argv[3])

# C:\Users\Walter\coding\picturesort> python .\sort_pictures.py '../manual_download/2021_07_katahdin' 'katahdin_full.txt' 'katahdin_full'
# C:\Users\Walter\coding\picturesort> python .\combine_lists.py 'gannett_full.txt' .2 'katahdin_full.txt' .2 '20211029_combined'
# python .\sort_pictures.py C:\Users\xctru\coding\manual_download\california_2022 california_full.txt california_full
# C:\Users\xctru\coding\picturesort>python .\combine_lists.py 20211216_combined.txt .8 california_full.txt .3 20220221_combined