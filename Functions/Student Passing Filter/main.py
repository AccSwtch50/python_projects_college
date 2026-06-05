def student_pass_check(student_score, passing_score):
    if student_score < passing_score:
        return False
    return True

def main():
    passing_grade = 80
    student_grade = int(input("Input student score: "))
    student_passed = "passed" if student_pass_check(student_grade, passing_grade) else "failed"
    print(f"The student {student_passed}.")

main()