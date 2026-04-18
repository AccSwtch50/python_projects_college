def main():
    for width in range(0, 5):
        for repeat in range(0, 5):
            if repeat <= width:
                char = "*"
            else:
                char = "_"
            print(char, end=" ")
        print("")

main()
