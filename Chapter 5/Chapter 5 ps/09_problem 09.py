# QUESTION 9 ))
"""Can you change the values inside a list which is contained in set S ?
                      s = {8, 7, 12, "Faisal", [1,2]}"""
      
# SOLUTION :-

# No, this code itself is invalid. Python will raise an error before you even get the chance to change the list.

''' first thing is a set can only contain hashable(immutable) objct
                    but here is a list [1,2] which is mutable ,so it is unhashbale , which also mean set never created '''
# The answer is No, because a list cannot be stored inside a set but "tuple can" in the first place.

''' second thing is, even if we could do it we cant change the value by indexing '''
# which mean set rely on hash value to store and find elements . if an element could change after being added , the sets internal orginazation would become incorrect

s = {8, 7, 12, "Faisal", [1,2]}
print(s) # TypeError: unhashable type: 'list'
