from connection import connect
from Entity.business import Business


cnx = connect()


#Check if DAO already exists
def checkBusinessById(id):
    query = "SELECT * FROM business WHERE id = %s;"
    cursor = cnx.cursor()
    count = cursor.execute(query, (id))
    cnx.commit() 
    return bool(count != 0)

def checkBusinessOwnerById(id):
    query = "SELECT * FROM business_owner WHERE id = %s;"
    cursor = cnx.cursor()
    count = cursor.execute(query, (id))
    cnx.commit() 
    return bool(count != 0)
