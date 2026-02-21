def main():
	numbers = []
	for count in range(0,2):
		numbers.append(float(input(f"Enter number {count+1}: ")))
	if numbers[0] > numbers[1]:
		print("Number 1 is larger than number 2.")
		return None
	if numbers[0] < numbers[1]:
		print("Number 2 is larger than number 1.")
		return None
	print("Both numbers are the same size")

main()
