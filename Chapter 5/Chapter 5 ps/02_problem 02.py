# QUESTION 2 ))
"""Write a program to input eight numbers from the user and display all the unique numbers
(once)."""

# SOLUTION :-

s = set()

n = input("enter the number : ")
s.add(int(n))
n = input("enter the number : ")
s.add(int(n))
n = input("enter the number : ")
s.add(int(n))
n = input("enter the number : ")
s.add(int(n))
n = input("enter the number : ")
s.add(int(n))
n = input("enter the number : ")
s.add(int(n))
n = input("enter the number : ")
s.add(int(n))
n = input("enter the number : ")
s.add(int(n))

print(s,type(s))