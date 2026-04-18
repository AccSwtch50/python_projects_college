import math

def valid_pos(pos, height):
    valid = False
    if pos == height:
        valid = True
    return valid

def valid_pos_mirrored(pos, height, max_pos):
    mirrored_pos = max_pos - pos
    return valid_pos(pos, height) or valid_pos(mirrored_pos, height)

def main():
    for height in range(0, 5):
        for horiz in range(0, 5):
            valid_pos = valid_pos_mirrored(horiz, height, 4)
            if valid_pos:
                print("*", end=" ")
            else:
                print("_", end=" ")
        print("")


main()
