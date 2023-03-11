import pyqrcode
from uuid import uuid4

class QRCodeService:
    def __init__(self):
        self.scale = 9
        self.encodingFormat = ['alphanumeric', 'numeric', 'alphabet', 'binary']
        self.filename = f'{uuid4().hex}.png'

    def generateQrCodePng(self, data, encoding, path):
        value = encoding in self.encodingFormat
        if not value:
            print(f"{encoding} format not found")

        qrcode = pyqrcode.create(data, error='L', version=27, mode=encoding)
        qrcode.png(path, scale=self.scale)

    def generateQrCodeSvg(self, data, encoding, path):
        value = encoding in self.encodingFormat
        if not value:
            print(f"{encoding} format not found")
        qrcode = pyqrcode.create(data, error='L', version=27, mode=encoding)
        qrcode.svg(path, scale=self.scale)

    def generateQrCodeEps(self, data, encoding, path):
        value = encoding in self.encodingFormat
        if not value:
            print(f"{encoding} format not found")
        qrcode = pyqrcode.create(data, error='L', version=27, mode=encoding)
        qrcode.eps(path, scale=self.scale)

    def generateQrCodePngs(self, filename, datatoencode, scalenumber):
        filenamedata = f'{filename}.png'
        qrcode_data = pyqrcode.create(datatoencode)
        qrcode_data.png(filenamedata, scalenumber)
        return filenamedata

    def lookupQrCodePngs(self, filename):
        with open(filename, mode='rb') as f:
            content = f.read()
            return content


# qrcodeService = GeneratePyqrcode()
# filenamedata = qrcodeService.generateQrCodePngs("qrcodefile", uuid4().hex, 8)
# print(filenamedata)


