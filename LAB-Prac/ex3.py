import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1d2d3d@DP.9318",
    database="emp"
)
cursor = conn.cursor()
query = "INSERT INTO student VALUES (%s, %s, %s, %s)"
values = (1, "Amit", "CSE", 85)
cursor.execute(query, values)
conn.commit()
print("Inserted")
conn.close()