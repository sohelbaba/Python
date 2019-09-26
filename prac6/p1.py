#mysql Connector
import mysql.connector

con = mysql.connector.connect(host='localhost',database='Py_Practical',user='root',password='')

#createQuery = "create database Python"
cursor = con.cursor()
#cursor.execute(createQuery)

create = "create table Student( "
create = create + "rollno int(11),"
create = create + "name varchar(25),"
create = create + "bdate date,"
create = create + "gender char(1),"
create = create + "semester int(11),"
create = create + "python_m decimal(2,2),"
create = create + "java_m decimal(2,2),"
create = create + "php_m decimal(2,2),"
create = create + "total decimal(4,2),"
create = create + "percentage decimal(2,2),"
create = create + "grade char(1));"

cursor.execute(create)
print("Bye")
