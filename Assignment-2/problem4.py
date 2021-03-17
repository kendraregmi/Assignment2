# Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?

my_list= ['kendra', 'krishan', 'suman', 'guman', 'bikalpa']
print("ID before soring is", id(my_list))

my_list.sort()

print("ID after soring is", id(my_list)) #no change


print('First item in list is, ', my_list[0])
print('Second item in list is, ', my_list[1])


