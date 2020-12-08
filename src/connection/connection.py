import mysql.connector 

def connect() :
    cnx = mysql.connector.connect(user= 'root', password= '',
    host='127.0.0.1',
    database='programming_project' )
    return cnx
    

