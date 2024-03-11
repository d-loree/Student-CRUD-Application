# py -m pip install psycopg2 - prereq
import psycopg2
import sys

# Enter database credentials here
dbname = 'database name'
user = 'username'
password = 'password'
host = 'localhost'
port = 5432 

menu = """
   MENU   
==========
1: Get All Students
2: Add Student
3: Update Student Email
4: Delete Student
5: Exit

>>> """

try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

except Exception as error:
    # could not connect to database, quit program
    print("ERROR: ", error)
    sys.exit()


while True:
    # Print menu and get user choice
    userInput = input(menu)
    if userInput == '1':
        #getallstudents
        try:
            # fetch all users from database and print each row
            cursor.execute("SELECT * from students;")
            allStudents = cursor.fetchall() 
            print("\nAll Students:")
            for set in allStudents:
                print(set)
            input("\nPress enter to continue...")
        except Exception as error:
            # catch and print any errors while getting all students
            print("ERROR: ", error)

    elif userInput == '2':
        # add student
        try:
            # take user input for adding student
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            email = input("Email: ")
            enrollment_date = input("Enrollment Date: ")

            # excecute SQL statement and make changes persistent with conn.commit()
            cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{}', '{}', '{}', '{}');".format(first_name, last_name, email, enrollment_date))
            conn.commit() 

            # let user know the operation was successful
            print("\nSuccessfully added student {} {}".format(first_name, last_name))
            input("Press enter to continue...")
        except Exception as error:
            # catch and print any errors while adding the data to the database
            print("ERROR: ", error)

    elif userInput == '3':
        # Update student email
        try:
            # take user input for changing email
            studentId = input("Student ID to update email: ")
            newEmail = input("New Email: ")

            # execute SQL statement and make changes persistent
            cursor.execute("UPDATE students SET email = '{}' WHERE student_id = '{}'".format(newEmail, studentId))
            conn.commit()

            # let user know operation was successful
            print("\nSuccessfully updated student {} to the email {}".format(studentId, newEmail))
            input("Press enter to continue...")

        except Exception as error:
            # catch and print any errors while updating user email
            print("ERROR: ", error)

    elif userInput == '4':
        # Delete student
        try:
            # take user input for deleting student
            studentId = input("Student ID to delete: ")

            # excecute SQL statement and make changes persistent
            cursor.execute("DELETE FROM students WHERE student_id = '{}'".format(studentId))
            conn.commit()

            # let user know operaiton was successful
            print("\nSuccessfully deleted student {}".format(studentId))
            input("Press enter to continue...")
        
        except Exception as error:
            # catch and print any errors while deleting student
            print("ERROR: ", error)
        


    elif userInput == '5':
         # Exit program
        print("Exiting...")
        cursor.close()
        conn.close()
        break