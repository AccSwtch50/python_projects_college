def main():
    string = input("Enter your string: ")
    reversed_string = ""
    for char_idx in range ((len(string) - 1), -1, -1):
        reversed_string += string[char_idx]
    if string == reversed_string:
        print(f"The string {string} is a palindrome")
    else:
        print(f"The string {string} is not a palindrome ({reversed_string})")

main()