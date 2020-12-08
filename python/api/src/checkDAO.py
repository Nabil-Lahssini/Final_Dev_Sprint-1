from connection import connect
from Entity.business import Business


cnx = connect()


#Check if DAO already exists
def checkBusinessById(id):
    query = "SELECT name FROM business WHERE id = %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    for(name) in cursor:
        result=name
    cnx.commit() 
    return result

def checkBusinessOwnerById(id):
    query = "SELECT firstname FROM business_owner WHERE id = %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    for(firstname) in cursor:
        result=firstname
    cnx.commit() 
    return result
