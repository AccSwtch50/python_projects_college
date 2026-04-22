def valid_position(position, height):
    valid = False
    if position == 2:
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