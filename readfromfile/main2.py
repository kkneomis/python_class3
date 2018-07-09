
import csv
import sqlite3
connection = sqlite3.connect("company.db")

cursor = connection.cursor()


sql_command = """
CREATE TABLE employee ( 
staff_number INTEGER PRIMARY KEY, 
fname VARCHAR(20), 
lname VARCHAR(30), 
gender CHAR(1), 
joining DATE,
birth_date DATE);"""

cursor.execute(sql_command)

with open('employees.csv', 'rb') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        format_str = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
        VALUES (NULL, "{first}", "{last}", "{gender}", "{birthdate}");"""
        
        sql_command = format_str.format(first=row[0], last=row[1], gender=row[2], birthdate = row[3])
        cursor.execute(sql_command)
    
        
connection.commit()
connection.close()