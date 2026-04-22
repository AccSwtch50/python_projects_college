def main():
    text = "mang kasir aplikasi sederhana"
    words = 0
    chars = 0
    index = 0
    while True:
        try:
            char_at_index = text[index]
            index += 1
            if char_at_index == " ":
                words += 1
        except:
            chars = index
            non_space_chars = chars - words
            words += 1
            break
    print(f"There are {words} words, {non_space_chars} non-space characters, and {chars} total characters in string {text}.")

main()