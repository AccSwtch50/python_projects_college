def main():
	if input("Do you want to use predefined values? (y/n) ") == "y":
		hours_worked = 5
		minutes_worked = 45
		payrate = 85000
	else:
		hours_worked = int(input("How many hours did you work? "))
		minutes_worked = int(input("How many minutes did you work on top of that? "))
		payrate = int(input("How much did you get paid per hour? "))
	
	print(f"You have worked for {hours_worked} hour(s) and {minutes_worked} minute(s), with a pay rate of IDR {payrate}/hour.")
	total_hours = hours_worked + (minutes_worked / 60)
	total_pay = payrate * total_hours
	print(f"You are paid IDR {total_pay} for the entire time you've worked.")
	
main()
