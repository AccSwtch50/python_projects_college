import math

def main():
    age_years = float(input("Enter your age in years: "))
    
    age_months = math.floor(age_years * 12)
    age_years -= age_months // 12
    age_weeks = math.floor(age_years * 52)
    age_years -= age_years // 52
    age_days = age_years * 365
    
    print(f"{age_months} Month(s), {age_weeks} Week(s), and {age_days} Day(s)")

main()