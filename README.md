# Student CRUD Applicaiton with Python
This project provides a CRUD (Create, Read, Update, Delete) application developed with Python allowing you to use the following operations:
- Get all students (Prints all students in database)
- Add a student (Adds student to the database)
- Update a student's email (Update a student's email in the database using their student ID)
- Delete a student (Delete a student from the database using their student ID)

# Setup
1. Install PostgreSQL on PC and create a database.

2. Add the following table inside your PostgresSQL database using the SQL statement:
```sql
CREATE TABLE students (
	student_id SERIAL PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	enrollment_date DATE NOT NULL
)
```

3. Optional: Insert data for testing:
```sql
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
```

4. Make sure Python3 is installed on your computer

5. Install psycopg2 for PostgreSQL access with Python:
'py -m pip install psycopg2'

6. Download 'student_crud.py' and add your PostgreSQL credentials to the 'Enter database credentials' section 

7. Run the application and manage the database:
'py student_dbms.py'

# Video Showcase
[Youtube Demonstration Video](https://youtu.be/X5PU1L5-LdA)