import qrcode

data = 'This is my QRCode'

img = qrcode.make(data)

img.save()