#qr-code created using, [qrcode] module wth added other customizations to it, eg-: change in color and all

import qrcode 
from PIL import Image


qr_content=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4)

qr_content.add_data("github.com/karush2807")
qr_content.make(fit=True)

img=qr_content.make_image(fill_color="white", back_color="blue")
img.save("Github Profile.png")