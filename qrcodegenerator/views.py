from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorator_csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.decorator.views import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from qrcodeServices import QRCodeService


qrcodeService = QRCodeService()

@csrf_exempt
def create_or_get_qrcode(request):
    """
    Generate qr code
    """
    if request.method == "GET":
        filename = request.path.get("filename")
        if filename is None:
            content = qrcodeService.lookupQrCodePngs(filename)
            return Response(data=content, status=status.HTTP_200_OK, content_type="image/png")
        return Response(data={"detail": f"{filename} not found"}, status=status.HTTP_NOT_FOUND, content_type="application/json")

    elif request.method == "POST":
        data = JSONParser().parse(request)
        filename = data.get("filename")
        datatoencode = data.get("datatoencode")
        scalenumber = data.get("scalenumber")
        if filename is not None:
            filenamedata = qrcodeService.generateQrCodePngs(filename, datatoencode, scalenumber)
            content = qrcodeService.lookupQrCodePngs(filenamedata)
            return Response(data=content, status=status.HTTP_200_OK, content_type="image/png")

        filedata = qrcodeService.generateQrCodePngs(None, datatoencode, scalenumber)
        contents = qrcodeService.lookupQrCodePngs(filedata)
        return Response(data=content, status=status.HTTP_200_OK, content_type="image/png")

@csrf_exempt
@api_view(['GET'])
def generateQrCodeData(request):
    """
    Generate code Automatically
    """
    if request.method == "GET":
        datatoencode = request.query_params.get("datatoencode")
        scalenumber = request.query_params.get("scale")
        filename = request.query_params.get("filename")
        if filename is not None:
            filenamedata = qrcodeService.generateQrCodePngs(filename, datatoencode, scalenumber)
            content = qrcodeService.lookupQrCodePngs(filenamedata)
            return Response(data=content, status=status.HTTP_200_OK, content_type="image/png")

        filedata = qrcodeService.generateQrCodePngs(None, datatoencode, scalenumber)
        contents = qrcodeService.lookupQrCodePngs(filedata)
        return Response(data=content, status=status.HTTP_200_OK, content_type="image/png")


# POST: http://127.0.0.1:8000/generateqrcode/
# GET: http://127.0.0.1:8000/generateqrcode/{filename}
# GET: http://127.0.0.1:8000/generateqrcode/?datatoencode=&scale=8&filename=qrcodegenerator

