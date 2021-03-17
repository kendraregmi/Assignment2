# Write a function, is_prime, that takes an integer and returns True if the
# number is prime and False if the number is not prime.



def check_prime(num, flag):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                flag=True
                break
    if flag:
        print("Not Prime")
    else:
        print("Prime Number")


num= int(input("Enter the number to check prime"))
check_prime(num, False)