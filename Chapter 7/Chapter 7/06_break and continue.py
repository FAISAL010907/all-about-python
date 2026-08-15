# using of break statement in for loop
# eg:
for i in range(100):
    if (i == 19):
        break  # this will exit the loop when we met the output 19
    print(i)


list = [1,2,3,4,5,6,"faisal",7,8,9,10]
for i in list:  #you can write item as well instead of i
    if (i == 7):
        break
    print(i)

    ## print(item, end=" ") # this will print output in horizontal line

# using continue statement in for loop
#eg:

for l in range(100):
    if (l == 1):
        continue  # this will skip the output 1 and continue the loop
    print(l,end = "")