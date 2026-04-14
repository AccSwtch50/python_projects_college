def main():
    list = [1,1,2,2,4,4,5,6]
    print(f"Original list: {list}")
    dedup_list = []
    for item in list:
        if not item in dedup_list:
            dedup_list.append(item)
    print(f"Deduped list: {dedup_list}")

main()