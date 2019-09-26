#mysql Connector
import mysql.connector

def options():
    print("1. Insert Row")
    print("2. Calculate total")
    print("3. Calculate Percentage")
    print("4. Calculate Grade")
    print("5. Update Rollno Wise ")
    print("6. Delete Row")
    print("7. Merit List")
    print("8. Display top 3 Student")
    print("9. Display top 2 Student")
    print("10. Display recored of boys who passed in any two")

def getchoice():
    ch = int(input("Enter Choice : "))
    return ch


def Insertdata(con,cursor):
    rno = input("Enter RollNumber : ")
    name = input("Enter Name :" )
    bdate = input("Enter Birth Date : ")
    gender = input("Enter Gender (M/F) : ")
    semester = input("Enter Semester : ")
    p_m = input("Enter Python Marks : ")
    j_m = input("Enter Java Marks : ")
    ph_m = input("Enter Php Marks : ")

    insertquery = "insert into student(rollno,name,bdate,gender,semester,python_m,java_m,php_m) values('%s','%s','%s','%s','%s','%s','%s','%s')"
    #print(insertquery)
    arg = (rno,name,bdate,gender,semester,p_m,j_m,ph_m)
    cursor.execute(insertquery % arg)
    con.commit()
    print("Insert Record")

def total(con,cursor):
    total = "update student set total = python_m + java_m + php_m"
    cursor.execute(total)
    con.commit()

def percentage(con,cursor):
     per = "update student set percentage = total / 3"
     cursor.execute(per)
     con.commit()

def grade(con,cursor):
    update = "UPDATE  student SET grade = IF(percentage > 70,='A',percentage > 50 = 'B',percentage > 45 = 'C', percentage < 33 ='F')"   
    cursor.execute(update)
    con.commit()
     
#driver --------------------
con = mysql.connector.connect(host='localhost',database='Py_Practical',user='root',password='')
cursor = con.cursor()
options()
ch = getchoice()
if ch == 1:
    Insertdata(con,cursor)
elif ch == 2:
    total(con,cursor)
elif ch == 3:
    percentage(con,cursor)
elif ch == 4:
    grade(con,cursor)
    
    




    
print("Bye")
