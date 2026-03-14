def main():
    word = input("Enter a word: ")
    
    if word.capitalize().startswith("A"):
        print("Starts with A")
    else:
        print("Does not start with A")

main()