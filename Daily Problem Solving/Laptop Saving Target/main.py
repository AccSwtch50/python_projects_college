import math

def main():
    laptop_price = int(input("What's the price of the laptop? "))
    monthly_savings = int(input("How much do you save each month? "))
    
    print(f"You can buy the laptop in {math.ceil(laptop_price / monthly_savings)} months.")

main()
