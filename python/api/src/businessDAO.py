from connection import connect
from Entity.business import Business
from idGenerator import generateId
from encrypt import encrypt
from decrypt import decrypt

cnx = connect()

def setBusiness(p):
    query = "INSERT INTO `business` VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    cursor = cnx.cursor()
    cursor.execute(query, (p.id , encrypt(p.business_type), encrypt(p.name),encrypt(p.appointment_time),encrypt(p.country),encrypt(p.city), encrypt(p.code), encrypt(p.street),encrypt(p.house_nr) ,encrypt(p.email) ,encrypt(p.phone) ,encrypt(p.id_owner)))
    cnx.commit()

def setBusinessSearch(p):
    query = "INSERT INTO `search_business` VALUES (NULL,%s,%s);"
    cursor = cnx.cursor()
    id = generateId()
    p.id = id
    cursor.execute(query, (p.name, id))
    cnx.commit()
    setBusiness(p)
    return id

def updateBusiness(p):
    query = "UPDATE `business` SET `name`=%s,`address`=%s,`appointment_time`=%s,`email`=%s,`phone`=%s,`id_owner`=%s WHERE id = %s"
    cursor = cnx.cursor()
    cursor.execute(query, (encrypt(p.name), encrypt(p.address),encrypt(p.appointment_time) ,encrypt(p.email) ,encrypt(p.phone) ,encrypt(p.id_owner), p.id))
    cnx.commit()


def getBusinessById(id):
    query = "SELECT * FROM business WHERE id = %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    for (id,business_type, name, appointment_time,country,city,code,street,house_nr, email, phone, id_owner) in cursor:
        business = Business(id, decrypt(business_type), decrypt(name), decrypt(appointment_time),decrypt(country), decrypt(city), decrypt(code), decrypt(street), decrypt(house_nr), decrypt(email), decrypt(phone), decrypt(id_owner))
    cnx.commit()
    return business

def getBusinessBySearch(term):
    query = "SELECT * FROM `search_business` INNER JOIN business WHERE search_business.token = business.id and search_business.name like %s"
    cursor = cnx.cursor()
    cursor.execute(query, ('%'+term+'%', ))
    business = []
    for (id_search, name_search, token, id,business_type, name, address, appointment_time, email, phone, id_owner) in cursor:
        del id_search, name_search, token
        business.append(Business(id, decrypt(business_type), decrypt(name), decrypt(address), decrypt(appointment_time), decrypt(email), decrypt(phone), decrypt(id_owner)))
    cnx.commit()
    return business

def deleteBusiness(id):
    query = "DELETE FROM business where id = %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    cnx.commit()
