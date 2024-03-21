# Import required libraries
import sqlite3

# https://www.geeksforgeeks.org/python-sqlite-join-clause/

# Connect to SQLite database
# New file created if it doesn't already exist
conn = sqlite3.connect('sqlite3.db')

# Create cursor object
cursor = conn.cursor()

# Create and populate tables
cursor.executescript('''
    CREATE TABLE IF NOT EXISTS Advisor (
    AdvisorID INTEGER NOT NULL,
    AdvisorName TEXT NOT NULL,
    PRIMARY KEY(AdvisorID)
);

CREATE TABLE IF NOT EXISTS Student (
    StudentID NUMERIC NOT NULL,
    StudentName NUMERIC NOT NULL,
    AdvisorID INTEGER,
    FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID),
    PRIMARY KEY(StudentID)
);

CREATE TABLE IF NOT EXISTS StudentAdvisor (
    StudentID NUMERIC,
    AdvisorID INTEGER,
    FOREIGN KEY(StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID),
    PRIMARY KEY(StudentID, AdvisorID)
);

INSERT INTO Advisor(AdvisorID, AdvisorName) VALUES
    (1,"John Paul"),
    (2,"Anthony Roy"),
    (3,"Raj Shetty"),
    (4,"Sam Reeds"),
    (5,"Arthur Clintwood");

INSERT INTO Student(StudentID, StudentName, AdvisorID) VALUES
    (501,"Geek1",1),
    (502,"Geek2",1),
    (503,"Geek3",3),
    (504,"Geek4",2),
    (505,"Geek5",4),
    (506,"Geek6",2),
    (507,"Geek7",2),
    (508,"Geek8",3),
    (509,"Geek9",NULL),
    (510,"Geek10",1);

INSERT INTO StudentAdvisor(StudentID, AdvisorID) VALUES
    (501,1),
    (501,2),
    (501,3),
    (502,1),
    (503,3),
    (504,2),
    (504,3),
    (505,4),
    (506,2),
    (507,2),
    (508,3),
    (509,NULL),
    (510,1);
''')

# Commit changes to database
# conn.commit()

# Print advisors with the number of students they advise
cursor.execute('''
    SELECT Advisor.AdvisorName, COUNT(StudentAdvisor.StudentID)
    FROM Advisor
    LEFT JOIN StudentAdvisor ON Advisor.AdvisorID = StudentAdvisor.AdvisorID
    GROUP BY Advisor.AdvisorID;
''')

advisors_with_students_count = cursor.fetchall()
print("Advisors with the number of students they advise:")
for advisor in advisors_with_students_count:
    print(f"{advisor[0]}: {advisor[1]} students")

# Closing the connection
conn.close()
