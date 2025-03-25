import datetime
import os

print("Welcome to Personal Journal Manager!")

open("Journal.txt","x")
file_path = "Journal.txt"

def is_empty():
    return os.stat(file_path).st_size == 0
                    

while True:
    print("Please select an option:")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")
    
    choice = int(input("User Input: "))
    
    if choice == 5:
        print("Thank you for using Personal Journal Manager. Goodbye!")
        os.remove("Journal.txt")
        exit()
        
    elif choice == 1:
        data = input("Enter your journal entry: ")
        dat = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        with open("Journal.txt", "a") as file:
            file.write(f"{dat}\n{data}\n\n")
        print("Entry added successfully!")
        
    
    elif choice == 2:
        if is_empty():
            print("No journal entries found. Start by adding a new entry!")
        else:
            print("\nYour Journal Entries:")
            print("--------------------------------")
            with open(file_path, "r") as file:
                print(file.read())     
        
    elif choice == 3:
        search = input("Enter a keyword or date to search: ").strip().lower()

        if is_empty():
            print("No journal entries to search.")
        else:
            with open(file_path, "r") as file:
                entries = file.readlines()

            found = False
            print("\nMatching Entries:")
            print("----------------------------")

            for i in range(len(entries)):
                if search in entries[i].lower():
                    found = True
                    print(entries[i].strip()) 
                    if i + 1 < len(entries):
                        print(entries[i + 1].strip())  
                        print()

            if not found:
                print(f"No entries were found for the keyword: {search}.")
            
    elif choice == 4:
        confirm = input("Are you sure you want to delete all entries? (yes/no): ").strip().lower()
        
        if confirm == "yes":
            open(file_path, "w").close() 
            print("All journal entries deleted successfully.")
        else:
            print("Operation canceled.")

    else:
        print("Invalid option. Please select a valid option from the menu.")