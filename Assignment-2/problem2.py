# 2. Write an if statement to determine whether a variable holding a year is
# a leap year.


year_inp= int(input("Enter the year to determine the leap year or not: "))

if year_inp%4== 0:
    if year_inp%100==0:
        if year_inp%400==0:
            print("Leap year")
        else:
            print("not leap year")
    else:
        print(" leap year")

else:
    print("not Leap year")


