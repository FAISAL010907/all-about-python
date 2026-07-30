# QUESTION 8 ))
'''If languages of two friends are same; what will happen to the program in problem 6?'''

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

"""Nothing will happen , the value can be same"""
