import datetime
import os

print("Welcome to Personal Journal Manager!")

open("Journal.txt","x")

allData = []

class EmptyError(Exception):
    pass

def isEmpty(file_path):
    if os.path.getsize(file_path) == 0:
        raise EmptyError()
    else:
        with open("Journal.txt","r") as file:
                print("Your Journal Entries: ")
                print("--------------------------------")
                # for i in allData:
                    

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
        dat = datetime.datetime.now()
        allData.append({data,dat.strftime("%Y-%m-%d %H:%M:%S")})
        with open("Journal.txt","w") as file:
            file.write(data)
        print("Entry added successfully!")
        
    
    elif choice == 2:
        # try:
        #     isEmpty()
        # except:
        #     print("No journal entries found. Start by adding a new entry!")
        print(allData["1"])
        
        
    elif choice == 3:
        search = input("Enter a keyword or date to search: ")
            
    elif choice == 4:
        deleteAll = input("Are you sure you want to delete all entries? (yes/no): ")
        if deleteAll == "yes":
            os.remove("Journal.txt")
        elif deleteAll == "no":
            break
        else:
            print("Invalid choice.....")
            
    else:
        print("Invalid option. Please select a valid option from the menu.")