# QUESTION 8 ))
'''Write a program to print the following star pattern:
*
**
*** for n = 3'''

# SOLUTION :-
n = int(input("enter your number : "))
for i in range (1,n+1):

    print("*"* (i), end ="")
    print("")