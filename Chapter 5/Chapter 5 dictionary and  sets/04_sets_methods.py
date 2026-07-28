#  SETS METHODS 
s = {1,22,32,54,5465,7,345,34,234,5,5,5,5,5,5}

# 1)) s.add("kamal")
# this function adds the input element in the ()

s.add("kamal")
print(s) # ans since it is unordered it can be print anywherwe in the set
# output = {32, 1, 34, 5, 'kamal', 7, 345, 234, 22, 54, 5465}
'''============================================================'''

# 2)) len(s)
# this will tell the length of the set

print(len(s))
# output = 11
'''============================================================'''

# 3)) s.remove("kamal")
# this will remove the element and retun the value

s.remove(1)
print(s)
# output = {32, 34, 5, 7, 345, 234, 22, 54, 'kamal', 5465}

s.remove("kamal")
print(s)
# output = {32, 34, 5, 7, 345, 234, 22, 54, 5465} , since the set is mutable
'''============================================================'''

# 4 )) s.pop()
#--- this removes one random arbitary element from the set and return that removed elements
#--- the specific element is not guaranteed to be any oerticular number

print(s.pop())
# output = 32 
'''============================================================'''

# 5)) s.clear()
# this fxn empties the set and always return the NONE output
print(s.clear())
# output = NONE , since it clear out the set
'''============================================================'''

# 6)) s.union
# this return a new set with all item from both the set
print(s.union({12,333,786}))
#output = {786,12,33}, since the set is immutable and the previous se emptied the set and make it a null set 

# if we want to get the union of previous set and new set we need to mention or define it agan
# like
s = {1,22,32,54,5465,7,"kamal",345,34,234,5,5,5,5,5,5}
print(s.union({"786","12","333"}))
# now the output is {32, 1, 34, 5, '333', 7, 345, '786', 234, 22, 54, '12', 5465}
'''============================================================'''

# 7 )) s.intersection({8,111})
# -- return the set which contain the element that are common in both

print(s.intersection({8,111}))
# will return the empty set, no element is common

print(s.intersection({32,1,"kamal",8,111,222,222,333}))
#output = {32, 1, 'kamal'}
'''============================================================'''

# 8 )) a.symmetric_difference(b)
# this will return the set that contain all the element of both set except the common elements

a = {1,2,3,4,5}
b = {4,5,6,7,8,9}
print(a^b)
# output = {1,2,3,6,7,8,9}
# we can also use :-
print(a.symmetric_difference(b))
# output will be same {1,2,3,6,7,8,9}