import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

cur.execute(
    """CREATE TABLE IF NOT EXISTS student(id integer primary key autoincrement,name varchar(250) not null,dob date not null);"""
)
cur.execute(
    """CREATE TABLE IF NOT EXISTS teacher(employee_id integer primary key autoincrement,name varchar(250) not null,age int not null,doj date not null);"""
)


def insert_student_details(student_name, student_dob):
    query = "INSERT INTO student(name,dob)VALUES (?,?)"
    cur.execute(query, (student_name, student_dob))
    print("Student Details Inserted successfully")

def insert_teacher_details(teacher_name, teacher_age, teacher_doj):
    query = "INSERT INTO teacher(name,age,doj) VALUES (?,?,?);"
    cur.execute(query, (teacher_name, teacher_age, teacher_doj))
    print("Teacher Details Inserted successfully")

def update_student_name(new_data, st_id):
    query = "UPDATE STUDENT SET name=? where id=?"
    cur.execute(query, (new_data, st_id))
    print("Student name updated successfully")

def update_student_dob(new_data, st_id):
    query = "UPDATE STUDENT SET dob=? where id=?"
    cur.execute(query, (new_data, st_id))
    print("Student dob updated successfully")

user_input = int(
    input("SELECT OPERATION TO BE PERFORMED:\n1.CREATE\n2.READ\n3.UPDATE\n4.DELETE\n")
)

while user_input <= 4 and user_input > 0:
    if user_input == 1:
        table_input = int(input("CHOOSE TABLE:\n1.STUDENT\n2.TEACHER\n"))
        if table_input == 1:
            print("Enter Student Details\n")
            student_name = input("Enter student name:")
            student_dob = input("Enter student date of birth:")
            insert_student_details(student_name, student_dob)
        elif table_input == 2:
            print("Enter Teacher Details")
            teacher_name = input("Enter teacher's name:")
            teacher_age = int(input("Enter teacher age:"))
            teacher_doj = input("Enter date of joining:")
            insert_teacher_details(teacher_name, teacher_age, teacher_doj)

    elif user_input == 2:
        table_input = int(input("CHOOSE TABLE\n1.STUDENT\n2.TEACHER\n"))
        if table_input == 1:
            query = "SELECT * FROM STUDENT;"
            for row in cur.execute(query):
                print(row)
            print("student table displayed successfully\n")
        elif table_input == 2:
            query = "SELECT * FROM teacher;"
            for row in cur.execute(query):
                print(row)
            print("Teacher table displayed successfully\n")

    elif user_input == 3:
        table_input = int(input("CHOOSE TABLE:\n1.STUDENT\n2.TEACHER\n"))
        if table_input == 1:
            st_id = int(input("Enter student_id for which data should be updated:"))
            column_selection = int(
                input(
                    "SELECT COLUMN TO BE UPDATED:\n1.Student_name\n2.Student_dob\n"
                )
            )
            if column_selection == 1:
                new_data = input("Enter student name to be updated: ")
                update_student_name(new_data, st_id)
            elif column_selection == 2:
                new_data = input("Enter dob to be updated: ")
                update_student_dob(new_data,st_id)

    user_input = int(
        input(
            "SELECT OPERATION TO BE PERFORMED:\n1.CREATE\n2.READ\n3.UPDATE\n4.DELETE\n"
        )
    )
