#ARITHEMTIC OPERATORS
from pickle import TRUE


a = 10
b = 5

A = a + b  # addition
print("addition = ",A) 

S= a - b  # subtraction
print("subtraction = ",S)

M = a * b  # multiplication
print("multiplication = ",M)

D= a / b  # division
print("division = ",D)

FD= a // b  # floor division
print("floor division = ",  FD)

Ex= a ** b  # exponentiation
print("exponentiation = ", Ex)

Mo= a % b  # modulus
print("modulus = ", Mo)

print("=================================")

#ASSIGNMENT OPERATORS
a = 10-5 #means assign 10-5 to a
print(a)

a = 10
a += 5 # mean increase/increment the value of a by 5 or add 5 in the value of a
print(a)

a = 10
a -= 5 # mean decrease/decrement the value of a by 5 or subtract 5 from the value of a
print(a)

print("=================================")
#COMPARISON OPERATORS
#the resulting valur of comparison operators is always boolean value either True or False

d= 5>7 # "greater than"
print(d) #answer is always true or false depend on the question 

d= 5<7 # "less than"
print(d) #answer is always true or false depend on the question or the equation given

d= 5>=7 # "greater than or equal to"
print(d) #answer is always true or false depend on the question or the equation given

d= 5<=7 # "less than or equal to"
print(d) #answer is always true or false depend on the question or the equation given

d= 5==7 # "equal to"
print(d) #answer is always true or false depend on the question or the equation given

d= 5!=7 # "not equal to"
print(d)  #answer is always true or false depend on the question or the equation given

print("=================================")

#LOGICAL OPERATORS
# it works on truth table and give answer in boolean value 

#TRUTH TABLE FOR "OR"
print("TRUE OR FALSE is", True or False) # answer is always true if one true is present in the equation
print("TRUE OR TRUE is", True or True) 
print("FALSE OR TRUE is", False or True) 
print("FALSE OR FALSE is", False or False) # answer is always false if both are false in the equation

print("=================================")

#TRUTH TABLE FOR "AND"
print("TRUE AND FALSE is", True and False) # answer is always false if one false is present in the equation
print("TRUE AND TRUE is", True and True) # answer is always true if both are true in the equation
print("FALSE AND TRUE is", False and True)
print("FALSE AND FALSE is", False and False) 

print("=================================")

#TRUTH TABLE FOR "NOT"
print("NOT TRUE is", not True) 
print("NOT FALSE is", not False) # this will always give the opposite value 
                                 #and always the boolean value either True or False     