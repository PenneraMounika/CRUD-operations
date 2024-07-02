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
    print("Student Details Inserted successfully.")


def insert_teacher_details(teacher_name, teacher_age, teacher_doj):
    query = "INSERT INTO teacher(name,age,doj) VALUES (?,?,?);"
    cur.execute(query, (teacher_name, teacher_age, teacher_doj))
    print("Teacher Details Inserted successfully.")


def update_student_name(new_data, st_id):
    query = "UPDATE STUDENT SET name=? where id=?"
    cur.execute(query, (new_data, st_id))
    print("Student name updated successfully.")


def update_student_dob(new_data, st_id):
    query = "UPDATE STUDENT SET dob=? where id=?"
    cur.execute(query, (new_data, st_id))
    print("Student dob updated successfully.")


def update_teacher_name(new_data, tr_id):
    query = "UPDATE Teacher SET name=? where employee_id=?"
    cur.execute(query, (new_data, tr_id))
    print("Teacher name updated successfully.")


def update_teacher_age(new_data, tr_id):
    query = "UPDATE Teacher SET age=? where employee_id=?"
    cur.execute(query, (new_data, tr_id))
    print("Teacher age updated successfully.")


def update_teacher_doj(new_data, tr_id):
    query = "UPDATE Teacher SET doj=? where employee_id=?"
    cur.execute(query, (new_data, tr_id))
    print("Teacher doj updated successfully.")

def display_student_row_to_delete(row_selection):
    query="SELECT * FROM STUDENT WHERE id=?;"
    for row in cur.execute(query,(row_selection,)):
        print(row)
    else:
        print("Row does not exist.")
        return False

def delete_student_row(row_selection):
    query="DELETE FROM STUDENT WHERE id=?"
    cur.execute(query,(row_selection,))

user_input = int(
    input("SELECT OPERATION TO BE PERFORMED:\n1.CREATE\n2.READ\n3.UPDATE\n4.DELETE\n")
)

while user_input <= 4 and user_input > 0:
    if user_input == 1:
        table_input = int(input("CHOOSE TABLE:\n1.STUDENT\n2.TEACHER\n"))
        if table_input == 1:
            print("Enter Student Details")
            student_name = input("Enter student name:")
            student_dob = input("Enter student date of birth:")
            insert_student_details(student_name, student_dob)
        elif table_input == 2:
            print("Enter Teacher Details")
            teacher_name = input("Enter teacher's name:")
            teacher_age = int(input("Enter teacher age:"))
            teacher_doj = input("Enter date of joining:")
            insert_teacher_details(teacher_name, teacher_age, teacher_doj)
        else:
            print("No such table exists.")
            break
        conn.commit()

    elif user_input == 2:
        table_input = int(input("CHOOSE TABLE\n1.STUDENT\n2.TEACHER\n"))
        if table_input == 1:
            count=0
            query = "SELECT * FROM STUDENT;"
            for row in cur.execute(query):
                count += 1
            if count == 0:
                print("No rows to display in student table.")
            else:
                for row in cur.execute(query):
                    print(row)
                print("Student table displayed successfully.\n")
        elif table_input == 2:
            query = "SELECT * FROM teacher;"
            for row in cur.execute(query):
                count += 1
            if count == 0:
                print("No rows to display in teacher table.")
            else:
                for row in cur.execute(query):
                    print(row)
                print("Teacher table displayed successfully.\n")
        else:
            print("No such table exists.")
            break

    elif user_input == 3:
        table_input = int(input("CHOOSE TABLE:\n1.STUDENT\n2.TEACHER\n"))
        if table_input == 1:
            st_id = int(input("Enter student_id for which data should be updated:"))
            column_selection = int(
                input("SELECT COLUMN TO BE UPDATED:\n1.Student_name\n2.Student_dob\n")
            )
            if column_selection == 1:
                new_data = input("Enter student name to be updated: ")
                update_student_name(new_data, st_id)
            elif column_selection == 2:
                new_data = input("Enter student dob to be updated: ")
                update_student_dob(new_data, st_id)
            else:
                print("Column should be either 1 or 2.")
                break
        elif table_input == 2:
            tr_id = int(
                input("Enter teacher employee_id for which data should be updated:")
            )
            column_selection = int(
                input(
                    "SELECT COLUMN TO BE UPDATED:\n1.Teacher_name\n2.Teacher_age\n3.Teacher_doj\n"
                )
            )
            if column_selection == 1:
                new_data = input("Enter teacher name to be updated: ")
                update_teacher_name(new_data, tr_id)
            elif column_selection == 2:
                new_data = input("Enter teacher age to be updated: ")
                update_teacher_age(new_data, tr_id)
            elif column_selection == 3:
                new_data = input("Enter teacher doj to be updated:")
                update_teacher_doj(new_data, tr_id)
            else:
                print("Column should be either 1,2 or 3.")
                break
        else:
            print("No such table exists.")
            break
        conn.commit()

    elif user_input==4:
        table_input=int(input("CHOOSE TABLE:\n1.STUDENT\n2.TEACHER\n"))
        if table_input==1:
            query = "SELECT * FROM STUDENT;"
            for row in cur.execute(query):
                count += 1
            if count == 0:
                print("No rows to delete in student table.")
            else:
                row_selection=int(input("Enter the id to remove that row from the table:"))
                row_existence=display_student_row_to_delete(row_selection)
                if row_existence!=False:
                    confirm_user_input=input("Confirm deletion of the row selected above:")
                    if confirm_user_input=="yes":
                        delete_student_row(row_selection)
                        print("Selected row deleted successfully")
                    else:
                        print("Deletion cancelled")
                        pass
        conn.commit()
    
    user_input = int(
        input(
            "SELECT OPERATION TO BE PERFORMED:\n1.CREATE\n2.READ\n3.UPDATE\n4.DELETE\n"
        )
    )