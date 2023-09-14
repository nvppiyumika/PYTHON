num1 = eval(input("Enter angle 1: "))
num2 = eval(input("Enter angle 2: "))
num3 = eval(input("Enter angle 3: "))

total = num1+num2+num3

if total==180 and num1>0 and num2>0 and num3>0:
    print("It is a Triangle")
else:
    print("It is not a Triangle")
