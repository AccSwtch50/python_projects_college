def main():
    list = [9,100,101,88,3,7]
    largest = float("-inf")
    second_largest = float("-inf")
    for number in list:
        if number > largest:
            second_largest = largest
            largest = number
    print(f"The second largest number in list {list} is {second_largest}.")

main()