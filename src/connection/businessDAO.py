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

def getBusinessBySearch(term):
    query = "SELECT * FROM business WHERE name LIKE %s OR address like %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (term, term ))
    business = None
    for (id,name, address, appointment_time, email, phone, id_owner) in cursor:
        del business
        business = Business(id, name, address, appointment_time, email, phone, id_owner)
    cnx.commit()
    cnx.close()
    if business != None:
        return business
    else:
        return None

def deleteBusiness(id):
    query = "DELETE FROM business where id = %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    cnx.commit()
    cnx.close()