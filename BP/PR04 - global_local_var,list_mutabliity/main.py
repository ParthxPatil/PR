# Global variable
counter = 0


def factorial(n):
    # Added check for negative numbers
    if n < 0:
        return "Undefined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def modify_list(my_list):
    print("\nOriginal List inside function:", my_list)
    my_list.append(100)
    print("Modified List inside function:", my_list)


def function_scope_demo():
    global counter  # Explicitly tell Python to use the global variable
    counter = 5  # Now this updates the global variable, not a local one
    print("\nInside function (global modified), counter =", counter)


# Menu
while True:
    print("\n💫 Choose a Concept to Explore:")
    print("1. Recursion (Factorial Calculation)")
    print("2. List Mutability Demonstration")
    print("3. Function Scope Demonstration")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    try:
        if choice == "1":
            num = int(input("Enter a non-negative integer: "))
            print(f"Factorial of {num} is {factorial(num)}")

        elif choice == "2":
            user_list = [10, 20, 30]
            print("\nList before function call:", user_list)
            modify_list(user_list)
            print("List after function call:", user_list)

        elif choice == "3":
            print("\nGlobal counter before function call:", counter)
            function_scope_demo()
            print("Global counter after function call:", counter)

        elif choice == "4":
            print("\n🛑 Exiting Program. Thank you!")
            break

        else:
            print("\n⚠️ Invalid Choice! Please enter a number between 1 and 4.")

    except ValueError:
        print("\n❌ Error: Please enter a valid integer.")
