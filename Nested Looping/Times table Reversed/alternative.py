def main():
    for num1 in range(10, 8, -1):
        for num2 in range(9, 4, -1):
            print(f"{num1} * {num2} = {num1 * num2}")
            num1 -= 1
        print("")

main()
