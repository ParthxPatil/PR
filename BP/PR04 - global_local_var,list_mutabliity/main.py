x = 10


def change_value():
    global x
    x = 20
    y = 5
    print("x =", x, "y =", y)


print("Initial x =", x)


def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


def add(list_data):
    list_data.append("New Item")


while True:
    print("\n1. Factorial\n2. List\n3. Counter\n4. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        n = int(input("Enter number: "))
        print("Factorial =", fact(n))

    elif ch == "2":
        lst = [1, 2, 3]
        add(lst)
        print("List =", lst)

    elif ch == "3":
        change_value()

    elif ch == "4":
        break
