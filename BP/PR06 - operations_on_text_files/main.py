import os


def create_file():
    filename = input("Enter the filename to create: ").strip()
    try:
        with open(filename, "w"):
            pass
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")


def write_to_file():
    filename = input("Enter the filename to write to: ").strip()
    content = input("Enter text to write: ")
    try:
        with open(filename, "w") as file:
            file.write(content)
        print(f"Text written to '{filename}' successfully.")
    except Exception as e:
        print(f"Error: {e}")


def read_file():
    filename = input("Enter the filename to read: ").strip()
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
    filename = input("Enter the filename to append to: ").strip()
    content = input("Enter text to append: ")
    try:
        with open(filename, "a") as file:
            file.write("\n" + content)
        print(f"Text appended to '{filename}' successfully.")
    except Exception as e:
        print(f"Error: {e}")


def delete_file():
    filename = input("Enter the filename to delete: ").strip()
    if not os.path.exists(filename):
        print("File not found.")
        return
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")


# Main Menu
while True:
    print("\nText File Operations:")
    print("1. Create a file")
    print("2. Write to a file")
    print("3. Read a file")
    print("4. Append to a file")
    print("5. Delete a file")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        create_file()
    elif choice == "2":
        write_to_file()
    elif choice == "3":
        read_file()
    elif choice == "4":
        append_to_file()
    elif choice == "5":
        delete_file()
    elif choice == "6":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")