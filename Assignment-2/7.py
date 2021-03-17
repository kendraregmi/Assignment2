tuple1 = ('Solam', 'Rana', 22)
tuple2 = ('Manu', 'Pantha', 21)
tuple3 = ('Amrita', 'Pandey', None)
tuple4 = ('Sabnam', 'Pandit', None)
tuple5 = ('Anupama', 'Giri', 27)
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
