def calculate_loyalty_points(total_transaction, member_status):
    if not member_status:
        return 0
    return total_transaction // 20000

def main():
    total_transaction = int(input("Total Transaction: Rp"))
    member_status = bool(input("Member: "))
    print(f"Loyalty points: {calculate_loyalty_points(total_transaction, member_status)}")

main()