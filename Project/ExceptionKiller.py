print("Welcome to the Robust Banking System!")
print()
desopit = 0
balance = 0
withdraw = 0
class NegativeNumber(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

def depositOne():
        if deposit<0:
            raise NegativeNumber()
        else:
            balance = balance + deposit
            print("Account created successfully!")

def depositTwo():
        if deposit<0:
            raise NegativeNumber()
        else:
            balance = balance + deposit
            print(f"Deposit successful! Your new balance is: {balance}")

def withdrawFun():
    if withdraw>balance:
        raise InsufficientFundsError()
    else:
        balance = balance - withdraw
        print(f"Withdrawal successfull Your new balance is: {balance}")
        
while True:
    print("Please select an option:")
    print("1. Create Account")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. Check Balance")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Thank you for using the Robust Banking System! Goodbye!")
        exit()
        
    elif choice == 1:
        name = input("Enter your name: ")
        deposit = int(input("Enter initial deposit amount: "))
        try:
            depositOne()
        except:
            print("Error: Deposit amount must be positive.")

    elif choice == 2:
        deposit = int(input("Enter deposit amount: "))
        try:
            depositTwo()
        except:
            print("Error: Deposit amount must be positive.")
        

    elif choice == 3:
        withdraw = int(input("Enter withdrawal amount: "))
        try:
            withdrawFun()
        except:
             print(f"Insufficient funds. Your current balance is: {balance}")
            
    elif choice == 4:
        print(f"Your current balance is: {balance}")

    else:
        print("Invalid choice........")




