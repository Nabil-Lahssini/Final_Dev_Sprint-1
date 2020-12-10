from connection import connect
from Entity.business_owner import Business_Owner
from idGenerator import generateId
from encrypt import encrypt
from decrypt import decrypt

cnx = connect()

def setBusinessOwner(p):
    query = "INSERT INTO business_owner (id,firstname,lastname,date_of_birth,email,phone) VALUES (%s,%s,%s,%s,%s,%s);"
    cursor = cnx.cursor()
    id = generateId()
    cursor.execute(query, (id ,encrypt(p.firstname), encrypt(p.lastname),encrypt(p.date_of_birth) ,encrypt(p.email) ,encrypt(p.phone)))
    cnx.commit()
    return id

def getBusinessOwnerById(id):
    query = "SELECT * FROM business_owner WHERE id = %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    business = None
    for (id,firstname, lastname, date_of_birth, email, phone) in cursor:
        del business
        business = Business_Owner(id,decrypt(firstname), decrypt(lastname), decrypt(date_of_birth), decrypt(email), decrypt(phone))
    cnx.commit()
    return business


def updateBusinessOwner(p):
    query = "UPDATE `business_owner` SET `firstname`=%s,`lastname`=%s,`date_of_birth`=%s,`email`=%s,`phone`=%s WHERE id = %s"
    cursor = cnx.cursor()
    cursor.execute(query, (encrypt(p.firstname), encrypt(p.lastname),encrypt(p.date_of_birth) ,encrypt(p.email) ,encrypt(p.phone), p.id))
    cnx.commit()
    
test=Business_Owner(1,'anas','bentaher','05/07/2000','anas@anas','05464684')

def deleteBusinessOwner(id):
    query = "DELETE FROM business_owner where id = %s"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    cnx.commit()

