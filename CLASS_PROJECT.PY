import mysql.connector
class_project = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "Chandu@123",
    database = "class"

)

# print(class_project)

class_data = class_project.cursor()

# class_data.execute("CREATE DATABASE CLASS")
# class_data.execute("CREATE TABLE MONITOR (ROLLNO VARCHAR(50), NAME VARCHAR(50), MONTH VARCHAR(50))")
# class_data.execute("CREATE TABLE MARKS (ROLL VARCHAR(50), NAME VARCHAR(50), SUBJECT1 INT, SUBJECT2 INT, SUBJECT3 INT, TOTAL INT, PERCENTAGE float, term VARCHAR(50))")
# class_data.execute("CREATE TABLE ATTENDANCE (DATE VARCHAR(50), ABSENT VARCHAR(50))")
# class_data.execute("CREATE TABLE STUDENTS (ROLLNO VARCHAR(50), NAME VARCHAR(50), PHONE VARCHAR(50), ADDRESS VARCHAR(50))")
# class_project.commit()

# Another way to connect..............................................

# import mysql.connector as project

# class_project = project.connect(

#     host = "localhost",
#     user = "root",
#     password = "Chandu@123",
#     database = "class"
# )

# print(class_project)

# class_data = class_project.cursor()

# a = "CREATE DATABASE CLASS"

# class_data.execute(a)

# b = "CREATE TABLE MONITOR (ROLLNO VARCHAR(50), NAME VARCHAR(50), MONTH VARCHAR(50))"

# class_data.execute(b)

# c = "CREATE TABLE MARKS (ROLL VARCHAR(50), NAME VARCHAR(50), SUBJECT1 INT, SUBJECT2 INT, SUBJECT3 INT, TOTAL INT, PERCENTAGE float, term VARCHAR(50))"

# class_data.execute(c)

# d = "CREATE TABLE ATTENDANCE (DATE VARCHAR(50), ABSENT VARCHAR(50))"

# class_data.execute(d)

# e = "CREATE TABLE STUDENTS (ROLLNO VARCHAR(50), NAME VARCHAR(50), PHONE VARCHAR(50), ADDRESS VARCHAR(50))"

# class_data.execute(e)

# class_project.commit()


############################################### Programming ###################################################3


def monitor():
    print("1. Update Monitor   2. Check Monitor \n")
    m = int(input("Enter the task: "))
    if m == 1:
        r = input("Enter Student Roll No: ")
        n = input("Enter Student Name: ")
        c = input("Enter Month: ")
        data = (r,n,c)
        sql = "INSERT INTO MONITOR values(%s,%s,%s)"
        class_data = class_project.cursor()
        class_data.execute(sql,data)
        class_project.commit()
        print("\nData Entered Successfully")
        main()
    else:
        sql = "SELECT * FROM MONITOR"
        class_data = class_project.cursor()
        class_data.execute(sql)
        x = class_data.fetchall()
        for i in x:
            print(i)
        main()

def marks():
    print("1. Update Marks     2. Check Marks \n")
    m = int(input("Enter the task: "))
    if m == 1:
        r = input("Enter Student RollNo: ")
        n = input("Enter Student Name: ")
        s1 = float(input("Subject 1: "))
        s2 = float(input("Subject 2: "))
        s3 = float(input("Subject 3: "))
        t = s1 + s2 + s3
        per = (t/300)*100
        term = input("Enter Term: ")
        data = (r,n,s1,s2,s3,t,per,term)
        sql = "INSERT INTO MARKS values(%s,%s,%s,%s,%s,%s,%s,%s)"
        class_data = class_project.cursor()
        class_data.execute(sql,data)
        class_project.commit()
        print("Data Entered Sucessfully")
        main()
    else:
        r = input("Enter RollNo: ")
        t = input("Enter Term: ")
        sql = "SELECT * FROM MARKS WHERE ROLL = %s and term = %s"
        class_data = class_project.cursor()
        class_data.execute(sql,(r,t))
        for i in class_data:
            print(i)
        main()


def attendance():
    print("1. Update Attendacne     2. Check Attendacne \n")
    a = int(input("Enter the task: "))
    if a == 1:
        d = input("Enter Date: ")
        r = input("Enter Roll No: ")
        data = (d,r)
        sql = "INSERT INTO ATTENDANCE values(%s,%s)"
        class_data = class_project.cursor()
        class_data.execute(sql,data)
        class_project.commit()
        print("\nData Entered Sucessfully")
        main()
    else:
        sql = "SELECT * FROM ATTENDANCE"
        class_data = class_project.cursor()
        class_data.execute(sql)
        x = class_data.fetchall()
        for i in x:
            print(i)
        main()

def students():
    print("1. Update Student Details     2. Check Student Details \n")
    s = int(input("Enter the task: "))
    if s == 1:
        r = input("Enter Student RollNO: ")
        n = input("Enter Student Name: ")
        p = input("Enter Phone: ")
        a = input("Enter Address: ")
        data = (r,n,p,a)
        sql = "INSERT INTO STUDENTS values(%s,%s,%s,%s)"
        class_data = class_project.cursor()
        class_data.execute(sql,data)
        class_project.commit()
        print("\nData Entered Sucessfully")
        main()
    else: 
        sql = "SELECT * FROM STUDENTS"
        class_data = class_project.cursor()
        class_data.execute(sql)
        x = class_data.fetchall()
        for i in x:
            print(i)
        main()


def main():
    print("""

    1.Monitor
    2.Report Card
    3.Attendance
    4.Students

    """)
    choice = input("Enter Task No: ")
    while True:
        if(choice == '1'):
            monitor()
        elif(choice == '2'):
            marks()
        elif(choice == '3'):
            attendance()
        elif(choice == '4'):
            students()
        else:
            print("Wrong choice..................")
main()



