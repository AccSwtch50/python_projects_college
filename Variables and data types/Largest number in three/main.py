def main():
    numbers = [0,0,0]
    numbers[0] = int(input("Enter your first number: "))
    numbers[1] = int(input("Enter your second number: "))
    numbers[2] = int(input("Enter your third number: "))
    
    largest_number_idx = 0
    largest_number = numbers[largest_number_idx]
    for number_idx in range(0, len(numbers)):
        number = numbers[number_idx]
        if number >= largest_number:
            largest_number_idx = number_idx
            largest_number = numbers[largest_number_idx]
    
    print(f"The largest number {largest_number} is number {largest_number_idx + 1}.")

main()