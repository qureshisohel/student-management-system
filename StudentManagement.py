import mysql.connector

# connect to database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="student_management"
)

cursor = db.cursor()

def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    sql = "INSERT INTO students (roll_no, name, marks) VALUES (%s,%s,%s)"
    val = (roll, name, marks)

    cursor.execute(sql, val)
    db.commit()

    print("Student added successfully")

def view_students():
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()

    for row in result:
        print("Roll:", row[0], "Name:", row[1], "Marks:", row[2])

def search_student():
    roll = int(input("Enter Roll Number to search: "))
    sql = "SELECT * FROM students WHERE roll_no=%s"
    
    cursor.execute(sql,(roll,))
    result = cursor.fetchone()
    
    if result:
        print("Roll:",result[0],"Name:",result[1],"Marks:",result[2])
    else:
        print("Student not found")

def update_student():
    roll = int(input("Enter Roll number to update: "))
    name = input(input("Enter new Name: "))
    marks = int(input("Enter new Marks: "))
    
    sql = "UPDATE students SET name=%s,marks=%s, WHERE roll_no=%s"
    val = (name,marks,roll)
    cursor.execute(sql,val)
    db.commit()
    print("Student updated successfully")
    
def delete_student():
    roll = int(input("Enter roll number: "))
    sql = "DELETE FROM students WHERE roll_no=%s"

    cursor.execute(sql, (roll,))
    db.commit()

    print("Student deleted")

while True:
    print("\n--- Student Management System ---")
    print("1 Add Student")
    print("2 View Students")
    print("3 Search Student")
    print("4 Update Student")
    print("5 Delete Student")
    print("6 Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        search_student()
    elif choice == 4:
        update_student()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        print("Exiting Program")
        break
    else:

        print("Invalid Choice")
