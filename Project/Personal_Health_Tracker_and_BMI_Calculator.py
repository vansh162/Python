print("Welcome to the Personal Health Tracker and BMI Calculator")
print()
print("----------------------------------")
print("BMI Classification")
print("----------------------------------")
print("Underweight: BMI < 18.5")
print("Normal weight: 18.5 ≤ BMI < 24.9")
print("Overweight: 25 ≤ BMI < 29.9")
print("Obese: BMI ≥ 30")
print("----------------------------------")
print()

record = []

def add():
    rID = int(input("Enter Record ID: "))
    dob = input("Enter Date (DD/MM/YYYY): ")
    weight = float(input("Enter Weight (kg): "))
    height = float(input("Enter Height (m): "))
    desc = input("Enter Activity Description: ")
    bmi = weight / height**2
    record.append({"rid": rID , "dob" : dob , "weight":weight, "height":height, "desc":desc, "BMI":bmi})
    ans = ""
    if bmi < 18.5:
            ans = "Underweight"
    elif 18.5 <= bmi < 24.9:
         print("Normal weight")
    elif 25 < bmi < 29.9:
         print("Overweight")
    elif bmi>=30:
         print("Obese")

    print(f"BMI: {bmi} {ans}")
    print("Health record added successfully!")

def view():
    for records in record:
         print(records)

def update():
     uID = int(input("Enter Record ID where you wanna edit: "))

     for records in record:
          if records["rid"] == uID:
                dob = input("Enter Date (DD/MM/YYYY): ")
                weight = float(input("Enter Weight (kg): "))
                height = float(input("Enter Height (m): "))
                desc = input("Enter Activity Description: ")
                records["rid"] = ({"dob" : dob , "weight":weight, "height":height, "desc":desc})
                bmi = weight / height**2
                ans = ""
                if bmi < 18.5:
                        ans = "Underweight"
                elif 18.5 <= bmi < 24.9:
                    ans = "Normal weight"
                elif 25 < bmi < 29.9:
                    ans = "Overweight"
                elif bmi>=30:
                    ans = "Obese"

                print(f"BMI: {bmi} ({ans})")
                print("Health record updated successfully!")

def delete():
        dID = int(input("Enter Record ID where you wanna delete: "))   
        for records in record:
            if records["rid"] == dID:
                record.remove(records)       
                print("Deleted....")       
                return 

def advice():
    weight = float(input("Enter Weight (kg): "))
    height = float(input("Enter Height (m): "))
    ad = ""
    bmi = weight / height**2
    ans = ""
    if bmi < 18.5:
        ans = "Underweight"
    elif 18.5 <= bmi < 24.9:
        ans = "Normal weight"
    elif 25 < bmi < 29.9:
        ans = "Overweight"
    elif bmi>=30:
        ans = "Obese"
    print()
    if ans == "Underweight":
        ad = "To safely and effectively gain weight, focus on a balanced diet rich in calories and nutrients, incorporate regular strength training, and consider eating smaller, more frequent meals throughout the day. "
    elif ans == "Normal weight":
        ad = "For maintaining a healthy weight and overall well-being, focus on a balanced diet, regular physical activity, and healthy habits like sufficient sleep and stress management."
    elif ans == "Overweight":
        ad = "Focus on Whole Foods: Include plenty of fruits, vegetables, whole grains, and lean protein sources in your meals."
    elif ans == "Obese":
        ad = "For an obese person, focusing on a healthy lifestyle through diet, exercise, and sleep is crucial. This includes eating a balanced diet rich in fruits, vegetables, and whole grains, engaging in regular physical activity, and prioritizing adequate sleep."

def analyze():
    totalBMI = sum(record["BMI"] for records in record)
    avgBMI = totalBMI/len(record)
    higestBMI = max(record["BMI"] for records in record)
    print(f"Average BMI: {avgBMI}")
    print(f"Higest BMI: {higestBMI}")
    
while True:
    print("1. Add a new health record")
    print("2. View all health records")
    print("3. Update a health record")
    print("4. Delete a health record")
    print("5. Calculate BMI and get health advice")
    print("6. Analyze health trends")
    print("7. Exit")
    choice = int(input("Enter your choice: ")) 

    if choice == 7:
        break
    
    elif choice == 1:
        add()
    
    elif choice == 2:
        view()

    elif choice == 3:
         update()
    
    elif choice == 4:
        delete()
    
    elif choice == 5:
        advice()
    
    elif choice == 6:
        analyze()


