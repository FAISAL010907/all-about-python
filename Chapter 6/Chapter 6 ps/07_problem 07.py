# QUESTION 7 ))
'''Write a program to find out whether a given post by user is talking about "faisal” or not.'''

# SOLUTION 1 :-
post = input("upload your post : ")

if("Faisal".lower() in post.lower()):
    print(" This post is about Faisal")
else:
    print(" This post is not about Faisal")

# Faisal.lower() - this will help when we miss or stuck between caplital and small letter in the post and finding word it will basically ready that capital letter as small

