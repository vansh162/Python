age = int(input("Enter your age: "))

if age<0:
    print("Invalid age.")
elif age<=12:
    print("Your are a CHILD.")
elif age<=19:
    print("Your are a TEENAGER.")
elif age<=59:
    print("Your are an ADULT.")
else:
    print("Your are a SENIOR.")
