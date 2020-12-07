import flask
import os
from flask import request
from flask import send_file
from flask import jsonify
from src.qr import createQR,clear
from src.qr import Img

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#this is the route to get the ip of the client (it can be used to block brute force attack or ddos)
@app.route("/get_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200



#this route will call the qr function made in the QrGenerator.py file, it will return a qr in png format to the client
@app.route('/askQR/<text>', methods=['GET'])
def getn(text=None):
    image = createQR(text)
    try:
        result = send_file(image.dir, attachment_filename= 'qrcode.png')
        #clear(image.dir)
        return result
    except Exception as e:
        return str(e)


app.run()