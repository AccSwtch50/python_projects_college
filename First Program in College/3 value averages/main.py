def main():
	numbers = []
	for count in range(0,3):
		numbers.append(float(input(f"Enter your number ({count + 1}/3): ")))
	print(f"The average of the three numbers is: {(sum(numbers)/len(numbers))}")

main()
