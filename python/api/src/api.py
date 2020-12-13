import flask, os , parseJson, AppointmentDAO
from flask_ipban import IpBan
from businessDAO import getBusinessById, setBusiness, deleteBusiness
from business_ownerDAO import setBusinessOwner, deleteBusinessOwner
from AppointmentDAO import deleteAppointmentByBusinessId
from flask import request, abort, send_file, jsonify
from qr import createQR,clear,Img
from parseJson import receiveBusinessJson, receiveBusinessOwnerJson, sendAppointmentByTokenJson

app = flask.Flask(__name__)

app.config["DEBUG"] = True

#If an ip make 10 bad request, it will be ban for 300 seconds
ip_ban = IpBan(app= app, ban_seconds=300, ban_count=10)

#this will check if an ip is in the blacklist and will automatically send a 403 forbidden
@app.before_request
def block_method():
    text_file = open('blacklist')
    ip_ban_list = text_file.readlines()
    ip = request.environ.get('REMOTE_ADDR')
    if ip in ip_ban_list:
        abort(403)

#Receives a json file that contains a business owner and send it to the database, return the id
@app.route('/post_business', methods = ['POST'])
def postBusiness():
    print (request.is_json)
    content = request.get_json()
    business = receiveBusinessJson(content)
    id = setBusiness(business)
    print(id)
    return id

#Receives a json file that contains a business owner and send it to the database, return the id
@app.route('/post_business_owner', methods = ['POST'])
def postBusinessOwner():
    print (request.is_json)
    content = request.get_json()
    businessOwner = receiveBusinessOwnerJson(content)
    id = setBusinessOwner(businessOwner)
    print(id)
    return id

#Will add an appointment on the database. receives a json file and return the token generated for the appointment
@app.route("/post_appointment", methods=["POST"])
def setAppointments():
    print (request.is_json)
    appointment = parseJson.reveiveAppointment(request.get_json())
    id = AppointmentDAO.setAppointment(appointment)
    return id

#this is the route to get the ip of the client (it can be used to block brute force attack or ddos)
@app.route("/get_ip", methods=["GET"])
def get_my_ip():
    response = jsonify({'ip': request.remote_addr})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


#this route will call the qr function made in the QrGenerator.py file, it will return a qr in png format to the client
@app.route('/ask_qr/<text>', methods=['GET'])
def askQR(text=None):
    image = createQR(text)
    try:
        result = send_file(image.dir, attachment_filename= 'qrcode.png')
        clear(image.dir)
        return result
    except Exception as e:
        return str(e)

#Will delete all the information od a business owner based on his owner id
@app.route("/delete_all_business/<business_id>", methods=["DELETE"])
def delete_all_business(business_id = None):
    business = getBusinessById(business_id)
    deleteAppointmentByBusinessId(business.id)
    deleteBusinessOwner(business.id_owner)
    deleteBusiness(business_id)
    return 'done'

#Will delete all the information od a business owner based on his owner id
@app.route("/delete_appointment/<appointment_id>", methods=["DELETE"])
def delete_appointment(appointment_id = None):
    AppointmentDAO.deleteAppointment(appointment_id)
    return 'done'


#Will send all the information about a business  based on his business id
@app.route("/get_business/<business_id>", methods=["GET"])
def get_business(business_id = None):
    json_file = parseJson.sendBusiness(business_id)
    return json_file

#Will send all the information about a business owner based on his owner id
@app.route("/get_business_owner/<owner_id>", methods=["GET"])
def getBusinessOwner(owner_id = None):
    json_file = parseJson.sendBusinessOwner(owner_id)
    return json_file

#Will send a json file back with all the appointments for a Business
@app.route("/get_appointments/<business_id>", methods=["GET"])
def getAppointments(business_id = None):
    json_file = parseJson.sendAppointmentJson(business_id)
    return json_file

#will send a json file back with an appointment searched with the token
@app.route("/get_appointment_by_token/<token>", methods=["GET"])
def getAppointmentByToken(token = None):
    appointment = sendAppointmentByTokenJson(token)
    return appointment

app.run("192.168.1.12")