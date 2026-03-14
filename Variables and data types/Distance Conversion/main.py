def main():
    distance_kilometers = int(input("Enter your distance in kilometers: "))
    
    distance_meters = distance_kilometers * 1000
    distance_centimeters = distance_meters * 100
    distance_miles = float(distance_kilometers) * 0.621371
    
    print("The distances are:")
    print(f"{distance_kilometers} km")
    print(f"{distance_meters} m")
    print(f"{distance_centimeters} cm")
    print(f"{distance_miles} miles")

main()