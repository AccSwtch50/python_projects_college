def main():
    list = ["Regyt","Mirna","Syifa"]
    print(f"The original list is {list}")
    reversed_list = []
    for item_idx in range((len(list) - 1), -1, -1):
        item = list[item_idx]
        reversed_list.append(item)
    print(f"The reversed list is {reversed_list}")

main()