def main():
    predefined_inputs = input("Do you want to use predefined inputs? (y/n)") == "y"
    if predefined_inputs:
        original_price = 12 * (10 ** 6)
        useful_years = 4
        salvage_value = 2 * (10 ** 6)
    else:
        original_price = int(input("What's the original price of the laptiop? "))
        useful_years = int(input("How many years is it projected to be useful for? "))
        salvage_value = int(input("How much is it projected to be worth at the end of it's life? "))
    
    annual_depreciation = (original_price - salvage_value) / useful_years
    print(f"The rate in which it depreciates each year is at Rp{'{0:_}'.format(annual_depreciation).replace('.', ',').replace('_', '.')}")
    
    if predefined_inputs:
        duration_window_years = 2
    else:
        duration_window_years = int(input("How many you want to check for depreciation? "))
    
    depreciation_calculation = salvage_value + (annual_depreciation * (useful_years - duration_window_years))
    print(f"The laptop will be worth Rp{'{0:_}'.format(depreciation_calculation).replace('.', ',').replace('_', '.')} in {duration_window_years} year(s)")

main()