import math

def valid_position(pos, height):
    valid = False
    if pos == 2:
        valid = True
    if height == 2:
        valid = True
    return valid

def main():
    for height in range(0, 5):
        for horiz in range(0, 5):
            valid_pos = valid_position(horiz, height)
            if valid_pos:
                print("*", end=" ")
            else:
                print("_", end=" ")
        print("")


main()
