def divide_numbers():
    """Function to demonstrate exception handling with try-except-finally"""
    try:
        num1 = float(input("\nEnter the numerator: "))
        num2 = float(input("Enter the denominator: "))

        # Assertion to ensure denominator is not zero
        assert num2 != 0, "Denominator cannot be zero!"

        result = num1 / num2
        print(f"✅ Division result: {result}")

    except ValueError:
        print("⚠ Error: Please enter a valid number!")

    except AssertionError as ae:
        print(f"⚠ Assertion Error: {ae}")

    except ZeroDivisionError:
        print("⚠ Error: Division by zero is not allowed!")

    except Exception as e:
        print(f"⚠ Unexpected Error: {e}")

    finally:
        print("✧ Finally block executed: Cleaning up resources...")


def open_file():
    """Function to demonstrate file handling exceptions"""
    try:
        filename = input("\nEnter file name to open: ")

        # Assertion to check if filename is not empty
        assert filename.strip() != "", "File name cannot be empty!"

        with open(filename, "r") as file:
            content = file.read()
            print("\n📄 File Content:\n", content)

    except FileNotFoundError:
        print("⚠ Error: File not found! Please check the filename.")

    except AssertionError as ae:
        print(f"⚠ Assertion Error: {ae}")

    except Exception as e:
        print(f"⚠ Unexpected Error: {e}")

    finally:
        print("✧ Finally block executed: File operation completed.")


# Menu
while True:
    print("\n📌 Choose an Exception Handling Demo:")
    print("1. Division Operation (Zero Division & Assertion Error)")
    print("2. File Handling (File Not Found & Assertion Error)")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        divide_numbers()

    elif choice == "2":
        open_file()

    elif choice == "3":
        print("\n🛑 Exiting Program. Thank you!")
        break

    else:
        print("\n⚠ Invalid Choice! Please enter a number between 1 and 3.")
