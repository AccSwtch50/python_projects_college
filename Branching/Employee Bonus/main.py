def main():
    salary = int(input("How much do you earn? "))
    tenure = int(input("How long in years have you worked here? "))
    
    bonus_percentage = 0
    if tenure >= 1:
        bonus_percentage = 5
    if tenure >= 5:
        bonus_percentage = 15
    if tenure >= 10:
        bonus_percentage = 25
    
    bonus_salary = salary * (bonus_percentage / 100)
    total_salary = salary + bonus_salary
    
    print(f"You've got a bonus of Rp{'{0:_}'.format(bonus_salary).replace('.', ',').replace('_', '.')}")
    print(f"Your total salary is Rp{'{0:_}'.format(total_salary).replace('.', ',').replace('_', '.')}")

main()