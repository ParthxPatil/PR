# Write a Python program to create and write data into a text file.
# Creates "student.txt" with names and marks of 5 students.

students = [
    ("Alice Johnson",   92),
    ("Bob Smith",       78),
    ("Clara Fernandez", 85),
    ("David Lee",       90),
    ("Eva Sharma",      88),
]

with open("student.txt", "w") as f:
    f.write("Student Records\n")
    f.write("=" * 30 + "\n")
    for name, marks in students:
        f.write(f"{name}: {marks}\n")

print("student.txt created successfully.")
