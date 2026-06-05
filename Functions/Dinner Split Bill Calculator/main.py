def calculate_split_bill(total_bill, people_amount, tip_percent):
    total_bill_with_tip = total_bill + (total_bill * (tip_percent / 100))
    final_bill = total_bill_with_tip / people_amount
    return final_bill

def main():
    total_bill = int(input("What\'s the bill of your dinners? "))
    people_amount = int(input("How many people are at your dinner? "))
    tip_percent = int(input("What percentage do you want to tip? "))
    final_bill = calculate_split_bill(total_bill, people_amount, tip_percent)
    print(f"The final bill for {people_amount} people with {tip_percent} percentage of the original bill added for tips is {final_bill}")

main()
