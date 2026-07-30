# QUESTION 1 ))
"""Write a program to create a dictionary of Hindi words with values as their English
translation. Provide user with an option to look it up!"""

#  SOLUTION 1 :-
dict = { "kitab" :"Book" ,
         "pani" : "Water",
         "ghar" : "House" ,
         "dost" : "Friend",
         "samay" : "Time",
         "khana" : "Food"
         }

a = input("enter word : ")
print("the word in english is ", dict[a])

print("======================================")

# also we can do it this way :- 
a = input("enter word : ")
print(f"the word in english is {dict.get(a)}")
