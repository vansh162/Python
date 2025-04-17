import os
import subprocess
from functools import reduce

def main_menu():
    while True:
        print("\nExecuter - Command Line Utility and File System Manager")
        print("=" * 25)
        print("\nChoose an option:")
        print("1. File System Operations")
        print("2. Execute Terminal Commands")
        print("3. File Analysis with Higher-Order Functions")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            file_system_operations()
        elif choice == '2':
            execute_terminal_commands()
        elif choice == '3':
            file_analysis()
        elif choice == '4':
            confirm = input("Do you really want to exit? (yes/no): ").strip().lower()
            if confirm == "yes":
                print("Thank you for using the Executer - Command Line Utility and File System Manager. Goodbye!")
                break
        else:
            print("Invalid choice. Please enter a valid option.")

def file_system_operations():
    while True:
        print("\nFile System Operations:")
        print("1. Display current directory")
        print("2. List files and directories")
        print("3. Change directory")
        print("4. Create a directory")
        print("5. Remove a directory")
        print("6. Create a file")
        print("7. Delete a file")
        print("8. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Current directory:\n", os.getcwd())
        elif choice == '2':
            print("Files and directories:")
            for item in os.listdir():
                print("-", item)
        elif choice == '3':
            path = input("Enter directory path: ")
            try:
                os.chdir(path)
                print("Directory changed to:", os.getcwd())
            except Exception as e:
                print("Error:", e)
        elif choice == '4':
            name = input("Enter the name of the new directory: ")
            try:
                os.mkdir(name)
                print(f"Directory '{name}' created successfully.")
            except Exception as e:
                print("Error:", e)
        elif choice == '5':
            name = input("Enter the name of the directory to remove: ")
            try:
                os.rmdir(name)
                print(f"Directory '{name}' removed successfully.")
            except Exception as e:
                print("Error:", e)
        elif choice == '6':
            name = input("Enter the name of the file to create: ")
            try:
                with open(name, 'w') as f:
                    pass
                print(f"File '{name}' created successfully.")
            except Exception as e:
                print("Error:", e)
        elif choice == '7':
            name = input("Enter the name of the file to delete: ")
            try:
                os.remove(name)
                print(f"File '{name}' deleted successfully.")
            except Exception as e:
                print("Error:", e)
        elif choice == '8':
            break
        else:
            print("Invalid choice.")

def execute_terminal_commands():
    while True:
        print("\nExecute Terminal Commands:")
        print("1. Run a predefined command (e.g., pwd, ls)")
        print("2. Run a custom command")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Choose a command:")
            print("1. pwd")
            print("2. ls")
            print("3. df -h")
            sub_choice = input("Enter your choice: ")
            command = ""
            if sub_choice == '1':
                command = "pwd"
            elif sub_choice == '2':
                command = "ls"
            elif sub_choice == '3':
                command = "df -h"
            else:
                print("Invalid command option.")
                continue
            print(f"Executing '{command}'...")
            subprocess.call(command, shell=True)
        elif choice == '2':
            cmd = input("Enter the custom command to execute: ")
            print(f"Executing '{cmd}'...")
            result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = result.communicate()
            print(out.decode())
            if err:
                print("Error:\n", err.decode())
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

def file_analysis():
    while True:
        print("\nFile Analysis with Higher-Order Functions:")
        print("1. Sort files by name")
        print("2. Filter files by extension")
        print("3. Calculate total size of files in a directory")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            files = sorted([f for f in os.listdir() if os.path.isfile(f)])
            print("Files sorted by name:")
            for f in files:
                print("-", f)
        elif choice == '2':
            ext = input("Enter file extension to filter by (e.g., .txt): ")
            filtered = list(filter(lambda f: f.endswith(ext), os.listdir()))
            print("Filtered files:")
            for f in filtered:
                print("-", f)
        elif choice == '3':
            print("Calculating total size of files in the current directory...")
            files = [f for f in os.listdir() if os.path.isfile(f)]
            total_size = reduce(lambda acc, f: acc + os.path.getsize(f), files, 0)
            print("Total size:", total_size, "bytes")
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
