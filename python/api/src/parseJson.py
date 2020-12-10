from flask import jsonify
from Entity.business import Business

def receiveBusinessJson(json_file):
    business = Business(0, json_file.business_type, json_file.name, json_file.address, json_file.appointment_time, json_file.email, json_file.phone, json_file.id_owner)
    return business







# {
#     "business_type" : "",
#     "name" : "",
#     "appointment_time" : "",
#     "city" : "",
#     "code" : "",
#     "street": "",
#     "house_nr": "",
#     "email" : "",
#     "phone" : "",
#     "id_owner" : ""
# }