from connection import connect
from Entity.appointment import Appointment

cnx = connect()

def setAppointment(p):
    query = "INSERT INTO `appointment` VALUES (NULL,%s,%s,%s,%s,%s,%s);"
    cursor = cnx.cursor()
    cursor.execute(query, (p.id, p.firstname, p.lastname, p.email, p.date, p.hour, p.business_id))
    cnx.commit()
    cnx.close()
    return cursor.lastrowid

def getAppointmentById(id):
    query = "SELECT * FROM `appointment` WHERE id = %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    for (id, firstname, lastname, email, date, hour, business_id) in cursor:
        appointment = Appointment(id, firstname, lastname, email, date, hour, business_id)
    cnx.commit()
    cnx.close()
    return appointment
# print(getAppointmentById(2).firstname)

# def updateAppointment(p):
#     query = "UPDATE `appointment` SET (NULL,%s,%s,%s,%s,%s,%s = WHERE 1)"
#     cursor = cnx.cursor()
#     cursor.execute(query, (p.id, p.firstname, p.lastname, p.email, p.date, p.hour, p.business_id))
#     cnx.commit()
#     cnx.close()
    
    

