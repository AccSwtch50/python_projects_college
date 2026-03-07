import math

def main():
    paint_coverage = 10
    if input("Do you want to use predefined inputs? (y/n)") == "y":
        length = 4
        width = 3
        height = 3
    else:
        length = int(input("What is the length of the room in meters? "))
        width = int(input("What is the width of the room in meters? "))
        height = int(input("What is the height of the room in meters? "))
    
    length_side_area = length * height
    width_side_area = width * height
    
    paint_amount = math.ceil((length_side_area + width_side_area) / paint_coverage)
    
    print(f"The amount of paint needed to paint the room is {paint_amount}")

main()