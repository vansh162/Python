import re

print("Welcome to the Pattern Extractor and Command-Line Utility")
while True:
    print("-----------------------------------------------")
    print("Choose an operation:")
    print("1. Extract email addresses from text")
    print("2. Find all phone numbers matching a specific pattern")
    print("3. Count occurrences of a specific word in text")
    print("4. Replace a pattern in the text with another string")
    print("5. Load text from a file")
    print("6. Save results to a new file")
    print("7. Exit")
    print("-----------------------------------------------")

    choice = int(input("Enter your choice: "))
    
    if choice == 7:
        print("Exiting the program. Goodbye!")
        exit()
        
    elif choice == 1:
            text = input("Enter the text to process: ")
            emailPattern = "\w+@+\w+.\w{2,}"
            findEmail = re.findall(emailPattern, text)
            print("Extracting email addresses...")
            if findEmail:
                print("Found email addresses:")
                print(findEmail)
            else:
                print("No emails found.")
            
    elif choice == 2:
        text = input("Enter the text to process: ")
        numberPattern = "\d{3}-\d{3}-\d{4}"
        findNumber = re.findall(numberPattern, text)
        print("Extracting phone numbers...")
        if findNumber:
            print("Found phone numbers:")
            print(findNumber)
        else:
            print("No phone numbers found.")
        
    elif choice == 3:
        text = input("Enter the text to process: ")
        find = input("Enter the word to count: ")
        find2 = re.findall(find, text)
        print(f"Counting occurrences of '{find}'...")
        if find2:
            print(f"The word '{find}' appears {len(find2)} times.")
        else:
            print("No word found.")
        
    elif choice == 4:
        text = input("Enter the text to process: ")
        old = input("Enter the pattern to replace: ")
        new = input("Enter the replacement string: ")
        updated = re.sub(re.escape(old), new, text)
        print("Replacing pattern...")
        if updated:
            print(f"Updated text: {updated}")
        else:
            print("No word found.")
    
    elif choice == 5:
        print("")       
        
    # else:
    #     print("Invalid choice.......")







