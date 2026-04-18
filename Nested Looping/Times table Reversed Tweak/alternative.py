def main():
    for looped in range(0, 3):
        num_base1 = 10 - (looped * 2)
        num_base2 = 9 - looped
        for num1, num2 in zip(range(num_base1, 3, -1), range(num_base2, 4, -1)):
            print(f"{num1} * {num2} = {num1 * num2}")
        print("")

main()
