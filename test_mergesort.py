from mergesort import mergesort
import random

def int_gt(a, b):
    return a >= b

random_list = [random.randint(0, 100) for _ in range(20)]
print(random_list)

sorted_list = mergesort(random_list, int_gt)
print(sorted_list)