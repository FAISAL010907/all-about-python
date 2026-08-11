# QUESTION 1 ))
"""1. Write a program to find the greatest of four numbers entered by the user """

#  SOLUTION 1 )

a = int(input("enter your number : "))
b = int(input("enter your number : "))
c = int(input("enter your number : "))
d = int(input("enter your number : "))

if(a>b and a>c and a>d):
    print("the greaters number is a :", a)

elif(b>a and b>c and b>d):
    print(b, "is greater")

elif(c>b and c>a and c>d):
    print("the greaters number is c :", c)

elif(d>b and d>c and d>a):
    print("the greaters number is d :", d)
else:
    print("all the input numbers are same")

