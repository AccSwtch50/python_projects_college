import math

def main():
    if input("Do you want to use predefined inputs? (y/n) ") == "y":
        travel_distance = 180
        consumption_rate = 40
        fuel_price = 13000
    else:
        travel_distance = int(input("How far is the destination in kilometers? "))
        consumption_rate = int(input("How much kilometers do you get per liter? "))
        fuel_price = int(input("How much in Indonesian Rupiah does the gas cost per liter? "))
    
    print(f"Your destination is {travel_distance} km away,\nit costs Rp{'{0:,}'.format(fuel_price).replace(',', '.')}/liter,\nand each liter gets you {consumption_rate} kilometers further")
    
    fuel_required = math.ceil(travel_distance / consumption_rate)
    total_cost = fuel_price * fuel_required
    print(f"The total cost of the trip is Rp{'{0:,}'.format(total_cost).replace(',', '.')}")

main()