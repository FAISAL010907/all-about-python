# QOUESTION 2)):-
#  Write a program to accept marks of 6 students and display them in a appended manner

# SOLUTION 1 )):-

marks = []

f1 = input("enter your mark : ")
marks.append(f1)
f2 = input("enter your mark : ")
marks.append(f2)
f3 = input("enter your mark : ")
marks.append(f3)
f4 = input("enter your mark : ")
marks.append(f4)
f5 = input("enter your mark : ")
marks.append(f5)
f6 = input("enter your mark : ")
marks.append(f6)

marks.sort()


print(F"the list of your mark is{marks}")
# this will sort the data in alphabetical order

#  SOLUTION 2 )):-

#if we want to sort the data in accending order we will do 
#we will change the data type because of input fxn this was happened so we will add int(fxn)

marks = []

f1 = int(input("enter your fruit : "))
marks.append(f1)
f2 = int(input("enter your fruit : "))
marks.append(f2)
f3 = int(input("enter your fruit : "))
marks.append(f3)
f4 = int(input("enter your fruit : "))
marks.append(f4)
f5 = int(input("enter your fruit : "))
marks.append(f5)
f6 = int(input("enter your fruit : "))
marks.append(f6)
f7 = int(input("enter your fruit : "))
marks.append(f7)

marks.sort()

print(F"the list of your fruit is{marks}")
# now this will arrange the data in accending order


