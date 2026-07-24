# TUPLE METHODS

friend = ("faisal","banana",65,"banana",56.234,True,"sufi","guava")
# if we dont mention class again it doesnt make any difference because as string tuple also create new solution every time wihtout changing in parent tuple

# 1)) TUPLE.COUNT(X)
#  it will count and return the number of times the element "x" occure in the tuple
 
c = friend.count("faisal")
print(c) # data type dont matter

# 2)) TUPLE.INDEX(X)
# it will return the index of first occurance of x in the tuple

i = friend.index("faisal")
print(i) # as name it will return the index when the input is first occure

#we can even specify where to search friend
print(friend.index("banana",2))

