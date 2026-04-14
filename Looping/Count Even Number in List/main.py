def main():
    numbers = [1,5,7,8,10,18,50]
    even_numbers = 0
    for number in numbers:
        if (number % 2) == 0:
            even_numbers += 1
    print(f"Even numbers = {even_numbers}")

main()
