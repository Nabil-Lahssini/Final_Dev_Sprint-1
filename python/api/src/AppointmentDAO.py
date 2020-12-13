from connection import connect
from Entity.appointment import Appointment
from idGenerator import generateId
from encrypt import encrypt
from decrypt import decrypt
import idGenerator, secrets

cnx = connect()

def validateAppointment(token):
    query = "UPDATE appointment SET done = 2 WHERE token = %s"
    cursor = cnx.cursor()
    cursor.execute(query, (token , ))
    cnx.commit()

def setAppointment(p):
    query = "INSERT INTO appointment VALUES (%s,%s,%s,%s,%s,%s,%s,%s, NULL);"
    cursor = cnx.cursor()
    token = generateAppointmentToken()
    cursor.execute(query, (generateId() ,encrypt(p.firstname), encrypt(p.lastname), encrypt(p.email), encrypt(p.begin_date), encrypt(p.end_date), p.business_id, token))
    cnx.commit()
    return token

def getAppointmentById(id):
    query = "SELECT * FROM appointment WHERE id = %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    for (id, firstname, lastname, email, begin_date, end_date, business_id, token, done) in cursor:
        appointment = Appointment(id, decrypt(firstname), decrypt(lastname), decrypt(email), decrypt(begin_date), decrypt(end_date), business_id, token)
    cnx.commit()
    return appointment

def getAppointmentByToken(token):
    query = "SELECT * FROM appointment WHERE token = %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (token, ))
    for (id, firstname, lastname, email, begin_date, end_date, business_id, token, done) in cursor:
        appointment = Appointment(id, decrypt(firstname), decrypt(lastname), decrypt(email), decrypt(begin_date), decrypt(end_date), business_id, token)
    cnx.commit()
    return appointment

def getAppointmentByBusinessId(id):
    query = "SELECT * FROM appointment WHERE business_id = %s;"
    cursor = cnx.cursor()
    cursor.execute(query, (id, ))
    appointment = []
    for (id, firstname, lastname, email, begin_date, end_date, business_id, token, done) in cursor:
        appointment.append(Appointment(id, decrypt(firstname), decrypt(lastname), decrypt(email), decrypt(begin_date), decrypt(end_date), business_id, token))
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
    query = "UPDATE appointment SET `firstname`=%s,`lastname`=%s,`email`=%s,`begin_date`=%s,`end_date`=%s,`business_id`=%s WHERE id = %s"
    cursor = cnx.cursor()
    cursor.execute(query, (encrypt(p.firstname), encrypt(p.lastname), encrypt(p.email) ,encrypt(p.begin_date) ,encrypt(p.end_date),p.business_id, p.id))
    cnx.commit()

def generateAppointmentToken():
    lines = idGenerator.checkFile()
    token = secrets.token_hex(24)
    tokend = token + '\n'
    while tokend in lines:
        token = secrets.token_hex(24)
        tokend = token + '\n'
    idGenerator.appendFile(tokend)
    return token


setAppointment(Appointment(0, 'Nabil', 'Lahssini', 'NabilLahssini@gmail.com', '13/12/2020 16:00', '13/12/2020 17:00', '6ca2d5419eacdb08', generateAppointmentToken()))