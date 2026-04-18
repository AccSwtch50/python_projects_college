import math

def valid_pos(pos, height, max_height):
    valid = False
    if pos == 0:
        valid = True
    if height == 0 or height == max_height:
        valid = True
    return valid

def valid_pos_mirrored(pos, height, max_pos, max_height):
    mirrored_pos = max_pos - pos
    return valid_pos(pos, height, max_height) or valid_pos(mirrored_pos, height, max_height)

def main():
    for height in range(0, 5):
        for horiz in range(0, 5):
            valid_pos = valid_pos_mirrored(horiz, height, 4, 4)
            if valid_pos:
                print("*", end=" ")
            else:
                print("_", end=" ")
        print("")


main()
