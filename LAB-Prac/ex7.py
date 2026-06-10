import mysql . connector
conn = mysql . connector . connect (
    host =" localhost " ,
    user =" root " ,
    password ="1d2d3d@DP.9318" ,
    database =" emp "
)
cursor = conn . cursor ()
cursor . execute (" UPDATE student SET marks = marks + 5")
conn . commit ()
print (" Marks increased ")
conn . close ()
