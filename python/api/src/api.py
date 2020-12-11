import flask, os , parseJson
from flask_ipban import IpBan
from businessDAO import getBusinessById, setBusiness, deleteBusiness
from business_ownerDAO import setBusinessOwner, deleteBusinessOwner
from AppointmentDAO import deleteAppointmentByBusinessId
from flask import request, abort, send_file, jsonify
from qr import createQR,clear,Img
from parseJson import receiveBusinessJson, receiveBusinessOwnerJson

app = flask.Flask(__name__)

app.config["DEBUG"] = True

ip_ban = IpBan(app= app, ban_seconds=300, ban_count=10)

#this will check if an ip is in the blacklist and will automatically send a 403 forbidden
@app.before_request
def block_method():
    text_file = open('blacklist')
    ip_ban_list = text_file.readlines()
    ip = request.environ.get('REMOTE_ADDR')
    if ip in ip_ban_list:
        abort(403)

#to et a json file and send it to the database, return the id
@app.route('/postBusiness', methods = ['POST'])
def postBusiness():
    print (request.is_json)
    content = request.get_json()
    business = receiveBusinessJson(content)
    id = setBusiness(business)
    print(id)
    return id

#to et a json file and send it to the database, return the id
@app.route('/postBusinessOwner', methods = ['POST'])
def postBusinessOwner():
    print (request.is_json)
    content = request.get_json()
    businessOwner = receiveBusinessOwnerJson(content)
    id = setBusinessOwner(businessOwner)
    print(id)
    return id

#this is the route to get the ip of the client (it can be used to block brute force attack or ddos)
@app.route("/get_ip", methods=["GET"])
def get_my_ip():
    response = jsonify({'ip': request.remote_addr})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


#this route will call the qr function made in the QrGenerator.py file, it will return a qr in png format to the client
@app.route('/askQR/<text>', methods=['GET'])
def getn(text=None):
    image = createQR(text)
    try:
        result = send_file(image.dir, attachment_filename= 'qrcode.png')
        clear(image.dir)
        return result
    except Exception as e:
        return str(e)

@app.route("/delete_all_business/<business_id>", methods=["DELETE"])
def delete_all_business(id = None):
    business = getBusinessById(id)
    deleteAppointmentByBusinessId(business.id)
    deleteBusinessOwner(business.id_owner)
    deleteBusiness(id)
    return True

@app.route("/getBusiness/<business_id>", methods=["GET"])
def get_business(business_id = None):
    json_file = parseJson.sendBusiness(business_id)
    return json_file

@app.route("/getBusinessOwner/<owner_id>", methods=["GET"])
def getBusinessOwner(owner_id = None):
    json_file = parseJson.sendBusinessOwner(owner_id)
    return json_file

app.run("192.168.1.12")