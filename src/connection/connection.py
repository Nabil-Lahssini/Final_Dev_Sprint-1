import mysql.connector

def connect() :
    cnx = mysql.connector.connect(user= '2021ProgProj2GR10', password= 'sK9eQKtxtU',
    host='dt5.ehb.be',
    database='2021ProgProj2GR10' )
    return cnx
    

