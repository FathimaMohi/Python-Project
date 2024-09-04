students = []

def add(id, name,cgpa):
    students.append({"id": id, "name": name,"CGPA": cgpa})

def remove(id):
    global students
    students=[student for student in students if student["id"] != id]

def update(id, name):
    for student in students:
        if student["id"] == id:
            student["name"] = name
            break

def display(id,name,cgpa):
        for student in students:
         print("ID:",id,"Name:",name,"CGPA:",cgpa)

def search(id,name):
    f = [student for student in students if name in student["name"] or id == str(student["id"])]
    print("ID:",id,"Name:",name)

def main():
    while True:
        print("************************Student Management System************************")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Update Student")
        print("4. Display Students")
        print("5. Search Student")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            cgpa=float(input("Enter student CGPA:"))
            add(id, name,cgpa)
        elif choice == "2":
            id = input("Enter student ID to remove: ")
            print("removed successfully")
            remove(id)
        elif choice == "3":
            id = input("Enter student ID to update: ")
            name = input("Enter new student name: ")
            update(id, name)
        elif choice == "4":
            display(id,name,cgpa)
        elif choice == "5":
            name_or_id = input("Enter student name or ID to search: ")
            search(id,name)
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose a valid option.")
main()
