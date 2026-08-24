# QUESTION 4 ))
'''4. Write a recursive function to calculate the sum of first n natural numbers.'''

# SOLUTION 1 :-


def sun_n(n):
    if n == 0 :
        return 0 
    return (n*(n+1))//2


n = int(input('enter your number : '))
print("the factorial value of your input is",sum(n))