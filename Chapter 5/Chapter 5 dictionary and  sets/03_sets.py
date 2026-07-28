# SETS IN PYTHON

# 1) empty set  
 
e = () # this is a empty set ,dont use {} as it will ceate empty dictionary

# 2) set

s = {1,2,32,4,35,44,43,43,43,55,"faisal"}
print(s)
print(type(s))
print(s, type(s))
# output = {32, 1, 2, 35, 4, 43, 44, 55} as repeatetion is not allowed in sets

# we can add the elements in the set with s.add
s.add("kamal")
print(s)