import pyqrcode
import png
from pyqrcode import QRCode
  
def GenerateQR(URL):  
    url = "https://" + URL
    url = pyqrcode.create(URL)
    url.png("BizzyCard/BizzyCardApp/static/media/BizzyCardApp/QRs/" + URL + ".png", scale = 8)

GenerateQR("lttstore.com")
