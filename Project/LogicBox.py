print("Welcome to the Pattern Generator and Number Analyzer!")
print()


while True:
    print("Select an option:")
    print("1. Generate a Right-angled Triangle Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice > 3 or choice <= 0:
        print("Invalid choice. Exiting.....")
        break
    print()
    if choice == 1:
        row = int(input("Enter the number of rows for the pattern: "))
        print("Pattern:")
        for i in range(1,row+1):
            print("*"*i)
    
    elif choice == 2:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        total = 0
        for i in range(start,end+1): 
            if i%2==0:
                print("Number",i,"is Even")
            else:
                print("Number",i,"is Odd")
            total = total + i
        print("Sum of all number from",start,"to",end,"is: ",total)

    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break

    
