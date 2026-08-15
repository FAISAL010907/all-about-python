# iteration in for loop 

list = [1,2,3,4,5,6,"faisal",7,8,9,10]
for i in list:
    print(i)
    ''' output will return the element from the list''' 
print(type(list))

print('====================================')

    # this same will happen for tuple just make a tuple and run the code
tuple = (6,34,2,3,5,6,"faisal")
for i in tuple:
    print(i)
print(type(tuple))
    # print(type(i)) this will print the type of entire tuple for individual element

# for string it will print the individual alphabets od words
S = "faisal is the best"
for i in S.upper():
    print(i)
    #the upper() will bascially convert the string into upper case and then print the individual alphabets of the string and the same for lowert() in same manner
    