# negative slicing 
#using negative index
"""likee F  A  I  S  A  L"""
      #  0  1  2  3  4  5  →→→ +ve index
      # -6,-5,-4,-3,-2,-1  →→→ -ve index

name = "faisal"             
character1 = name[-4:-1]
print(character1)              #these two are same 
character2 = name[2:5]
print(character2)

# if we leave any of two index empty
# like:-
name = "faisal" 
print(name[:3])

name = "faisal"
print(name[2:])