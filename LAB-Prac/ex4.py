import mysql . connector
conn = mysql . connector . connect (
    host =" localhost " ,
    user =" root " ,
    password ="1d2d3d@DP.9318" ,
    database ="emp"
)
cursor = conn.cursor ()
data = [
    (2 ," Neha " ," IT " ,90) ,
    (3 ," Rahul " ," ECE " ,78)
]
cursor . executemany (" INSERT INTO student VALUES (%s,%s,%s,%s) " ,data )
conn . commit ()
print (" Multiple inserted ")
conn . close ()
