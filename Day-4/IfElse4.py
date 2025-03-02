num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2st number: "))
ope = input("Enter the OPERATION you wanna perform(+,-,*,/): ")
if ope == "+":
    print(f"{num1} {ope} {num2} = {num1+num2}")
elif ope == "-":
    print(f"{num1} {ope} {num2} = {num1-num2}")
elif ope == "*":
    print(f"{num1} {ope} {num2} = {num1*num2}")
elif ope == "/":
    print(f"{num1} {ope} {num2} = {num1/num2}")
else:
    print("Invalid Choice")