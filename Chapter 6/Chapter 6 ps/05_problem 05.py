# QUESTION 5 ))
'''Write a program which finds out whether a given name is present in a list or not.'''

# SOLUTION 1:-
set = ["faisal","gg","basketball","bb","pandey","dot"]
a = str(input("enter your name : "))

if(a in set): 
    print("it belongs to the list")
else:
    print("it doesnt belongs to the list")