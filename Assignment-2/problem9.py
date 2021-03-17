# Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.

# def binary_search(my_list, item, flag):
#     for i in my_list:
#         if i==item:
#             flag= True
#             return (my_list.index(i), True)
#     return -1, False
            

# def flag_check(flag, position):
#     if flag:
#         print(position)
#     else:
#         print(-1)

# my_list= [2,4,6,8,10,12,14]
# my_list.sort
# position, flag= binary_search(my_list, 100, False)
# flag_check(flag, position)


def binary_search(arr, low, high, x):
 
    if high >= low:
        mid = (high + low) // 2
        
        if arr[mid] == x:
            return mid
 
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        return -1
 
arr = [ 2,4,6,8,10,12 ]
x = 10

result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")