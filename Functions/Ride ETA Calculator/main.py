def calculate_eta(distance_km, weather_condition):
    estimated_time_of_arrival = distance_km * 3
    if weather_condition == "rainy":
        estimated_time_of_arrival += 10
    return estimated_time_of_arrival

def main():
    weather_condition = "sunny"
    distance_km = 30
    print(f"The trip takes {calculate_eta(distance_km, weather_condition)} minutes to arrive at destination.")

main()