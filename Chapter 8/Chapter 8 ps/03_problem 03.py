#  QUESTION 3 ))
'''How do you prevent a python print() function to print a new line at the end.'''

# SOLUTION :-
'''by usign (end = "") '''

print("Hello")          # default: end="\n"
print("Hello", end=" ")  # no new line
print("Hello", end=" maka ladle meow ghop ghop ghop") # space instead of new line

print("a")
print("b")
print("c", end="") # no new line
print("d") # will be printed in the same line as c or you can do print("d", end="")
