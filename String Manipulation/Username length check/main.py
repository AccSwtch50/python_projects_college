def main():
    while True:
        username = input("Enter your username: ")
        
        if len(username) >= 5:
            break
        else:
            print("Username too short!")
    print("Username accepted.")

main()