# to ask for users data we can use input() function. It takes input from user and returns it as a string.
# like
a = input(" enter yout name:")
print (a)

# calculation using input() function
a = int(input(" enter first number:"))
b = int(input(" enter second number:"))

print("the sum of two numbers is:", (a) + (b)) 

print("==============================================")

# or you can use int() in the final formula for converting strin valur of a and b to int like this :-
                ##{int(a)+ int(b)}##   

a = (input(" enter first number:"))
b = (input(" enter second number:"))  
print("the sum of two numbers is:", int(a) + int(b))
 # both the code will work same but the second one is more efficient because it will convert the string to int only once.

print("==============================================")

# if you  forget to use data type conversion function like int() or float() then the final formual will read the inputs as string
#and just trint them in a line like  
 
 # like this :-

a = (input(" enter first number:"))
b = (input(" enter second number:"))  
print("the sum of two numbers is:", (a) + (b))
