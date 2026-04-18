def main():
    for index, num1 in enumerate(range(10, 5, -2)):
        for num2 in range(9 - index, 4, -1):
            print(f"{num1} * {num2} = {num1 * num2}")
            num1 -= 1
        print("")

main()
