import datetime
import time
import math
import random
import string
import uuid
import file_operations

print("===========================")
print("Welcome to Multi-Utility Toolkit")
print("===========================")

while True:
    print("Choose an option:")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    print("===========================")

    choice = int(input("Enter your choice: "))
    
    if choice == 7:
        print("Thank you for using the Multi-Utility Toolkit!")
        print("===========================")
        exit()
    
    elif choice == 1:
        while True:
            print("Datetime and Time Operations:")
            print("1. Display current date and time")
            print("2. Calculate difference between two dates/times")
            print("3. Format date into custom format")
            print("4. Stopwatch")
            print("5. Countdown Timer")
            print("6. Back to Main Menu")
            
            choice2 = int(input("Enter your choice: "))
            
            if choice2 == 6:
                break
            
            elif choice2 == 1:
                print(f"Current Date and Time: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
                print("===========================")
            
            elif choice2 == 2:
                date1 = input("Enter the first date (YYYY-MM-DD): ")
                date2 = input("Enter the second date (YYYY-MM-DD): ")
                date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
                date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
                difference = date2 - date1
                print(f"Difference: {difference}")
                print("===========================")
            
            elif choice2 == 3:
                date_input = input("Enter a date (YYYY-MM-DD): ")
                date_obj = datetime.datetime.strptime(date_input, "%Y-%m-%d")
                formatted_date = date_obj.strftime("%A, %d %B %Y")
                print("Formatted Date:", formatted_date)
                print("===========================")
                
            elif choice2 == 4:
                input("Press Enter to start the stopwatch....")
                startTime = time.time()
                input("Press Enter to stop the stopwatch....")
                endTime = time.time()
                diff = endTime - startTime
                print(f"Time: {diff:.2f} seconds")
                print("===========================")
            
            elif choice2 == 5:
                seconds = int(input("Enter countdown time in seconds: "))
                while seconds:
                    mins, secs = divmod(seconds, 60)
                    print(f"\rTime Remaining: {mins:02}:{secs:02}", end="")
                    time.sleep(1)
                    seconds -= 1
                print("\nTime's up!")
                print("===========================")
            
            else:
                print("Invalid choice...........")
                print("===========================")


    elif choice == 2:
        print("Mathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 5:
            break
        
        elif choice == 1:
            num = int(input("Enter a number: "))
            if num < 0:
                print("Can't find Factorial of Negative number.")
            else:
                ans = math.factorial(num)
                print(f"Factorial: {ans}")
            print("===========================")
        
        elif choice == 2:
            principal = float(input("Enter principal amount: "))
            rate = float(input("Enter rate of interest (in %): "))
            time = float(input("Enter time (in years): "))
            amount = principal * (1 + rate / 100) ** time
            print(f"Compound Interest: {amount:.2f}")
            print("===========================")
        
        elif choice == 3:
            print("\nTrigonometric Functions:")
            angle = float(input("Enter angle in degrees: "))
            radians = math.radians(angle)
            print(f"sin({angle}) = {math.sin(radians):.4f}")
            print(f"cos({angle}) = {math.cos(radians):.4f}")
            print(f"tan({angle}) = {math.tan(radians):.4f}")
            print("===========================")
                
        elif choice == 4:
            print("\nSelect Shape:\n1. Circle\n2. Square\n3. Rectangle")
            choice = input("Enter choice: ")
            if choice == '1':
                radius = float(input("Enter radius: "))
                print(f"Area of Circle: {math.pi * radius ** 2:.2f}")
            elif choice == '2':
                side = float(input("Enter side length: "))
                print(f"Area of Square: {side ** 2:.2f}")
            elif choice == '3':
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                print(f"Area of Rectangle: {length * width:.2f}")
            else:
                print("Invalid choice!")
            print("===========================")
        
        else:
                print("Invalid choice...........")
                print("===========================")
        
            
    elif choice == 3:
        print("Random Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == 5:
            break
        
        elif choice == 1:
            lower = int(input("Enter lower bound: "))
            upper = int(input("Enter upper bound: "))
            print(f"Random Number: {random.randint(lower, upper)}")
            print("===========================")
        
        elif choice == 2:
            length = int(input("Enter the length of the list: "))
            lower = int(input("Enter lower bound: "))
            upper = int(input("Enter upper bound: "))
            
            rList = [random.randint(lower,upper) for _ in range(length)]
            
            print(f"Random List: {rList}")
            print("===========================")
        
        elif choice == 3:
            length = int(input("Enter password length: "))
            char = string.ascii_letters + string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
            password = ''.join(random.choice(char) for _ in range(length))
            print(f"Generated Password: {password}")
            print("===========================")
        
        elif choice == 4:
            length = int(input("Enter length of OTP (4-8): "))
            
            if length < 4 or length > 8:
                print("OTP length must be between 4 and 8 digits.")
                break
            
            otp = ''.join(random.choice(string.digits) for _ in range(length))
            
            print("Generated OTP: {otp}")
            print("===========================")
            
        else:
                print("Invalid choice...........")
                print("===========================")
    
    elif choice == 4:
        while True:
            print("1. Generate UUID1 (based on timestamp and MAC address)")
            print("2. Generate UUID4 (random UUID)")
            print("3. Back to Main Menu")
            
            choice = input("Enter your choice: ")
            
            if choice == 3:
                break
            
            elif choice == 1:
                print(f"Generated UUID1: {uuid.uuid1()}")
                print("===========================")
                
            elif choice == 2:
                print(f"Generated UUID4: {uuid.uuid4()}")
                print("===========================")
                
            else:
                print("Invalid choice..........")
                print("===========================")
    
    elif choice == 5:
        while True:
            print("File Operations:")
            print("1. Create a new file")
            print("2. Write to a file")
            print("3. Read from a file")
            print("4. Append to a file")
            print("5. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                file_name = input("Enter file name: ")
                file_operations.create_file(file_name)
                print("===========================")
                
            elif choice == 2:
                file_name = input("Enter file name: ")
                data = input("Enter data to write: ")
                file_operations.write_to_file(file_name, data)
                print("===========================")
                
            elif choice == 3:
                file_name = input("Enter file name: ")
                file_operations.read_from_file(file_name)
                print("===========================")
                
            elif choice == 4:
                file_name = input("Enter file name: ")
                data = input("Enter data to append: ")
                file_operations.append_to_file(file_name, data)
                print("===========================")
                
            elif choice == 5:
                break
            
            else:
                print("Invalid choice............")
                print("===========================")

    
    elif choice == 6:
        print("Explore Module Attributes:")
        module = input("Enter module name to explore: ")
        print(f"Available Attributes in {module} module: {dir(module)}")
        print("===========================")

    else:
        print("Invalid choice...........")
        print("===========================")



