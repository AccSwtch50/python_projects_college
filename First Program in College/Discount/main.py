def main():
	item_price = float(input("What's the price of your item? "))
	if item_price >= 100000:
		item_price = item_price - (item_price * (10/100))
	print(f"The price of your item is: {item_price}")

main()
