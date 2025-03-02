print("Welcome to the Student Data Organizer!")
print()

student = {}

while True:
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Student")
    print("3. Update Student Infomation")
    print("4. Delete Student")
    print("5. Display Student Offered")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Enter student details:")
        sID = int(input("Student ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        sub = input("Subject (comma-separated): ")

        student[len(student)] = {"Student ID" : {sID},"Name" : {name}, "Age" : {age}, "Grade" : {grade}, "Date of Birth" : {dob} , "Subject" : {sub}}
        print(len(student))
    
    if choice == 2:
        if len(student) == 0:
            print("Can't print NO STUDENT ADDED.")
        else:
            for x in student.keys():
                for keys in student[x]:
                    print(f"{keys}: {student[x][keys]}")

    if choice == 3:
        if len(student) == 0:
            print("Can't print NO STUDENT ADDED.")
        else:
            update = int(input("Enter Student Student ID to UPDATE: "))
            for x in student.keys():
                if student[x]["Student ID"] == update:
                    print(student[x])
                    print("Enter student details:")
                    sID = int(input("Student ID: "))
                    name = input("Name: ")
                    age = int(input("Age: "))
                    grade = input("Grade: ")
                    dob = input("Date of Birth (YYYY-MM-DD): ")
                    sub = input("Subject (comma-separated): ")
                    student[x] = {"Student ID" : {sID},"Name" : {name}, "Age" : {age}, "Grade" : {grade}, "Date of Birth" : {dob} , "Subject" : {sub}}
                    print(student[x])

    if choice == 4:
        if len(student) == 0:
            print("Can't print NO STUDENT ADDED.")
        else:
            delete = int(input("Enter Student ID to delete a student: "))
            found = 0
            for x in student.keys():
                if student[x]["Student ID"] == delete:
                    found = x
            del student[found]
            print(f"Deleted Student.")

    if choice == 5:
        if len(student) == 0:
            print("Can't print NO STUDENT ADDED.")
        else:
            print("Subject Offered are: ")
            for x in student.keys():
                allSub = set(student[x]["Subject"])
            print(allSub)
            
    if choice >= 6 or choice <= 0:
        break