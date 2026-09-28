import mysql.connector


# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abhishek@2004",
    database="ai_engineer"
)

print("Connected successfully!")


# Create cursor
cursor = connection.cursor()


# 1. SELECT - View all students
print("\n--- All Students ---")

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)


# 2. SELECT with WHERE - Find AI students
print("\n--- AI Students ---")

cursor.execute("""
    SELECT *
    FROM students
    WHERE course = %s
""", ("AI",))

ai_students = cursor.fetchall()

for student in ai_students:
    print(student)


# 3. INSERT - Add a student
print("\n--- Adding Student ---")

sql = """
    INSERT INTO students (name, age, course, marks)
    VALUES (%s, %s, %s, %s)
"""

values = ("Vijay", 22, "AI", 91)

cursor.execute(sql, values)

connection.commit()

print("Student added successfully!")


# 4. UPDATE - Update marks
print("\n--- Updating Marks ---")

sql = """
    UPDATE students
    SET marks = %s
    WHERE name = %s
"""

values = (95, "Vijay")

cursor.execute(sql, values)

connection.commit()

print("Marks updated successfully!")


# 5. DELETE - Delete Vijay
print("\n--- Deleting Student ---")

sql = """
    DELETE FROM students
    WHERE name = %s
"""

values = ("Vijay",)

cursor.execute(sql, values)

connection.commit()

print("Student deleted successfully!")


# Close cursor and connection
cursor.close()
connection.close()

print("\nMySQL connection closed.")