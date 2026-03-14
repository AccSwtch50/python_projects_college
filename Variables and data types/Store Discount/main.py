def main():
    base_price = float(input("Enter your base price: "))
    
    print(f"The base price is Rp{'{0:_}'.format(base_price).replace(".", ",").replace("_", ".")}")
    
    discount_percentage = 0
    if base_price >= 250000:
        discount_percentage = 10
    if base_price >= 500000:
        discount_percentage = 20
    
    discounted_price = base_price - (base_price * (discount_percentage / 100))
    print(f"The discounted price is Rp{'{0:_}'.format(discounted_price).replace(".", ",").replace("_", ".")}")

main()