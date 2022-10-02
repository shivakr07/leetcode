import functools
  
  
def mycmp(a, b):
    print("comparing ", a, " and ", b)
    if a > b:
        return -1
    elif a < b:
        return 1
    else:
        return 0
  
# what ever case you make -1 sorting will be done according to that
print(sorted([1, 2, 4, 2], key=functools.cmp_to_key(mycmp)))