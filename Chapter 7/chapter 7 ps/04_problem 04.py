# QUESTION 4 ))
'''4. Write a program to find whether a given number is prime or not.'''

# SOLUTION :-
 
n = int(input("enter your number : "))

for i in range(2,n):
    if(n%i)==0 :
        print(n," is not a prime number")
        break
else:
        print(n,' is a prime number')
