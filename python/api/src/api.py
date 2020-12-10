import flask, os 
from flask_ipban import IpBan
from businessDAO import getBusinessById, setBusiness
from flask import request, abort, send_file, jsonify
from qr import createQR,clear,Img
from parseJson import receiveBusinessJson

app = flask.Flask(__name__)

app.config["DEBUG"] = True

ip_ban = IpBan(app= app, ban_seconds=300, ban_count=10)

@app.before_request
def block_method():
    text_file = open('blacklist')
    ip_ban_list = text_file.readlines()
    ip = request.environ.get('REMOTE_ADDR')
    if ip in ip_ban_list:
        abort(403)

@app.route('/postBusiness', methods = ['POST'])
def postJsonHandler():
    print (request.is_json)
    content = request.get_json()
    business = receiveBusinessJson(content)
    id = setBusiness(business)
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

@app.route("/get_business/<id>", methods=["GET"])
def get_business(id = None):
    b = getBusinessById(id)
    response = jsonify({'name': b.name})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

app.run("192.168.1.12")