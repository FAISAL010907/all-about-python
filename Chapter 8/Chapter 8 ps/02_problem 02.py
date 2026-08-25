# QUESTION 2 ))
'''Write a python program using function to convert Celsius to Fahrenheit'''

# SOLUTION 1:-

def celsius():
    c = float(input("enter the temperaure in Celcius : "))
    fahrenheit = (c*(9/5)+32)
    kelvin = (c + 273.15)

    print(f"'{c}°C' celsius is '{fahrenheit}°F' Fahrenheit")
    print(f"'{c}°C' celsius is '{kelvin}°K' Kelvin")

def kelvin():
    k = float(input("enter the temperature in Kelvin : "))
    celsius = (k - 273.15)
    fahrenheit = (k-273.15)*(9/5)+32

    print(f"'{k}°K' kelvin is '{celsius:.2f}°C' celsius")
    print(f"'{k}°K' kelvin is '{fahrenheit:.2f}°F' fahrenheit")

def fahrenheit():
    f = float(input("enter the temperature in Fahrenheit : "))
    celsius = (f-32)*(5/9)
    kelvin = (f-32)*(5/9)+273.15

    print(f"'{f}°F' fahrenheit is '{celsius:.2f}°C' Celsius")
    print(f"'{f}°F' fahrenheit is '{kelvin:.2f}°K' Kelvin")

celsius()
kelvin()
fahrenheit()

''' alternate solution

def f_to_c(f):
    return 5*(f-32)/9 or c = 5*(f-32)/9
    
f = int(input("enter temp in f))
print(f_to_c(f))'''