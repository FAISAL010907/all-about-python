#  QUESTION 1 ))
'''Write a program using functions to find greatest of three numbers.'''

# SOLUTION 1:-
a = float(input("enter your number : "))
b = float(input("enter your number : "))
c = float(input("enter your number : "))
def greater():
    if(a>b and a>c):
        print(a,"is the greatest number amongst a,b and c")

    elif(b>a and b>c):
        print(b,"is the greatest number amongst a,b and c")

    elif(c>a and c>b):
        print(c,"is the greatest number amongst a,b and c")

    else:
        print("all the inputs are same")

greater()

#  if values are given then just do this in fxn, def greater(a,b,c) and then in last mention the given value like a =1 b = 2 c=3
