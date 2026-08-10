# QUESTION 6 ))
'''Write a program to calculate the grade of a student from his 
   marks from the following scheme:-
   
       90 - 100 => Ex
       80 - 90 => A
       70 - 80 => B
       60 - 70 => C
       50 - 60 => D
       <50 => F                                       '''

# SOLUTION :-

a = int(input("enter your marks in physics outoff 100    : "))
if(a>100 or a<0):
    print("invalid input")

b = int(input("enter your marks in chemistry outoff 100  : "))
if(b>100 or b<0):
    print("invalid input")

c = int(input("enter your marks in maths outoff 100      : "))
if(c>100 or c<0):
    print("invalid input")

d = int(input("enter your marks in biology outoff 100    : "))
if(d>100 or d<0):
    print("invalid input")

e = int(input("enter your marks in english outoff 100    : "))
if(e>100 or d<0):
    print("invalid input")

aggrigate = 100*(a+b+c+d+e)/500

if(90<aggrigate<100):
    print("Ex")
elif(80<aggrigate<90):
    print("A")
elif(70<aggrigate<80):
    print("B")
elif(60<aggrigate<70):
    print("C")
elif(50<aggrigate<60):
    print("D")
elif(0<aggrigate<50):
    print("F")
else:
    print("invalid result please check your inputs")