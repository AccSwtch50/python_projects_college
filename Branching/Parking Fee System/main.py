import math

def main():
    vehicle_types = {
        "Motorcycle" : {
            "first_hour_cost" : 1,
            "hour_cost" : 0.5
            },
        "Car" : {
            "first_hour_cost" : 2,
            "hour_cost" : 1
            },
        "Bus" : {
            "first_hour_cost" : 3,
            "hour_cost" : 2
            }
        }
    print("Vehichle Types:")
    vehicle_counter = 0
    for vehicle in vehicle_types:
        vehicle_counter += 1
        print(f"{vehicle_counter}. {vehicle}")
    vehicle_type = input("What kind of vehicle do you use? ")
    hours_parked = int(input("How many hours have you been parking here? "))

    parking_cost = math.ceil(min(1, hours_parked)) * vehicle_types[vehicle_type]["first_hour_cost"]
    parking_cost += math.ceil(max(hours_parked, 1) - 1) * vehicle_types[vehicle_type]["hour_cost"]

    print(f"You have to pay ${parking_cost}.")

main()
