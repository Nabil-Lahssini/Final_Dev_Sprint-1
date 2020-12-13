from flask import jsonify
import businessDAO, json, business_ownerDAO
from Entity.business import Business
from Entity.appointment import Appointment
from Entity.business_owner import Business_Owner
from AppointmentDAO import getAppointmentByBusinessId, getAppointmentByToken
from Entity.appointment import Appointment

#Converts a json file that contains a business to a business object
def receiveBusinessJson(json_file):
    business = Business(0, json_file["business_type"], json_file["name"],json_file["appointment_time"],json_file["country"],json_file["city"],json_file["code"],json_file["street"],json_file["house_nr"],  json_file["email"],json_file["phone"],json_file["id_owner"])
    return business

#Converts an array of appointments retrieved in the database with on the business id to a JSON file
def sendAppointmentJson(business_id):
    array_appointments = getAppointmentByBusinessId(business_id)
    jso = []
    for app in array_appointments:
        js = {"id":app.id,"title": app.firstname + ' '+app.lastname, "begin" : app.begin_date, "end" : app.end_date}
        jso.append(js)
    result = json.dumps(jso)
    return result

#Converts an array of appointments retrieved in the database with on the token to a JSON file
def sendAppointmentByTokenJson(token):
    app = getAppointmentByToken(token)
    jso = []
    js = {"id":app.id,"title": app.firstname + ' '+app.lastname, "begin" : app.begin_date, "end" : app.end_date}
    result = json.dumps(js)
    return result

#Converts a received json file that contains an appointment to a appointment object
def reveiveAppointment(json_file):
    appointment = Appointment(0,json_file["firstname"],json_file["lastname"], json_file["email"], json_file["begin_date"], json_file["end_date"], json_file["business_id"], 0)
    return appointment

#will return a json file with data of the business
def sendBusiness(business_id):
    b = businessDAO.getBusinessById(business_id)
    js = {"business_id":business_id,
    "business_type":b.business_type,
    "name":b.name,
    "appointment_time":b.appointment_time,
    "country":b.country,
    "city":b.city,
    "code":b.code,
    "street":b.street,
    "house_nr":b.house_nr,
    "email":b.email,
    "phone":b.phone,
    "id_owner":b.id_owner
    }
    result = json.dumps(js)
    return result

#will return a json file with data of the business_owner
def sendBusinessOwner(owner_id):
    b=business_ownerDAO.getBusinessOwnerById(owner_id)
    js = {"id":owner_id,
    "firstname":b.firstname,
    "lastname":b.lastname,
    "date_of_birth":b.date_of_birth,
    "email":b.email,
    "phone":b.phone
    }
    result = json.dumps(js)
    return result

#Converts a json object that contains the data of a business owner to a business owner object
def receiveBusinessOwnerJson(json_file):
    business_owner = Business_Owner('0', json_file["firstname"], json_file["lastname"], json_file["date_of_birth"], json_file["email"], json_file["phone"])
    return business_owner
# {
#     "business_type" : "",
#     "name" : "",
#     "appointment_time" : "",
#     "country" : "",
#     "city" : "",
#     "code" : "",
#     "street": "",
#     "house_nr": "",
#     "email" : "",
#     "phone" : "",
#     "id_owner" : ""
# }

#appointment
# {
#     "firstname" : 
#     "lastname" : 
#     "email" : 
#     "begindate":
#     "enddate":
#     "business_id":
# }

# {
#     "firstname" : "",
#     "lastname" : "",
#     "date_of_birth" : "",
#     "email" : "",
#     "phone" : ""
# }
# {"id":"1",
# "start":"2020-12-11 15:56:00"
# ,"end":"2020-12-11 18:00:00"
# ,"title":"omer",
# "created_at":"2020-12-10 12:56:53",
# "updated_at":"2020-12-10 12:56:53"
# }
# country, city, zipcode, street, number