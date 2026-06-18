import pandas as pd

def numeric_to_grade(numeric_score):
    grade = "D"
    if numeric_score >= 60:
        grade = "C"
    if numeric_score >= 70:
        grade = "B"
    if numeric_score >= 85:
        grade = "A"
    
    return grade

def num_to_grade_column(column):
    if column.name == "Score":
        return column.map(numeric_to_grade).astype(str)
    return column

def calculate_gpa(scores):
    numerator = 0
    denominator = 0
    for score in scores:
        numerical_grade = 4 - (ord(score["Score"].lower()) - ord("a"))
        numerator += numerical_grade * score["SKS"]
        denominator += score["SKS"]
    return numerator/denominator

def main():
    students_table = pd.read_excel("data.xlsx", sheet_name="Students")
    subjects_table = pd.read_excel("data.xlsx", sheet_name="Subjects")
    raw_scores_table = pd.read_excel("data.xlsx", sheet_name="RawScores")
    
    raw_scores_table = raw_scores_table.apply(num_to_grade_column)
    
    merged_table = pd.merge(left=students_table, right=raw_scores_table, on="StudentID")
    merged_table = pd.merge(left=merged_table, right=subjects_table, left_on="SubjectCode", right_on="Code")
    
    student_ids = set(merged_table["StudentID"].tolist())
    students = dict()
    for student_id in student_ids:
        student_dataframe = merged_table[merged_table['StudentID'] == student_id]
        student_name = student_dataframe["Student Name"].iloc[0]
        student_courses = student_dataframe[["Subject Name", "SKS", "Score"]]
        student_scores = list(student_courses.to_dict(orient="index").values())
        student_gpa = calculate_gpa(student_scores)
        student_stats = {"name" : student_name, "scores" : student_scores, "gpa" : student_gpa}
        students[student_id] = (student_stats)
    
    students_dataframe = pd.DataFrame.from_dict(students, orient="index")
    students_dataframe = students_dataframe.explode("scores").reset_index(names="student_id")
    students_scores_dataframe = pd.json_normalize(students_dataframe["scores"])
    students_dataframe = students_dataframe.drop(columns="scores").join(students_scores_dataframe)
    students_dataframe.to_excel("report.xlsx", index=False)

main()