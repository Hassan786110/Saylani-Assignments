students = []

def display_students():
    if len(students) != 0:
        total_grades = 0
        print("\n")
        for item in students:
            grade = item['grade']
            print(f"Name: {item['name']} Grade: {grade}")
            total_grades += grade
        print(f"Total Grades: {total_grades} Average Grade: {total_grades / len(students)}")
    else:
        print("\nNo students")

def add_student():
    name = input("\nEnter student name: ")
    grade = int(input("Enter student grade: "))
    students.append({"name": name, "grade": grade})
    display_students()

def delete_student():
    if len(students) != 0:
        name = input("\nEnter student name you want to delete: ")
        flag = True
        for item in students:
            if item["name"] == name:
                students.remove(item)
                flag = False
        if flag:
            print("\nStudent does not exist")
        display_students()
    else:
        print("\nNo students")

def start():
    user_input = input("\na for add item\nd for delete item\nq for quit: ")
    if user_input == "a":
        add_student()
    elif user_input == "d":
        delete_student()
    elif user_input != "q":
        print("\nInvalid Input")

    if user_input != "q":
        start()


display_students()
start()
