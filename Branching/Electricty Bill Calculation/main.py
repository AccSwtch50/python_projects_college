from decimal import Decimal

def calculate_bill(electricity_usage):
    bill_cents = min(electricity_usage, 100) * 10
    electricity_usage -= 100
    
    if electricity_usage <= 0:
        return bill_cents
    
    bill_cents += min(electricity_usage, 200) * 15
    electricity_usage -= 200
    
    if electricity_usage <= 0:
        return bill_cents
    
    bill_cents += electricity_usage * 20
    return bill_cents

def main():
    electricity_usage = int(input("How much electricity do you use in KWh? "))
    
    bill_cents = calculate_bill(electricity_usage)
    
    bill = Decimal(bill_cents) / Decimal(100)
    
    print(f"Your electricity bill costs ${bill}.")

main()