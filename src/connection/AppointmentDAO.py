from connection import connect
from Entity.appointment import Appointment

cnx = connect()

def setAppointment(p):
    query = "INSERT INTO appointment VALUES (NULL,%s,%s,%s,%s,%s,%s);"
    cursor = cnx.cursor()
    cursor.execute(query, (p.id, p.firstname, p.lastname, p.email, p.date, p.hour, p.business_id))
    cnx.commit()
    return cursor.lastrowid

def getAppointmentById(id):
    query = "SELECT * FROM appointment WHERE id = %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    for (id, firstname, lastname, email, date, hour, business_id) in cursor:
        appointment = Appointment(id, firstname, lastname, email, date, hour, business_id)
    cnx.commit()
    return appointment

def getAppointmentBySearch(term):
    query = "SELECT * FROM appointment WHERE id LIKE %s OR firstname LIKE %s OR lastname LIKE %s OR business_id LIKE %s;"
    cursor = cnx.cursor()
    cursor.execute(query, ('%'+term+'%', '%'+term+'%', '%'+term+'%', '%'+term+'%'))
    appointment = []
    for (id, firstname, lastname, email, date, hour, business_id) in cursor:
        appointment.append(Appointment(id, firstname, lastname, email, date, hour, business_id))
    cnx.commit()
    return appointment

def deleteAppointment(id):
    query = "DELETE FROM appointment where id = %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    cnx.commit()

def updateAppointment(p):
    query = "UPDATE appointment SET `firstname`=%s,`lastname`=%s,`email`=%s,`date`=%s,`hour`=%s,`business_id`=%s WHERE id = %s"
    cursor = cnx.cursor()
    cursor.execute(query, (p.firstname, p.lastname, p.email ,p.date ,p.hour, p.business_id, p.id))
    cnx.commit()
