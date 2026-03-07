def main():
    if input("Do you want to use predefined values? (y/n)") == "y":
        bill = 347500
        friend_number = 3
    else:
        bill = float(input("How large is your bill? "))
        friend_number = int(input("How many friends do you have? "))
    
    print(f"The bill is {bill}")
    print(f"You have {friend_number} friend(s)")
    total_bill = bill + (bill * (10/100))
    print(f"The total bill for everyone is {total_bill}.")
    bill_per_person = bill / (friend_number + 1)
    print(f"The bill per person is {bill_per_person}.")

main()
