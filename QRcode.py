# QR code Generator in python
# make ,save ,

import qrcode as qr
img=qr.make("https://dictionary.cambridge.org/")
img.save("eng_dict.png")

