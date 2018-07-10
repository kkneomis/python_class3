import sqlite3
connection = sqlite3.connect("company.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM employee") 
print("fetchall:")
result = cursor.fetchall() 
for r in result:
    print(r[1])
    
cursor.execute("SELECT fname FROM employee") 
print("\nfetch one:")
res = cursor.fetchone() 
print(res)
