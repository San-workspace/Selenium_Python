
import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",passwd="",database="py_test")
my_cursor=connection.cursor()
my_cursor.execute("CREATE TABLE test_table"
                  "(emp_name VARCHAR(100),emp_code VARCHAR(100))")