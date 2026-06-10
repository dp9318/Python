import mysql . connector
conn = mysql . connector . connect (
    host =" localhost " ,
    user =" root " ,
    password ="1d2d3d@DP.9318" ,
    database =" emp "
)
cursor = conn . cursor ()
cursor . execute (" DELETE FROM student ")
conn . commit ()
print (" All records deleted ")
conn . close ()
