def main():
    input_seconds = int(input("Enter seconds: "))
    
    seconds = input_seconds % 60
    minutes = (input_seconds // 60) % 60
    hours = input_seconds // 3600
    
    print(f"{hours} Hour(s), {minutes} Minute(s), and {seconds} second(s)")

main()