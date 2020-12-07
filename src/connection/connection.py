import mysql.connector
def connect() :
    cnx = mysql.connector.connect(user= , password= ,
    host= ,
    database='dt5.ehb.be' )
    return cnx

