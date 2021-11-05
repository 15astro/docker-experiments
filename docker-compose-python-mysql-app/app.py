import os
import mysql.connector

mysql_host = os.getenv('MYSQL_HOST', "mysql-test")
print("MYSQL_HOST_IS:",mysql_host)
mydb = mysql.connector.connect(
  host=mysql_host,
  user="app_user",
  password="root"
)

print("Hello from docker!")
for i in range(10):
  print(mydb)
