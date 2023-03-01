try:
    import mysql.connector
    connection=mysql.connector.connect(host="localhost ",user="root",password="",database="mydb")
    mycursor=connection.cursor()
    sql="SELECT * from `table2` where employee_name=%s"
    emp_name = ("san",)
    mycursor.execute(sql,emp_name)
    myresult=mycursor.fetchall()


    for res in myresult:
        print(res)

except:
    print("exception error")
finally:
    mycursor.close()
    connection.close()
