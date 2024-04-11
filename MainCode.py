import re
import mysql.connector
names_list = []
def userName(string):
    checkName = re.findall(r"")
    database = mysql.connector.connect(host = 'localhost',user='root',passwd='Harsha@2004',database ='users')
    cursor = database.cursor()
    cursor.execute("SELECT * FROM users")
    for i in cursor:
        names_list.append(i)
    for i in names_list:
        if i[0]==string :
            return False
    