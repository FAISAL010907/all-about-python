# LIST METHOD 

# this will give us list as it is

friend = ["faisal","banana",65,56.234,True,"sufi","guava"]
print(friend)

# 1)) LIST.SORT()

# to rearrange the list in accending order we use 
l1 = [2,5,3,1,15,43,24,18,0,1]
l1.sort()

print(l1) # this will give us rearranged list in accending order
###---------------------------------------------------------------###

# 2)) LIST.REVERSE()
# this will create a mirror image from the of list or can say it will basically reverse the order
l1 = [2,5,3,1,15,43,24]
l1.reverse()

print(l1)
###---------------------------------------------------------------###

# 3)) LIST.APPEND(X)
# it will basically add the X or the vale/elemnt you enter in the closed bracket at the end of list
friend = ["faisal","banana",65,56.234,True,"sufi","guava"]
friend.append("kamal")
print(friend) 


#we can even change the data type
friend = ["faisal","banana",65,56.234,True,"sufi","guava"]
friend.append(577776)  # it would be fine even we would not defined the list
print(friend)

###---------------------------------------------------------------###
# 4 )) LIST.INSERT(X,Y)
# this will basically add Y at the X index(position int the list)
friend = ["faisal","banana",65,56.234,True,"sufi","guava"]
friend.insert(3,'best') # here as well even if we will not define the list because we did at the start , it would be fine
print(friend)
###---------------------------------------------------------------###

#5 )) LIST.POP(X)
# this will basically delet the element at that index you put in the closed bracket and it will return its value
friend = ["faisal","banana",65,56.234,True,"sufi","guava"]
friend.pop(0)

print(friend)\
###---------------------------------------------------------------###

# 6)) LIST.REMOVE(x)
# it will basically remove the element you put in the bracket
friend = ["faisal","banana",65,56.234,True,"sufi","guava"]
friend.remove("sufi")
print(friend) # no need to define list if you want the previous change to stay in list if not then you need to 

# we can do it this way also
friend = [54,65,56.234,]
value = friend.pop(2)
print(value)
