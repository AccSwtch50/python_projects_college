from academic_system.students import student_manager
from academic_system.courses import course_manager
from academic_system.grades import grade_manager

def main():
    while True:
        print(
        """
        Main menu:
        
        1. Add a student
        2. View students
        3. Add a course
        4. View Courses
        5. Assign a grade
        6. Generate student report
        7. Exit
        
        """
        )
        choice = int(input("Select an option: "))
        
        if choice == 1:
            student_manager.add_student()
        if choice == 2:
            student_manager.view_students()
        if choice == 3:
            course_manager.add_course()
        if choice == 4:
            course_manager.view_courses()
        if choice == 5:
            grade_manager.add_grades()
        if choice == 6:
            grade_manager.generate_report()
        if choice == 7:
            break

main()