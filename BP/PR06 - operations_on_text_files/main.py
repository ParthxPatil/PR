import os

def get_filename(prompt):
    return input(prompt).strip()


def create_file():
    filename = get_filename("Enter the filename to create: ")
    try:
        with open(filename, "w"):
            pass
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")


def write_to_file():
    filename = get_filename("Enter the filename to write to: ")
    content = input("Enter text to write: ")
    try:
        with open(filename, "w") as file:
            file.write(content)
        print(f"Text written to '{filename}' successfully.")
    except Exception as e:
        print(f"Error: {e}")


def read_file():
    filename = get_filename("Enter the filename to read: ")
    if not os.path.exists(filename):
        print("File not found.")
        return

    try:
        with open(filename, "r") as file:
            print("\nFile Content:")
            print(file.read())
    except Exception as e:
        print(f"Error: {e}")


def append_to_file():
    filename = get_filename("Enter the filename to append to: ")
    content = input("Enter text to append: ")
    try:
        with open(filename, "a") as file:
            file.write("\n" + content)
        print(f"Text appended to '{filename}' successfully.")
    except Exception as e:
        print(f"Error: {e}")


def delete_file():
    filename = get_filename("Enter the filename to delete: ")
    if not os.path.exists(filename):
        print("File not found.")
        return

    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    actions = {
        "1": create_file,
        "2": write_to_file,
        "3": read_file,
        "4": append_to_file,
        "5": delete_file,
    }

    while True:
        print("\nText File Operations:")
        print("1. Create a file")
        print("2. Write to a file")
        print("3. Read a file")
        print("4. Append to a file")
        print("5. Delete a file")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "6":
            print("Exiting program.")
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
