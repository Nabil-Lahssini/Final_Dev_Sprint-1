from connection import connect
from Entity.business_owner import Business_Owner

cnx = connect()

def setBusinessOwner(p):
    query = "INSERT INTO business_owner (id,firstname,lastname,date_of_birth,email,phone) VALUES (NULL,%s,%s,%s,%s,%s);"
    cursor = cnx.cursor()
    cursor.execute(query, (p.firstname, p.lastname,p.date_of_birth ,p.email ,p.phone))
    cnx.commit()
    return cursor.lastrowid

def getBusinessOwnerById(id):
    query = "SELECT * FROM business_owner WHERE id = %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    for (id,firstname, lastname, date_of_birth, email, phone) in cursor:
        business = Business_Owner(id,firstname, lastname, date_of_birth, email, phone)
    cnx.commit()
    return business


def updateBusinessOwner(p):
    query = "UPDATE `business_owner` SET `firstname`=%s,`lastname`=%s,`date_of_birth`=%s,`email`=%s,`phone`=%s WHERE id = %s"
    cursor = cnx.cursor()
    cursor.execute(query, (p.firstname, p.lastname,p.date_of_birth ,p.email ,p.phone, p.id))
    cnx.commit()
    
test=Business_Owner(1,'anas','bentaher','05/07/2000','anas@anas','05464684')

def deleteBusinessOwner(id):
    query = "DELETE FROM business_owner where id = %s"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    cnx.commit()


def getBusinessBySearch(string):
    query = "SELECT * FROM business_owner WHERE firstname LIKE %s OR lastname like %s;"
    cursor = cnx.cursor()
    cursor.execute(query, ('%'+string+'%', '%'+string+'%'))
    business_owner = []
    for (id,firstname, lastname, date_of_birth, email, phone) in cursor:
        business_owner.append(Business_Owner(id, firstname, lastname, date_of_birth, email, phone))
    cnx.commit()
    return business_owner

