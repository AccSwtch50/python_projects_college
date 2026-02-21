def main():
	number = int(input("Enter a number: "))
	
	if number < 0:
		print(f"The number you entered ({number}) is less than zero (i.e negative)")
		return None
	if number > 0:
		print(f"The number you entered ({number}) is more than zero")
		return None
	print(f"The number you entered ({number}) is zero")

main()
