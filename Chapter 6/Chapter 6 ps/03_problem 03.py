# QUSTION 3 ))
'''A spam comment is defined as a text containing following keywords: “Make a lot of
money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.'''

# SOLUTION 1 :-
l1 = "Make a lot of money"
l2 = "buy now"
l3 = "subscribe this"
l4 = "click this"

message = input("enter your comment : ")

if((l1 in message) or (l2 in message) or (l3 in message)or (l4 in message)):
    print("alert this is spam")
else:
    print(message)