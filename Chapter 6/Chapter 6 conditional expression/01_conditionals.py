#  CONDITIONAL EXPRESSIONS 
''' we use conditional epressions in python to make decisions/code based on certain conditions.'''

# 1) "if", "elif", "else" statements are used to implement conditional expressions in python.
a = 9
if(a>9):
    print("a is greater than 9")
elif(a<9):
    print("a is less than 9")    
elif(a==9):
    print("a is equal to 9")    
else: 
    print("a is not a number")

#  QUICK QUESTION:
# write a program to print yes when th age entered by the user is greater than or equal to 18 and print no when the age is less than 18.
age = int(input("enter your age : ")) # we need to mention data type like int() or it will give error because input() type caste the str() data type automatically
if(age > 18):
    print("yes")
elif(age<0):
    print("enter the valid age ")
else:
    print("no")



