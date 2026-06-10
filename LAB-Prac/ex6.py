import mysql . connector
conn = mysql . connector . connect (
    host =" localhost " ,
    user =" root " ,
    password ="1d2d3d@DP.9318" ,
    database =" emp "
)
cursor = conn . cursor ()
cursor . execute (" UPDATE student SET marks =95 WHERE rollno =1")
conn . commit ()
print (" Updated ")
conn . close ()
