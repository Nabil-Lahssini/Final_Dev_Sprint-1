from connection import connect
from Entity.appointment import Appointment
from idGenerator import generateId
from encrypt import encrypt
from decrypt import decrypt

cnx = connect()

def setAppointment(p):
    query = "INSERT INTO appointment VALUES (%s,%s,%s,%s,%s,%s,%s);"
    cursor = cnx.cursor()
    cursor.execute(query, (generateId() ,encrypt(p.firstname), encrypt(p.lastname), encrypt(p.email), encrypt(p.date), encrypt(p.hour), encrypt(p.business_id)))
    cnx.commit()
    return cursor.lastrowid

def getAppointmentById(id):
    query = "SELECT * FROM appointment WHERE id = %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    for (id, firstname, lastname, email, date, hour, business_id) in cursor:
        appointment = Appointment(id, decrypt(firstname), decrypt(lastname), decrypt(email), decrypt(date), decrypt(hour), decrypt(business_id))
    cnx.commit()
    return appointment

def getAppointmentByBusinessId(id):
    query = "SELECT * FROM appointment WHERE business_id = %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    appointment = []
    for (id, firstname, lastname, email, date, hour, business_id) in cursor:
        appointment.append(Appointment(id, decrypt(firstname), decrypt(lastname), decrypt(email), decrypt(date), decrypt(hour), decrypt(business_id)))
    cnx.commit()
    return appointment

def deleteAppointment(id):
    query = "DELETE FROM appointment where id = %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    cnx.commit()

def deleteAppointmentByBusinessId(id):
    query = "DELETE FROM appointment where business_id = %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    cnx.commit()

def updateAppointment(p):
    query = "UPDATE appointment SET `firstname`=%s,`lastname`=%s,`email`=%s,`date`=%s,`hour`=%s,`business_id`=%s WHERE id = %s"
    cursor = cnx.cursor()
    cursor.execute(query, (encrypt(p.firstname), encrypt(p.lastname), encrypt(p.email) ,encrypt(p.date) ,encrypt(p.hour), encrypt(p.business_id), p.id))
    cnx.commit()
