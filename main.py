import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()
cur.execute(
    """CREATE TABLE IF NOT EXISTS student(id integer primary key autoincrement,name varchar(250),dob date);"""
)
cur.execute(
    """CREATE TABLE IF NOT EXISTS teacher(employee_id integer primary key autoincrement,name varchar(250),age int,doj date);"""
)


def insert_student_details(student_name, student_dob):
    query = "INSERT INTO student(name,dob)VALUES (?,?)"
    cur.execute(query, (student_name, student_dob))
    print("Student Details Inserted successfully")


def insert_teacher_details(teacher_name, teacher_age, teacher_doj):
    query = "INSERT INTO teacher(name,age,doj) VALUES (?,?,?);"
    cur.execute(query, (teacher_name, teacher_age, teacher_doj))
    print("Teacher Details Inserted successfully")


user_input = int(input("1.CREATE\n2.READ\n3.UPDATE\n4.DELETE\n"))
while user_input <= 4 and user_input > 0:
    if user_input == 1:
        table_input = int(input("1.STUDENT\n2.TEACHER\n"))
        if table_input == 1:
            student_name = input("Enter name:")
            student_dob = input("Enter date of birth:")
            insert_student_details(student_name, student_dob)
        elif table_input == 2:
            teacher_name = input("Enter teacher's name: ")
            teacher_age = int(input("Enter age: "))
            teacher_doj = input("Enter date of joining: ")
            insert_teacher_details(teacher_name, teacher_age, teacher_doj)
    elif user_input == 2:
        table_input = int(input("1.STUDENT\n2.TEACHER\n"))
        if table_input == 1:
            query = "SELECT * FROM STUDENT;"
            for row in cur.execute(query):
                print(row)
            print("student table displayed successfully")
        elif table_input == 2:
            query = "SELECT * FROM teacher;"
            for row in cur.execute(query):
                print(row)
            print("Teacher table displayed successfully")
    user_input = int(input("1.CREATE\n2.READ\n3.UPDATE\n4.DELETE\n"))
