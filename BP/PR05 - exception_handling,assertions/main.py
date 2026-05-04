# Exception Handling and Assertions


def divide_numbers():
    try:
        num1 = float(input("Enter numerator: "))
        num2 = float(input("Enter denominator: "))
        assert num2 != 0, "Denominator cannot be zero!"  # assertion check
        print(f"Result: {num1 / num2}")
    except ValueError:
        print("Error: Enter a valid number!")
    except AssertionError as e:
        print(f"Assertion Error: {e}")
    finally:
        print("Division operation done.")


def open_file():
    try:
        filename = input("Enter filename: ")
        assert filename.strip() != "", "Filename cannot be empty!"  # assertion check
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Error: File not found!")
    except AssertionError as e:
        print(f"Assertion Error: {e}")
    finally:
        print("File operation done.")


while True:
    print("\n1. Division  2. File Handling  3. Exit")
    ch = input("Choice: ")

    if ch == "1":
        divide_numbers()
    elif ch == "2":
        open_file()
    elif ch == "3":
        break
