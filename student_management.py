import sqlite3
# Create Database and Table
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll_no INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")
conn.commit()
# Add Student
def add_student():
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    cursor.execute("INSERT INTO students VALUES (?, ?, ?)",
                   (roll, name, marks))
    conn.commit()
    print("Student Added Successfully!")
# View Students
def view_students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    print("\nStudent Records:")
    for row in data:
        print(row)
# Delete Student
def delete_student():
    roll = int(input("Enter Roll No to Delete: "))
    cursor.execute("DELETE FROM students WHERE roll_no = ?", (roll,))
    conn.commit()
    print("Student Deleted Successfully!")
# Main Menu
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        delete_student()
    elif choice == 4:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice!")
