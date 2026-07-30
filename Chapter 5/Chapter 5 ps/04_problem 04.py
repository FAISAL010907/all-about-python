# QUESTION 4 )
"""What will be the length of following set s:
   s = set()
   s.add(20)
   s.add(20.0)
   s.add('20') # length of s after these operations?"""

# SOLUTION :-

s = set()
s.add(20)
s.add(20.0)
s.add('20') 
print(len(s))

# OUTPUT = 2 , since python consider 20 and 20.0 as same 

s = set()
s.add(20)
s.add(20.5)
s.add('20') 
print(len(s))

# output = 3 , since we replsce 20.0 with 20.5 not the length is 3 