import mysql . connector
conn = mysql . connector . connect (
    host =" localhost " ,
    user =" root " ,
    password ="1d2d3d@DP.9318" ,
    database =" emp "
)
cursor = conn . cursor ()
cursor . execute ("""
    CREATE TABLE student (
        rollno INT PRIMARY KEY ,
        name VARCHAR (50) ,
        course VARCHAR (30) ,
        marks INT
    )
""")
print (" Table created ")
conn . close ()