# QUESTION 1)) 
""" Write a python program to display a user entered name followed by "good afternoon" using input function? """

#SOLUTIONS 1 :-

name = input("enter your name:  ")
print("good afternoon " + name )

#SOLUTION 2 :-

# using f string, means you allot a name to string like :-
#suppose gender = boy ,and we want to print faisal is a good {gender} in the end 
#so we will do it like print(f"faisal is a good {gender}")

name = input("enter your name :  ")
print(f"good afternoon {name}")
#here by writing f in start we are allotion the name to the string "good afternoon"