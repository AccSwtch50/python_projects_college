def main():
    length = int(input("Length: "))
    width = int(input("Width: "))
    
    area = length * width
    perimeter = 2 * (length + width)
    
    print(f"Area: {area}\nPerimeter: {perimeter}")
    if area > 100:
        print("Large area")

main()