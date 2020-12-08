from connection import connect
from Entity.business import Business

cnx = connect()

def setBusiness(p):
    query = "INSERT INTO `business` VALUES (NULL,%s,%s,%s,%s,%s,%s);"
    cursor = cnx.cursor()
    cursor.execute(query, (p.name, p.addres,p.appointment_time ,p.email ,p.phone ,p.id_owner))
    cnx.commit()
    return cursor.lastrowid

def updateBusiness(p):
    query = "UPDATE `business` SET `name`=%s,`address`=%s,`appointment_time`=%s,`email`=%s,`phone`=%s,`id_owner`=%s WHERE id = %s"
    cursor = cnx.cursor()
    cursor.execute(query, (p.name, p.address,p.appointment_time ,p.email ,p.phone ,p.id_owner, p.id))
    cnx.commit()


def getBusinessById(id):
    query = "SELECT * FROM business WHERE id = %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    for (id,name, address, appointment_time, email, phone, id_owner) in cursor:
        business = Business(id, name, address, appointment_time, email, phone, id_owner)
    cnx.commit()
    return business

def getBusinessBySearch(term):
    query = "SELECT * FROM business WHERE name LIKE %s OR address like %s;"
    cursor = cnx.cursor()
    cursor.execute(query, ('%'+term+'%', '%'+term+'%'))
    business = []
    for (id,name, address, appointment_time, email, phone, id_owner) in cursor:
        business.append(Business(id, name, address, appointment_time, email, phone, id_owner))
    cnx.commit()
    return business

def deleteBusiness(id):
    query = "DELETE FROM business where id = %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    cnx.commit()

# try:
#     print(getBusinessBySearch('ab')[0].name)
# except:
#     ('nothing found')