def main():
    list = [1,1,2,2,4,4,5,6]
    print(f"Original list: {list}")
    dedup_list = []
    for item in list:
        item_exists = False
        for item_dedup in dedup_list:
            if item == item_dedup:
                item_exists = True
                break
        if not item_exists:
            dedup_list.append(item)
    print(f"Deduped list: {dedup_list}")

main()