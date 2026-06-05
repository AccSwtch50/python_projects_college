def check_discount(ticket_count, coupon_code, total_price):
    if ticket_count < 2:
        return total_price
    
    if coupon_code.upper() != "NONTONSERU":
        return total_price
    
    return total_price - 15000

def main ():
    ticket_count = int(input("How many tickets do you have? "))
    total_price = int(input("What are the price of all the tickets? Rp"))
    coupon_code = input("Enter your coupon code: ")
    total_price = check_discount(ticket_count, coupon_code, total_price)
    print(f"You will pay Rp.{"{0:_}".format(total_price).replace("_", ".")} in total.")

main()