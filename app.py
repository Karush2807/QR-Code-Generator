#modules imported for generating QR code
import pyqrcode
import png
from pyqrcode import QRCode

#enter the link/text which u have to store!!
s="https://www.linkedin.com/in/arush-karnatak-894bb52a1/"

#generate QR code
url=pyqrcode.create(s)

#creating and saving the file in .png format
url.png('myqr.png',scale=8)

