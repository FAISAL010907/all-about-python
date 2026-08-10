# QUESTION 4 ))
'''Write a program to find whether a given username contains less than 10 characters or not.'''

# SOLUTION 1 :-
a = input("enter your username : ")
b = len(a)
if(len(a)>10):
    print("there are",b, "so username contain more than 10 character ")
#you can write the previous line as print(f"there are {b} character so the characteusername gave b character)
else:
    print(" username contain less than 10 character ")