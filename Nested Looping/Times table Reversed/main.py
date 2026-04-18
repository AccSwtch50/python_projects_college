def main():
    print(list(zip(range(10, 10 - 5, -1), range(9, 4, -1))))
    for num_base in range(10, 8, -1):
        for num1, num2 in zip(range(num_base, num_base - 5, -1), range(9, 4, -1)):
            print(f"{num1} * {num2} = {num1 * num2}")
        print("")

main()
