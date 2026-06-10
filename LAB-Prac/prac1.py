import mysql.connector
# Establish connection
conn = mysql.connector.connect (
host ="localhost" ,
user ="root" ,
password ="1d2d3d@DP.9318" ,
database ="emp"
)
# Create cursor object
cursor = conn . cursor ()
print (" Connected to MySQL successfully !")
# Close connection
conn . close ()