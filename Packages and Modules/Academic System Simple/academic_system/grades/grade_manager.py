from ..students import student_manager
from ..courses import course_manager

def add_grades():
    student_manager.view_students()
    student_index = int(input("Select student: ")) - 1
    print("")
    course_manager.view_courses()
    course_index = int(input("Select course: ")) - 1
    print("")
    grade = input("Input Grade: ")
    with open("data/grades.txt", "a") as file:
        file.write(';'.join([str(student_index), str(course_index), grade, "\n"]))

def generate_report():
    student_manager.view_students()
    student_index = int(input("Select student: ")) - 1
    print("")
    with open("data/courses.txt", "r") as file:
        courses = file.readlines()
    with open("data/students.txt", "r") as file:
        students = file.readlines()
    grades = []
    with open("data/grades.txt", "r") as file:
        for line in file:
            elements = line.split(";")
            if int(elements[0]) != student_index:
                continue
            grades.append((courses[int(elements[1])][:-1], elements[2]))
    
    print(f"Report for {students[student_index][:-1]}:", end = "\n\n")
    for grade in grades:
        print(f"{grade[0]}: {grade[1]}")
    print("")
