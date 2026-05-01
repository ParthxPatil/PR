# Write a Python program to demonstrate predefined clean-up actions
# using the 'with' statement.

# The 'with' statement ensures the file is automatically closed
# after the block ends, even if an exception occurs.

filename = "demo.txt"

# Writing using 'with'
with open(filename, "w") as file:
    file.write("Hello, this is a demo file.\n")
    file.write("Python handles file cleanup automatically with 'with'.\n")

print(f"Written to {filename}.")

# Reading using 'with'
with open(filename, "r") as file:
    contents = file.read()

print("\nFile Contents:")
print("-" * 40)
print(contents)
print("File closed automatically – no need for file.close()!")
