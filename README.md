# Connecting to the SQLite relational database using python

__Step 1:__ 

Create a python file named "main.py" that contain your script 

__Step 2:__ 

SQLite is a simple relational database system, which saves its data in regular data files or even in the internal memory of the computer.

Insert the following two lines to import the sqlite3 module and connect to the database. Note that your database file need not already exist. 

```python
import sqlite3
connection = sqlite3.connect("company.db")
```
We have now created a database with the name "company". It's like having sent the command "CREATE DATABASE company;" to a SQL server. If you call "sqlite3.connect('company.db')" again, it will open the previously created database. 

__Step 3:__ 



After having created an empty database, you will most probably add one or more tables to this database. 

To be capable to send a command to "SQL", or SQLite, we need a cursor object. Usually, a cursor in SQL and databases is a control structure to traverse over the records in a database. So it's used for the fetching of the results.

We get the cursor object by calling the cursor() method of connection. An arbitrary number of cursors can be created. The cursor is used to traverse the records from the result set. We can define a SQL command with a triple quoted string in Python:


```
sql_command = """
CREATE TABLE employee ( 
staff_number INTEGER PRIMARY KEY, 
fname VARCHAR(20), 
lname VARCHAR(30), 
gender CHAR(1), 
joining DATE,
birth_date DATE);"""
```

 We have defined the staff_number field as "INTEGER PRIMARY KEY" A column which is labelled like this will be automatically auto-incremented in SQLite3. To put it in other words: If a column of a table is declared to be an INTEGER PRIMARY KEY, then whenever a NULL will be used as an input for this column, the NULL will be automatically converted into an integer which will one larger than the highest value so far used in that column. If the table is empty, the value 1 will be used. If the largest existing value in this column has the 9223372036854775807, which is the largest possible INT in SQLite, an unused key value is chosen at random.

__Step 4:__ 

Now we have a database with a table but no data included. To populate the table we will have to send the "INSERT" command to SQLite. We will use again the execute method. The following example is a complete working example. To run the program you will either have to remove the file company.db or uncomment the "DROP TABLE" line in the SQL command: 

Add the following to your file

```python
# delete 
#cursor.execute("""DROP TABLE employee;""")
cursor.execute(sql_command)

sql_command = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
    VALUES (NULL, "William", "Shakespeare", "m", "1961-10-25");"""
cursor.execute(sql_command)


sql_command = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
    VALUES (NULL, "Frank", "Schiller", "m", "1955-08-17");"""
cursor.execute(sql_command)

# never forget this, if you want the changes to be saved:
connection.commit()

connection.close()
```

__Optional: Using a loop__ 


Of course, in most cases, you will not literally insert data into a SQL table. You will rather have a lot of data inside of some Python data type e.g. a dictionary or a list, which has to be used as the input of the insert statement. 

The following working example, assumes that you have already an existing database company.db and a table employee. We have a list with data of persons which will be used in the INSERT statement:

```python
import sqlite3
connection = sqlite3.connect("company.db")

cursor = connection.cursor()

staff_data = [ ("William", "Shakespeare", "m", "1961-10-25"),
               ("Frank", "Schiller", "m", "1955-08-17"),
               ("Jane", "Wall", "f", "1989-03-14") ]
               
for p in staff_data:
    format_str = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
    VALUES (NULL, "{first}", "{last}", "{gender}", "{birthdate}");"""

    sql_command = format_str.format(first=p[0], last=p[1], gender=p[2], birthdate = p[3])
    cursor.execute(sql_command)
    
connection.commit()
connection.close()
```

### Querying the database

create a file called "query.py"

Add the following to the file

```
import sqlite3
connection = sqlite3.connect("company.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM employee") 
print("fetchall:")
result = cursor.fetchall() 
for r in result:
    print(r)
    
cursor.execute("SELECT * FROM employee") 
print("\nfetch one:")
res = cursor.fetchone() 
print(res)
```

If we run this program, saved as "sql_company_query.py", we get the following result, depending on the actual data: 

```
$ python3 sql_company_query.py 
fetchall:
(1, 'William', 'Shakespeare', 'm', None, '1961-10-25')
(2, 'Frank', 'Schiller', 'm', None, '1955-08-17')
(3, 'Bill', 'Windows', 'm', None, '1963-11-29')
(4, 'Esther', 'Wall', 'm', None, '1991-05-11')
(5, 'Jane', 'Thunder', 'f', None, '1989-03-14')

fetch one:
(1, 'William', 'Shakespeare', 'm', None, '1961-10-25')
```


# Loading data from a file

Create a file called main2.py

Move the data file into the same directory as your python file.


Edit your python file to the following:

```

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
```

*Note: you can generate random data using https://mockaroo.com/*

*Source: https://www.python-course.eu/sql_python.php*




