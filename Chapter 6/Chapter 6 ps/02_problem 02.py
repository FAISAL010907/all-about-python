# QUESTION 2 ))
'''Write a program to find out whether a student has passed or failed if it requires a total of
40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
input from the user ?'''

# SOLUTION 2 :-

M1 = int(input("Enter makrs of subject 1 : "))
M2 = int(input("Enter makrs of subject 2 : "))
M3 = int(input("Enter makrs of subject 3 : "))

# Chech for the individual subjects
if(M1/100>=33/100):
    print("you passes subject 1 ")

else:
    print("you failed in  subject 1")

if(M2/100>=33/100):
    print("you passed in subject 2 ")

else:
    print("you failed in  subject 2")

if(M3/100>=33/100):
    print("you passed in subject 3 ")

else:
    print("you failed in  subject 3")

# Check for total percentage 
total_percentage = 100*(M1+M2+M3)/300

if(total_percentage >= 40/100 and M1/100>=33/100 and M2/100>=33/100 and M3/100>=33/100 ):
    print("you are passed the overall exam")

else:
    print("you have failed the overall exam")

