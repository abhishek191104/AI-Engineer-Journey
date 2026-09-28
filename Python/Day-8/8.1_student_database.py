import mysql.connector


def connect_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="__",
        database="ai_engineer"
    )


def add_student():

    connection = connect_database()
    cursor = connection.cursor()

    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    marks = int(input("Enter marks: "))

    sql = """
    INSERT INTO students (name, age, course, marks)
    VALUES (%s, %s, %s, %s)
    """

    values = (name, age, course, marks)

    cursor.execute(sql, values)

    connection.commit()

    print("Student added successfully!")

    cursor.close()
    connection.close()


def view_students():

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    print("\nID | Name | Age | Course | Marks")
    print("-" * 50)

    for student in students:
        print(student)

    cursor.close()
    connection.close()


def search_student():

    connection = connect_database()
    cursor = connection.cursor()

    name = input("Enter student name: ")

    sql = """
    SELECT *
    FROM students
    WHERE name = %s
    """

    cursor.execute(sql, (name,))

    students = cursor.fetchall()

    if students:

        for student in students:
            print(student)

    else:

        print("Student not found.")

    cursor.close()
    connection.close()


def update_marks():

    connection = connect_database()
    cursor = connection.cursor()

    student_id = int(input("Enter student ID: "))
    marks = int(input("Enter new marks: "))

    sql = """
    UPDATE students
    SET marks = %s
    WHERE id = %s
    """

    cursor.execute(sql, (marks, student_id))

    connection.commit()

    print("Marks updated successfully!")

    cursor.close()
    connection.close()


def delete_student():

    connection = connect_database()
    cursor = connection.cursor()

    student_id = int(input("Enter student ID: "))

    sql = """
    DELETE FROM students
    WHERE id = %s
    """

    cursor.execute(sql, (student_id,))

    connection.commit()

    print("Student deleted successfully!")

    cursor.close()
    connection.close()


while True:

    print("\n===== Student Database =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_student()

    elif choice == "2":

        view_students()

    elif choice == "3":

        search_student()

    elif choice == "4":

        update_marks()

    elif choice == "5":

        delete_student()

    elif choice == "6":

        print("Thank you!")

        break

    else:

        print("Invalid choice.")