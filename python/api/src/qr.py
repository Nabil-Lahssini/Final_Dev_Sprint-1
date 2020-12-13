import qrcode
import os
import pathlib
from datetime import date



#generate a little class to return 2 values easily
class Img: 
    def __init__(self, dir, img): 
        self.dir = dir
        self.qr = img 

 

#function that will save a QR code using the qr library to a png
def createQR(content):
    img = qrcode.make(content)
    dir = str(pathlib.Path().absolute())+'/temp/qr/data-'+content+str(date.today())+'.png'
    img.save(dir)
    imqg = Img(dir, img)
    return imqg

createQR("us")

#function to delete a file
def clear(dir):
    os.remove(dir)