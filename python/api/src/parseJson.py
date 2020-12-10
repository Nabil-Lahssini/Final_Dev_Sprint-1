from flask import jsonify
from Entity.business import Business
from Entity.appointment import Appointment
from Entity.business_owner import Business_Owner
from AppointmentDAO import getAppointmentByBusinessId
from Entity.appointment import Appointment

def receiveBusinessJson(json_file):
    business = Business(0, json_file["business_type"], json_file["name"],json_file["appointment_time"],json_file["country"],json_file["city"],json_file["code"],json_file["street"],json_file["house_nr"],  json_file["email"],json_file["phone"],json_file["id_owner"])
    return business

def sendAppointments(business_id):
    appointment = getAppointmentByBusinessId(business_id)
    appointment_array = []
    #for app in appointment:

def receiveBusinessOwnerJson(json_file):
    business_owner = Business_Owner('0', json_file["firstname"], json_file["lastname"], json_file["date_of_birth"], json_file["email"], json_file["phone"])
    return business_owner

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