#write a program for converting temperature from fahremheit tp celcius
fahrenheit = float(input("enter temprature of your area in fahrenheit : "))
celcius = (fahrenheit-32)/1.8

print("the temperature in celcius is : ",celcius)

print("============================================")
# since somethims the answer is very long after descimaL  so we can do this

fahrenheit = float(input("enter temprature of your area in fahrenheit : "))
celcius = (fahrenheit-32)/1.8

print(f"the temperature in celcius is : {celcius:.2f}")