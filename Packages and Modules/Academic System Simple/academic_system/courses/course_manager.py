def add_course():
    course_name = input("What's the name of your course? ")
    with open("data/courses.txt", "a") as file:
        file.write(f"{course_name}\n")

def view_courses():
    print("Courses: ", end="\n\n")
    with open("data/courses.txt", "r") as file:
        courses = file.readlines()
    for course_index, course in enumerate(courses):
        print(f"{course_index + 1}. {course[:-1]}")
    print("\n\n", end="")