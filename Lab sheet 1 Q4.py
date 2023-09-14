num = eval(input("Enter a number: "))

if num>-100 and num<100:
    if num>0:
        print("It is a positive number")
    if num<0:
        print("It is a negative number")
    if num==0:
        print("It is zero")
else:
    print("Error")
