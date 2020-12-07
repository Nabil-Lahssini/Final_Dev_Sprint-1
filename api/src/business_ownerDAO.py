from connection import connect
from Entity.business_owner import Business_Owner

cnx = connect()

def setBusinessOwner(p):
    query = "INSERT INTO `business_owner` VALUES (NULL,%s,%s,%s,%s,%s);"
    cursor = cnx.cursor()
    cursor.execute(query, (p.firstname, p.lastname,p.date_of_birth ,p.email ,p.phone))
    cnx.commit()
    return cursor.lastrowid

def getBusinessOwnerById(id):
    query = "SELECT * FROM business WHERE id = %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    for (id,firstname, lastname, date_of_birth, email, phone) in cursor:
        business = Business_Owner(id,firstname, lastname, date_of_birth, email, phone)
    cnx.commit()
    return business

