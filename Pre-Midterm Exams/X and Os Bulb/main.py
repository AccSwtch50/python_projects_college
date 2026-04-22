def valid_position(horz, vert):
    valid = False
    if horz == 2:
        valid = True
    if (1 <= horz <= 3) and (1 <= vert <= 2):
        valid = True
    return valid

def main():
    for vert in range(0, 4):
        for horz in range(0, 5):
            valid_for_o = valid_position(horz, vert)
            if valid_for_o:
                print("O", end=" ")
            else:
                print("X", end=" ")
        print("")

main()