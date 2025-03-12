print("--- Python 00P Project: Employee Management System ---")
print()

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"Person created with name: {self.name} and age: {self.age}.")

    def showData(self):
        print("Person Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee(Person):
    def __init__(self,name,age,eid,salary):
        self.name = name
        self.age = age
        self.eid = eid
        self.salary = salary
        self.post = "Employee"
        print(f"Employee created with name: {self.name}, age: {self.age}, ID: {self.eid}, and salary: ${self.salary}")

    def showData(self):
        print("Employee Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.eid}")
        print(f"Salary: {self.salary}")

class Manager(Person):
    def __init__(self,name,age,eid,salary,dep):
        self.name = name
        self.age = age
        self.eid = eid
        self.salary = salary
        self.dep = dep
        self.post = "Manager"
        print(f"Manager created with name: {self.name}, age: {self.age}, ID: {self.eid}, salary: ${self.salary} and department: {self.dep}")

    def showData(self):
        print("Manager Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.eid}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.dep}")

def copmareSalary(e1,e2):
    print("Comparing salaries:")
    if e1.salary > e2.salary:
        return f"{e2.post} {e2.name} {e2.eid} has a lower salary than {e1.post} {e1.name} {e1.eid}."
    elif e1.salary < e2.salary:
        return f"{e1.post} {e1.name} {e1.eid} has a lower salary than {e2.post} {e2.name} {e2.eid}."
    else:
        print("Both have same salary.")

personList = []
employeeList = []
managerList = []

while True:
    print("Choose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Compare Salaries")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 6:
        print()
        print("Exiting the system. All resources have been freed.")
        print()
        print("Goodbye!")
        break
    
    elif choice == 1:
        pName = input("Enter Name: ")
        pAge = input("Enter Age: ")
        person = Person(pName,pAge)
        personList.append(person)
    
    elif choice == 2:
        eName = input("Enter Name: ")
        eAge = input("Enter Age: ")
        eid = int(input("Enter Employee ID: "))
        eSalary = int(input("Enter Salary: "))
        employee = Employee(eName,eAge,eid,eSalary)
        employeeList.append(employee)
    
    elif choice == 3:
        mName = input("Enter Name: ")
        mAge = input("Enter Age: ")
        eid = int(input("Enter Employee ID: "))
        mSalary = int(input("Enter Salary: "))
        mDepartment = input("Enter Department: ")
        manager = Manager(mName,mAge,eid,mSalary,mDepartment)
        managerList.append(manager)

    elif choice == 4:
        print("Choose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        DisplayChoice = int(input("Enter your choice: "))

        if DisplayChoice == 1:
            for person in personList:
                person.showData()
        elif DisplayChoice == 2:
            for employee in employeeList:
                employee.showData()
        elif DisplayChoice == 3:
            for manager in managerList:
                manager.showData()
        else:
            print("Invalid choice....")
            break

    elif choice == 5:
        print("Choose two employees to compare salaries.")
        firstSalary = int(input("Enter the first employee's ID: "))
        secondSalary = int(input("Enter the second employee's ID: "))
        
        one = None
        two = None

        for employee in employeeList + managerList:
            if employee.eid == firstSalary: 
                one = employee
                print(one)

        for employee in employeeList + managerList:        
            if employee.eid == secondSalary:
                two = employee
                print(two)

        print(one,two)
        if one and two:
            copmareSalary(one,two)
        else:
            print("Try again no person found....")
            
                

        
        












