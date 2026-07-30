#  QUESTION 7 ))
"""f the names of 2 friends are same; what will happen to the program in problem 6?"""

# SOLUTION :- 
fav_lang = {}

n = input("enter your name : ")
m = input("enter your language : ")
fav_lang.update({n:m})
n = input("enter your name : ")
m = input("enter your language : ")
fav_lang.update({n:m})
n = input("enter your name : ")
m = input("enter your language : ")
fav_lang.update({n:m})
n = input("enter your name : ")
m = input("enter your language : ")
fav_lang.update({n:m})

print(fav_lang)

# The value entered later will be updated 
