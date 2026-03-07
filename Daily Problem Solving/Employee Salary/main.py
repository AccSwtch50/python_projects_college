import math

def main():
    if input("Do you want to use predefined inputs? (y/n)") == "y":
        base_salary = 5 * (10 ** 6)
        allowance = 75 * (10 ** 4)
        insurance_deduction = 2/100
        tax_deduction = 5/100
    else:
        base_salary = int(input("What is your base salary? "))
        allowance = int(input("What is your allowance? "))
        insurance_deduction = int(input("What percentage of your income is used to cover insurance? ")) / 100
        tax_deduction = int(input("What percentage of your income is taxed? ")) / 100
    
    deductions = (base_salary * insurance_deduction) + ((base_salary + allowance) * tax_deduction)
    salary = base_salary + allowance - deductions
    print(f"Your salary is Rp{'{0:_}'.format(salary).replace('.', ',').replace('_', '.')}")

main()