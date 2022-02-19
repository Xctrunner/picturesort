import random

def merge_lists(elt1gt2, list_1, list_2, *sort_func_args):
    sorted_list = []
    while len(list_1) > 0 and len(list_2) > 0:
        elt1 = list_1[0]
        elt2 = list_2[0]
        if elt1gt2(elt1, elt2, *sort_func_args):
            sorted_list.append(elt1)
            del list_1[0]
        else:
            sorted_list.append(elt2)
            del list_2[0]
    sorted_list += list_1 + list_2
    return sorted_list

def mergesort(picture_list, sort_func, sorted_lists, *sort_func_args):
    if not sorted_lists:
        picture_list = [[elt] for elt in picture_list]
    random.shuffle(picture_list)
    while len(picture_list) > 1:
        list_1 = picture_list.pop(0)
        list_2 = picture_list.pop(0)
        sorted_list = merge_lists(sort_func, list_1, list_2, *sort_func_args)
        picture_list.append(sorted_list)
    return picture_list[0]