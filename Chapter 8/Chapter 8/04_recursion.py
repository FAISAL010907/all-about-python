''' 0! = 1
    1! = 1
    
    5! = 1*2*3*4*5 
    
    n! = n * (n-1)* (n-2).........(n-n)
    
    Factorial (n) = n * factorial(n-1)
    '''
def factorial(n):     # in place of factorial or we casually say fxn we can give any name to the fxn
    if n == 0 or n == 1: # if we dont do this the fxn wont stop if we put input as 0 or 1 and it will become a infinite loop
        return 1
    return n*factorial(n-1)

n = int(input('enter your number : '))
print("the factorial value of your input is",factorial(n))    # in place of factorial or we casually say fxn we can give any name to the fxn


'''def count(n):
    if n == 0:       # Base case
        return     #this will stopr function to begin infinite loop and make funtion stop when the value met 0
    print(n)
    count(n - 1)     # Recursive case

count(5)'''
