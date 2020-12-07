from connection import connect
from Entity.business import Business

cnx = connect()

def setBusiness(p):
    query = "INSERT INTO `business` VALUES (NULL,%s,%s,%s,%s,%s,%s);"
    cursor = cnx.cursor()
    cursor.execute(query, (p.name, p.addres,p.appointment_time ,p.email ,p.phone ,p.id_owner))
    cnx.commit()
    cnx.close()
    return cursor.lastrowid

def getBusinessById(id):
    query = "SELECT * FROM business WHERE id = %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    for (id,name, address, appointment_time, email, phone, id_owner) in cursor:
        business = Business(id, name, address, appointment_time, email, phone, id_owner)
    cnx.commit()
    cnx.close()
    return business


