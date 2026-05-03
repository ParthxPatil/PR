def list_operations():
    print("\nList Operations:")
    my_list = list(
        map(int, input("Enter space-separated integers for the list: ").split())
    )
    my_list.append(int(input("Enter a number to append: ")))
    x = int(input("Enter a number to remove: "))
    if x in my_list:
        my_list.remove(x)
    else:
        print("Number not found in the list")
    print("Before Sorting: ", my_list)
    my_list.sort()
    print("Updated List:", my_list)


def tuple_operations():
    print("\nTuple Operations:")
    my_tuple = tuple(
        map(int, input("Enter space-separated integers for the tuple: ").split())
    )
    print("Tuple:", my_tuple)
    y = int(input("Enter a number to count: "))
    print("Count of an element: ", my_tuple.count(y))
    z = int(input("Enter a number to find index: "))
    print("Index of an element: ", my_tuple.index(z))


def dictionary_operations():
    print("\nDictionary Operations:")
    my_dict = {}
    n = int(input("Enter number of key-value pairs: "))
    for _ in range(n):
        key = input("Enter key: ")
        value = input("Enter value: ")
        my_dict[key] = value
    print("Dictionary:", my_dict)

    del_key = input("Enter key to delete: ")
    my_dict.pop(del_key, "Key not found")
    print("Updated Dictionary:", my_dict)

    search_key = input("Enter key to search: ")
    print("Value:", my_dict.get(search_key, "Key not found"))

    update_key = input("Enter key to update value: ")
    if update_key in my_dict:
        my_dict[update_key] = input("Enter new value: ")
        print("Updated Dictionary:", my_dict)
    else:
        print("Key not found")

    print("All Keys:", list(my_dict.keys()))
    print("All Values:", list(my_dict.values()))


def set_operations():
    print("\nSet Operations:")
    my_set = set(
        map(int, input("Enter space-separated integers for the set: ").split())
    )
    my_set.add(int(input("Enter a number to add: ")))
    my_set.discard(int(input("Enter a number to remove: ")))
    print("Updated Set:", my_set)


def main():
    list_operations()
    tuple_operations()
    dictionary_operations()
    set_operations()


if __name__ == "__main__":
    main()
