# Write a Python program to read and display content from a text file.
# Reads "student.txt" line by line.

try:
    with open("student.txt", "r") as f:
        print("Contents of student.txt:")
        print("-" * 30)
        for line in f:
            print(line, end="")
except FileNotFoundError:
    print("Error: student.txt not found. Run Q19/main.py first to create it.")
