def main():
    distance = int(input("How far did you go in kilometers? "))
    travel_time = int(input("How long did it take in hours? "))
    
    average_speed = distance / travel_time
    print(f"On average, you're traveling at {average_speed} km/h")
    if average_speed > 80:
        print("High speed")

main()