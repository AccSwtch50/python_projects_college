def main():
    numeric_score = int(input("Enter your score: "))
    
    grade = "D"
    if numeric_score >= 60:
        grade = "C"
    if numeric_score >= 70:
        grade = "B"
    if numeric_score >= 85:
        grade = "A"
    
    print(f"Your score is {numeric_score} and your grade is {grade}.")

main()