def main():
    hours_parked = int(input("Hours parked: "))
    
    parking_cost = (min(hours_parked, 2) * 5000) + (max(0, hours_parked - 2) * 3000)
    
    print(f"Total parking fee: Rps{parking_cost}")

main()