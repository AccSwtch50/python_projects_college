import math

def main():
    person_water_needs_per_day = 2.5
    gallon = 19
    gallon_price = 19000
    if input("Do you want to use predefined inputs? (y/n)") == "y":
        number_of_people = 5
    else:
        number_of_people = int(input("How many people live in your house? "))
    
    weekly_water_requirement = (number_of_people * person_water_needs_per_day) * 7
    print(f"The people in this household requires {weekly_water_requirement} litres per week.")
    
    gallons_amount = math.ceil(weekly_water_requirement / gallon)
    print(f"They need to buy {gallons_amount} gallon(s) per week,")
    
    total_budget = gallons_amount * gallon_price
    print(f"Which needs a budget of Rp{'{0:,}'.format(total_budget).replace(',', '.')} for the household to afford.")

main()