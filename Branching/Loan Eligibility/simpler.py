def main():
    salary = int(input("How much do you earn in dollars? "))
    credit_score = int(input("What\'s your credit score? "))
    employment_duration = int(input("How many years have you\'ve been working for? "))

    conditions_count = 0
    if salary >= 3000:
        conditions_count += 1
    if credit_score >= 650:
        conditions_count += 1
    if employment_duration >= 2:
        conditions_count += 1

    if conditions_count == 3:
        print("Your loan is approved.")
        return
    if conditions_count == 2:
        print("Your loan is awaiting approval.")
        return
    print("You are ineligible for a loan.")

main()
