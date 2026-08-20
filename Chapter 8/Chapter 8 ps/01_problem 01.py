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