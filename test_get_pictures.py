from get_pictures import get_list_of_img_from_directory, is_left_img_better
import sys

picture_list = get_list_of_img_from_directory(sys.argv[1])
# print(picture_list)

# show_two_img(picture_list[0], picture_list[1])

print(is_left_img_better(picture_list[0], picture_list[1]))
