# QUESTION 10 ))
'''Write a program to print multiplication table of n using for loops in reversed order.'''
 
# SOLUTION :-
n = int(input("enter no. : "))
for i in range (1,11):
    print(f"{n} time {11-i} = {n*(11-i)}")
