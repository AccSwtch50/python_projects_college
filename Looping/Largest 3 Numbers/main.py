def main():
    numbers = [0,0,0]
    for number_idx in range(0, len(numbers)):
        numbers[number_idx] = int(input(f"Enter number {number_idx + 1}: "))
    
    largest_number = numbers[0]
    for number in numbers:
        if number > largest_number:
            largest_number = number
    
    print(f"The largest number is: {largest_number}")

main()