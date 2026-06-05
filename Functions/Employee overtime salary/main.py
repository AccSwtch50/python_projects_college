def calculate_overtime_pay(base_salary, total_hours):
    if total_hours <= 40:
        return base_salary
    overtime_hours = total_hours - 40
    overtime_pay = 50000 * overtime_hours
    final_salary = base_salary + overtime_pay
    return final_salary

def main():
    base_salary = int(input("What\'s the base salary of your employee? "))
    total_hours = int(input("How many hours did your employee worked for? "))
    overtime_pay = calculate_overtime_pay(base_salary, total_hours)
    print(f"You have to pay {overtime_pay} to your employee.")

main()
