# QUESTION 1 ))
'''Write a program to print multiplication table of a given number using for loop'''

# SOLUTION 1 :-
N = int(input("enter your number : "))

for i in range(11):
    print(f"{N} times {i} = {N*i}")


print("+=============================================+")

# BASIC MISTAKE I DID :
# i didnt use the data type itn() byt this the output s like

P = input("enter number for patter :  ")

for j in range(0,11):
    print(f"{P} with {j} = {P*j}")

#in thsi case output is 
'''1 with 1 = 1
1 with 2 = 11
1 with 3 = 111
1 with 4 = 1111
1 with 5 = 11111
1 with 6 = 111111
1 with 7 = 1111111
1 with 8 = 11111111
1 with 9 = 111111111
1 with 10 = 1111111111'''