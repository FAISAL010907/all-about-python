# make a calculator for a child that ask from how much money he left in different currency and tell him how much he left in inr

a = float(input("amount left in USD   : "))
b = float(input("amount left in PESOS : "))
c = float(input("amount left in REAIS : "))
d = float(input("amount left in SOLES : "))

USD = a*95.40
PESOS = b*5.54
REAIS = c*18.50
SOLES = d*28.02

total = USD+PESOS+REAIS+SOLES

print(f"the total amount you left in INR is : {total:.2f}")