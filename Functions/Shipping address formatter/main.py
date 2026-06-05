def format_shipping_address(street, city, province, postal_code):
    return f"Street: {street}, City: {city}, {province}, ({postal_code})"

def main():
    street = input("Street: ")
    city = input("City: ")
    province = input("Province: ")
    postal_code = input("Postal Code: ")
    print(format_shipping_address(street, city, province, postal_code))

main()
