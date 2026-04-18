def main():
    num_base1 = 10
    num_base2 = 9
    for looped in range(0, 3):
        for num1, num2 in zip(range(num_base1, num_base1 - 10, -1), range(num_base2, num_base2 - 10, -1)):
            print(f"{num1} * {num2} = {num1 * num2}")
            if num2 == 5:
                break
        num_base1 -= 2
        num_base2 -= 1
        print("")

main()
