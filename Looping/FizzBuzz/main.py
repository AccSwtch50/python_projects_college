#This is not licensed under the GPLv2
def main():
    limit = 50
    replacements = {
        3 : "Fizz",
        5 : "Buzz"
    }
    
    for number in range(limit):
        output = ""
        
        for entry in replacements.keys():
            if (number % entry) == 0:
                output += replacements.get(entry, number)
        
        if output == "":
            print(number)
        else:
            print(output)

main()