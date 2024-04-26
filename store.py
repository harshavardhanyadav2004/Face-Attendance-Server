
import mysql.connector
import numpy as np
students ={'Dinesh': '213J1A4267',
 'Ritesh': '213J1A4280',
 'Vardhan': '213J1A4287',
 'Bhavani_shankar': '213J1A4288',
 'Shyam': '213J1A4297',
 'Hemanth_srinivas': '213J1A4298',
 'Harsha_Vardhan': '213J1A42A6',
 'Sadhiq shaik': '213J1A42B1',
 'Sadhik': '213J1A42B2',
 'Manideep': '213J1A42B6',
 'Rohit': '213J1A42B9',
 'Purna': '213J1A42C2',
 'Dev': '213J1A42C3',
 'Murali': '213J1A42C6',
 'Vivek': '213J1A42C9',
 'Deepak': '213J1A42D2',
 'Naveen': '223J5A4208',
 'Praveen': '223J5A4209',
 'Tharun': '223J5A4211'}

address = [
    '/content/Students/213J1A4267.jpg',
    '/content/Students/213J1A4280.jpg',
    '/content/Students/213J1A4287.jpg',
    '/content/Students/213J1A4288.jpg',
    '/content/Students/213J1A4297.jpg',
    '/content/Students/213J1A4298.jpg',
    '/content/Students/213J1A42A6.jpg',
    '/content/Students/213J1A42B1.jpg',
    '/content/Students/213J1A42B2.jpg',
    '/content/Students/213J1A42B6.jpg',
    '/content/Students/213J1A42B9.jpg',
    '/content/Students/213J1A42C2.jpg',
    '/content/Students/213J1A42C3.jpg',
    '/content/Students/213J1A42C6.jpg',
    '/content/Students/213J1A42C9.jpg',
    '/content/Students/213J1A42D2.jpg',
    '/content/Students/223J5A4208.jpg',
    '/content/Students/223J5A4209.jpg',
    '/content/Students/223J5A4211.jpg',
]
names = list(students.keys())
rollNo = list(students.values())
array = np.array([-0.08872673,  0.12595859,  0.07233356, -0.1175533 , -0.07966812,
        0.00037622, -0.03832965, -0.02789011,  0.13205335, -0.11928578,
        0.25209573, -0.07303479, -0.19947901, -0.17329374,  0.02186722,
        0.11221735, -0.09035052, -0.17444593, -0.00288934, -0.10259867,
        0.06860394, -0.01562172, -0.00126103,  0.10094545, -0.17182802,
       -0.36594707, -0.08837051, -0.11724732, -0.00277803, -0.16854236,
       -0.03222755,  0.04825436, -0.18500695, -0.01995997, -0.09012422,
        0.12998892, -0.0040362 , -0.02748638,  0.13282406, -0.00531685,
       -0.14603305, -0.01526514,  0.02521857,  0.29078496,  0.16132191,
        0.0113816 ,  0.01827573,  0.03652227,  0.12006519, -0.24711549,
        0.19335702,  0.12089474,  0.10385803,  0.02959827,  0.14328432,
       -0.0819609 , -0.04407743,  0.09900876, -0.19118588,  0.03944886,
       -0.03751282,  0.05623381, -0.04606102, -0.07833272,  0.20218287,
        0.19002408, -0.08804414, -0.12037624,  0.13706334, -0.14437568,
       -0.05605384,  0.10658067, -0.13690105, -0.10500005, -0.29746386,
        0.12656106,  0.36397737,  0.12405345, -0.1588684 , -0.00622921,
       -0.04188197, -0.07076716,  0.04857829, -0.0122142 , -0.10153079,
        0.05276916, -0.13365157,  0.14173524,  0.13649859, -0.00151819,
       -0.08022977,  0.20566773, -0.01856576,  0.05065173,  0.03925902,
        0.09293066, -0.0891689 ,  0.01142213, -0.13913773, -0.0246264 ,
        0.13571334, -0.0540612 , -0.08873462,  0.12230884, -0.16408369,
        0.1100717 ,  0.00668801, -0.01862857, -0.06415571,  0.06830668,
       -0.17016453, -0.04671033,  0.12195572, -0.21413878,  0.10445505,
        0.11316452, -0.0098037 ,  0.09033692,  0.08529153,  0.00065039,
        0.0254063 , -0.14547122, -0.11679968, -0.04708546,  0.09700096,
        0.01033681,  0.04462369,  0.05450545])
def CreateDataBase():
    connection = mysql.connector.connect(host = 'localhost',user ='root',passwd ='Harsha@2004')
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE Attendance")
    print("Created SuccessFully ")
def CreateTable():
    connection = mysql.connector.connect(host = 'localhost',user = 'root',passwd ='Harsha@2004',database='Attendance')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE USERS (id INT , Name VARCHAR(255) , RollNo VARCHAR(255) , Url_Image  VARCHAR(1024) , faceEncodings VARCHAR(16000))")
    print("Created table successFully ")
def InsertIntoTable():
    connection = mysql.connector.connect(host='localhost',user='root',passwd ='Harsha@2004',database ='Attendance')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO USERS VALUES (%s,%s,%s,%s,%s)',(1,names[0],rollNo[0],address[0],str("/".join([str(i) for i in array]))))
    connection.commit()
    print("Inserted successfully ")
def retreiveTable():
    connection = mysql.connector.connect(host='localhost', user='root',passwd ='Harsha@2004',database ='Attendance')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM USERS")
    for i in cursor:
        print(i)
    newArray = i[4].split("/")
    floatArray = np.array([float(j) for j in newArray ])
    print(floatArray==array)
retreiveTable()  
