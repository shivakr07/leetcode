# arr = [1,2,3,4,5]
# k = 2
# arr = [1,2,3,4,5,6]
# k = 5
# this will create a problem when length become smaller
#  so you need to process one by one
# while len(arr) >  1:
#     i = 0
#     print(arr)
#     arr.extend(arr[i:i+k-1])
#     print(arr[i+k-1])
#     arr = arr[i+k:]
#     # print(arr)
#     # arr.pop(0)
# print(arr)

# ------------------------------------------------------
arr = [1,2,3,4,5]
k = 2
# arr = [1,2,3,4,5,6]
# k = 5

while len(arr) > 1:
    i = 0
    lim = i+k-1
    while i < lim:
        x = arr.pop(0)
        print(x)
        arr.append(x)
        i += 1
    arr.remove(arr[0])
    # print(y)
print(arr)









# ----------------------------------------------------------
# i = 0
# while i < 3:
#     x = arr.pop(0)
#     arr.append(x)
#     i += 1
# print(arr)