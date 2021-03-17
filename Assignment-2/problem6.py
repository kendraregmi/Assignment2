# Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.


my_list= ['krishan', 'john', 'bikalpa', 'sanjaya', 'guman', 'suman']

for items in my_list:
    flag= 0
    if items=='john':
        print("the item is in index ", my_list.index("john"))
        flag= 1
        break
if flag==0:
    print("not found")