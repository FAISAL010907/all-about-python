# **TUPLES**

#tuples are immutable data types in python

a = () # this si empty tuple
a = (1,) # this is tuple with single element and it is important to add a comma "," this is neccerary 
a = (1,2,3,4,5,6,7,8,9,10) # this is the tuple with more than one element or we can say more than one element

t3 = 10,20,30,40

print(type(t3)) # this is a tuple without parenthesis
print(type(a))

# AND ALSO

friend = ("faisal","banana",65,56.234,True,"sufi","guava")

print(a)
print(type(a))
###---------------------------------------------------------------###

# SLICING 
print(friend[1:4])
###---------------------------------------------------------------###

# CONCATENATION (add)
a = (1, 2)
b = (3, 4)

print(a + b)
###---------------------------------------------------------------###

# REPEATITION
print(friend*5)
# simplear

b = (31,)
print(b*5)
###---------------------------------------------------------------###

# MEMBERSHIP
# TO CHECK WHEATHER THE ELEMENT PRESENT IN THE TUPLE OR NOT WE CAN DO
friend = ("faisal","banana",65,56.234,True,"sufi","guava")

print("faisal" in friend)
print(455 in friend)
print("sufi"in friend)
print("grape" in friend)
print(False in friend)
###---------------------------------------------------------------###

# LENGTH
t = (10,20,30)
print(len(t))
#output = 3 will give the number of element in the set
###---------------------------------------------------------------###

# ITERATION
# repeat a process or action
colours = ("red","blue", "green")
for colour in colours:
    print(colour)

'''output = will give the items in line like
        red 
        blue    
        green'''
###---------------------------------------------------------------###

# PACKING AND UNPACKING
# 1) PACKING :-

person = ("faisal",25,"usa")

# 2) UNPACKING :-

name,age,country = person
print(name)
print(age)
print(country)

#OUTPUT:-
#faisal
#25
#usa
###---------------------------------------------------------------###

# BUILT-IN FUNCTION THAT WORK IN TUPLE
number = (4,3,5,6,7)

print(len(number))
print(max(number))
print(min(number))
print(sum(number))

#OUTPUT:-
'''5
   7
   3
   25'''
###---------------------------------------------------------------###

# List to Tuple
numbers = [1, 2, 3]

numbers = tuple(numbers)

print(numbers)
print(type(numbers))
###---------------------------------------------------------------###

#Tuple to List
numbers = (10, 20, 30)

numbers = list(numbers)

print(numbers)
print(type(numbers))
###---------------------------------------------------------------###

#How can you change the data type of one element?
#Method 1: Convert the tuple to a list (most common)

t = (10, "25", "True")

# Convert to list
temp = list(t)

# Change the second element from string to integer
temp[2] = bool(temp[2])

# Convert back to tuple
t = tuple(temp)

print(t)
print(type(t[2]))

#Output:

#(10, 25, True)
#<class 'int'>
###---------------------------------------------------------------###

#Method 2: Create a new tuple
#Since tuples are immutable, you can create a new tuple with the changed value.
t = (10, "25", False)

new_t = (t[0], int(t[1]), int(t[2]))

print(new_t)


#Output:

#(10, 25, 0)
###---------------------------------------------------------------###

# how to change the perticular element like from bool to str like false to "sufi"

# Method 1: Convert to a list
t = (10, False, "Python")

lst = list(t)      # Convert tuple to list
lst[1] = "Sufi"    # Replace False with "Sufi"
t = tuple(lst)     # Convert back to tuple

print(t)

# Output:

#(10, 'Sufi', 'Python')
###---------------------------------------------------------------###

# Method 2: Create a new tuple
t = (10, False, "Python")

t = (t[0], "Sufi", t[2])

print(t)

# Output:

#(10, 'Sufi', 'Python')

###---------------------------------------------------------------###
