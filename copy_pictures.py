import os
import shutil

def copy_list_of_img(img_list, new_dir):
    os.makedirs(new_dir, exist_ok=True)
    img_index = 0
    for img in img_list:
        shutil.copyfile(img, os.path.join(new_dir, "{:0>3d}_{}".format(img_index, os.path.basename(img))))
        img_index += 1