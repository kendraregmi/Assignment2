# 7. Create a list of tuples of first name, last name, and age for your friends
# and colleagues. If you don't know the age, put in None. Calculate the
# average age, skipping over any None values. Print out each name,
# followed by old or young if they are above or below the average age.

tuple1 = ('Jon', 'Cena', 50)
tuple2 = ('Randy', 'Orton', 35)
tuple3 = ('George', 'Bush', None)
tuple4 = ('HAppy', 'Singh', None)
tuple5 = ('Hari', 'Mani', 80)
tuples = [tuple1, tuple2, tuple3, tuple4, tuple5]
ageSum = 0
count = 0
for t in tuples:
    if t[2] is not None:
        ageSum += t[2]
        count += 1
avg = ageSum / count
for t in tuples:
    if t[2] is not None:
        if t[2] > avg:
            print(t[0] + " " + t[1] + " " + "OLD")
        else:
            print(t[0] + " " + t[1] + " " + "YOUNG")
    else:
        print(t[0] + " " + t[1])
