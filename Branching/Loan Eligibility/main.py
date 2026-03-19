def main():
    salary = int(input("How much do you earn in dollars? "))
    credit_score = int(input("What\'s your credit score? "))
    employment_duration = int(input("How many years have you\'ve been working for? "))

    conditions = 0
    if salary >= 3000:
        conditions = conditions | 1
    if credit_score >= 650:
        conditions = conditions | 2
    if employment_duration >= 2:
        conditions = conditions | 4

    conditions_check = conditions ^ 7

    if conditions_check == 0:
        print("Your loan is approved.")
        return
    if f"{conditions_check:b}".count("0") == 2:
        print("Your loan is awaiting approval.")
        return
    print("You are ineligible for a loan.")

main()
