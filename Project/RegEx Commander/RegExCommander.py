import re
import sys
import os

def extract_pattern(text, operation_code):
    if operation_code == 1:
            emailPattern = r"\w+@\w+\.\w{2,}"
            findEmail = re.findall(emailPattern, text)
            print("Extracting email addresses...")
            if findEmail:
                print("Found email addresses:")
                for idx, email in enumerate(findEmail, start=1):
                    print(f"{idx}. {email}")
            else:
                print("No emails found.")
    
    elif operation_code == 2:
        numberPattern = r"\d{3}-\d{3}-\d{4}"
        findNumber = re.findall(numberPattern, text)
        print("Extracting phone numbers...")
        if findNumber:
            print("Found phone numbers:")
            for idx, number in enumerate(findNumber, start=1):
                print(f"{idx}. {number}")
        else:
            print("No phone numbers found.")
            
    elif operation_code == 3:
        find = input("Enter the word to count: ")
        find2 = re.findall(find, text)
        print(f"Counting occurrences of '{find}'...")
        if find2:
            print(f"The word '{find}' appears {len(find2)} times.")
        else:
            print("No word found.")
            
    elif operation_code == 4:
        old = input("Enter the pattern to replace: ")
        new = input("Enter the replacement string: ")
        updated = re.sub(re.escape(old), new, text)
        print("Replacing pattern...")
        if updated:
            print(f"Updated text: {updated}")
        else:
            print("No word found.")
            
    else:
        raise ValueError("Invalid operation code.")

def read_file(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File not found: {filename}")
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def write_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)

def command_line_mode():
    if len(sys.argv) != 3:
        print("Usage: python pattern_extractor.py <filename> <operation_code>")
        sys.exit(1)

    filename = sys.argv[1]
    operation = int(sys.argv[2])

    try:
        text = read_file(filename)
        print(f"Operation: Extract email addresses from file: {filename}")
        extract_pattern(text, operation)
        
    except Exception as e:
        print(f"Error: {e}")
        
if len(sys.argv) > 1:
        command_line_mode()
else:
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
                emailPattern = r"\w+@\w+\.\w{2,}"
                findEmail = re.findall(emailPattern, text)
                print("Extracting email addresses...")
                if findEmail:
                    print("Found email addresses:")
                    for idx, email in enumerate(findEmail, start=1):
                        print(f"{idx}. {email}")
                else:
                    print("No emails found.")
                
        elif choice == 2:
            text = input("Enter the text to process: ")
            numberPattern = r"\d{3}-\d{3}-\d{4}"
            findNumber = re.findall(numberPattern, text)
            print("Extracting phone numbers...")
            if findNumber:
                print("Found phone numbers:")
                for idx, number in enumerate(findNumber, start=1):
                    print(f"{idx}. {number}")
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
            
        else:
            print("Invalid choice.......")