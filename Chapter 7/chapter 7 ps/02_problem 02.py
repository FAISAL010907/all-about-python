#  QUSTION 2 ))
'''Write a program to greet all the person names stored in a list 'L' and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]'''

# SOLUTION 1:-

l = ["Harry", "Soham", "Sachin", "Rahul"] 
 
for name in l:
    if(name.startswith("S")):
        print(f"hello {name}")
    else:
        print(f"sorry not invited {name}")