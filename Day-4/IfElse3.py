num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2st number: "))
num3 = int(input("Enter 3st number: "))

if num1>num2 and num1>num3:
    print("Number 1 is the LARGEST NUMBER.")
elif num2>num1 and num2>num3:
    print("Number 2 is the LARGEST NUMBER.")
elif num3>num1 and num3>num2:
    print("Number 3 is the LARGEST NUMBER.")

if num1==num2:
    print("Number 1 and 2 have the same value.")
elif num1==num3:
    print("Number 1 and 3 have the same value.")
elif num2==num1:
    print("Number 2 and 1 have the same value.")
elif num2==num3:
    print("Number 2 and 3 have the same value.")
elif num3==num1:
    print("Number 3 and 1 have the same value.")
elif num3==num2:
    print("Number 3 and 2 have the same value.")