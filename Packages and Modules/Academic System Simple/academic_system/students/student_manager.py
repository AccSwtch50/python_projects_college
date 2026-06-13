from . import validation

def add_student():
    while True:
        student_name = input("Student name: ")
        if validation.validate_name(student_name):
            break
        print("Invalid student name!")
    
    with open("data/students.txt", "a") as file:
        file.write(f"{student_name}\n")

def view_students():
    print("Students: ", end="\n\n")
    with open("data/students.txt", "r") as file:
        students = file.readlines()
    for student_index, student in enumerate(students):
        print(f"{student_index + 1}. {student[:-1]}")
    print("\n\n", end="")