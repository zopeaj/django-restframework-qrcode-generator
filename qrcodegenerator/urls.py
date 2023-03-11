from django.urls import path, include
from qrcodegenerator.views import create_or_get_qrcode, generateQrCodeData

urlpatterns = [
    path('generateQrCode/', create_or_get_qrcode),
    path('generateQrCode/<str:filename>/', create_or_get_qrcode),
    path('generateQrCode/', generateQrCodeData)
]
