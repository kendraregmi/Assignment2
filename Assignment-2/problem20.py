# 20. Write a Python class to find the three elements that sum to zero from
# a list of n real numbers.
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]


def sum_three_zero(my_list, n):
 
    found = False
    for i in range(0, n-2):
     
        for j in range(i+1, n-1):
         
            for k in range(j+1, n):
             
                if (my_list[i] + my_list[j] + my_list[k] == 0):
                    print(my_list[i], my_list[j], my_list[k])
                    found = True
     
    if (found == False):
        print(" not exist ")
 
my_list = [-25, -10, -7, -3, 2, 4, 8, 10]
n = len(my_list)
sum_three_zero(my_list, n)