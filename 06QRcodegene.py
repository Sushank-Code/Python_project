import qrcode as qr
from PIL import Image

feature= qr.QRCode(version=1,box_size=40,border=3)
feature.add_data('https://www.w3schools.com/python/python_functions.asp')
feature.make(fit=True)

img = feature.make_image(fill_color="red",back_color="blue")
img.save("Myqr4.png")
