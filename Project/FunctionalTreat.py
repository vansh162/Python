print("Welcome to the Data Analyzer and Transformer Program")

while True:
    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = int(input("Please enter your choice: "))
    l = [10,20,1,2,3,4,5]

    if choice == 1:
        def inputData():
            arr = list(map(int,input("Enter data for a 1D array (separated by spaces): ").split()))
            return arr
        storedData = inputData()
        print("Data has been stored successfully!")
        print(storedData)

    elif choice == 2:
        print("Data Summary:")
        print(f"- Total elements: {len(l)}")
        print(f"- Minimum value: {min(l)}")
        print(f"- Maximum value: {max(l)}")
        print(f"- Sum of all values: {sum(l)}")
        print(f"- Average value: {(max(l) + min(l))/len(l)}")
    
    elif choice == 3:
       num = int(input("Enter a number to calculate its factorial: "))
       def factorial(n):
           if n == 0 or n == 1:
               return 1
           else:
               return n * factorial(n - 1)
       print(f"Factorial of {num} is: {factorial(num)}")

    elif choice == 4:
        def filter(arr, threshould):
            f = [i for i in arr if i >= threshould]
            return f
        val = int(input("Enter a threshold value to filter out data above this value: "))
        print(f"Filtered Data (values >= {val}): {filter(l,val)}")

    elif choice == 5:
        print("Choose sorting option:")
        print("1. Ascending")
        print("2. Descending ")
        cho = int(input("Enter your choice: "))
        if cho == 1:
            asc = sorted(l)
            print(f"Sorted Data in Ascendong Order: {asc}")
        elif cho == 2:
            des = sorted(l,reverse=True)
            print(f"Sorted Data in Ascendong Order: {des}")
        else:
            print("Invalid choice.")

    elif choice == 6:
      print("Dataset Statistics:")
      print(f"- Minimum value: {min(l)}")
      print(f"- Maximum value: {max(l)}")
      print(f"- Sum of all values: {sum(l)}")
      print(f"- Average value: {(max(l) + min(l))/len(l)}")

    elif choice == 7:
        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.....")        
