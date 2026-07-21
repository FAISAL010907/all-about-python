# negative slicing 
#using negative index
"""likee F  A  I  S  A  L"""
      #  0  1  2  3  4  5  →→→ +ve index
      # -6,-5,-4,-3,-2,-1  →→→ -ve index

name = "faisal"             
character1 = name[-4:-1]       #----this is nergative slicing
print(character1)              #these two are same 
character2 = name[2:5]
print(character2)

# if we leave any of two index empty
# like:-
name = "faisal" 
print(name[:3]) #here empty means 0
                # so this mean from 0 to 3
                # means [:3] same as [0:3]
name = "faisal"
print(name[2:]) #here empty means length or in leymen lang. last index
                # so this mean from 2 to last   
                #means [2:] is same as[2:5]
                