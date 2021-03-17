# Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.


people= []

name3_tup= ('Sanjaya', 'Shrestha', 25)
people.append(name3_tup)

name1_tup= ('Kendra', 'Regmi', 25)
people.append(name1_tup)

name2_tup= ('Krishan', 'Bhat', 25)
people.append(name2_tup)

print(people)

people.sort()
print(people)


print(sorted(people, key=lambda x: x[1] ))
