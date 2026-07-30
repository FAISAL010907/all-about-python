#  QUESTION 6 ))
"""Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
use key as their names. Assume that the names are unique ? """

# SOLUTION 1 :-
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

# output = 

''' enter your name : faisal
enter your language : hindi
enter your name : gg
enter your language : marathi
enter your name : harshh
enter your language : urdu
enter your name : harry
enter your language : arbi
{'faisal': 'hindi', 'gg': 'marathi', 'harshh': 'urdu', 'harry': 'arbi'} '''