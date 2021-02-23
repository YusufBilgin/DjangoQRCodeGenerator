from django.shortcuts import render, redirect
from shutil import copy
from .forms import GenerateQR
from .models import QRCode
import pyqrcode
import png
import os

# Create your views here.

def index(request):

    form = GenerateQR(request.POST or None)

    if form.is_valid():
        QR = form.save()

        # QR.id 

        qr_code = pyqrcode.create(QR.content)

        if QR.color == 'black':
            qr_color = (0, 0, 0, 255)
        elif QR.color == 'red':
            qr_color = (255, 0, 0, 255)
        elif QR.color == 'blue':
            qr_color = (0, 0, 255, 255)
        elif QR.color == 'green':
            qr_color = (0, 255, 0, 255)
        elif QR.color == 'brown':
            qr_color = (150, 75, 0, 255)
        elif QR.color == 'purple':
            qr_color = (128, 0, 128, 255)
        elif QR.color == 'pink':
            qr_color = (255, 192, 203, 255)
        elif QR.color == 'yellow':
            qr_color = (255, 255, 0, 255)
        elif QR.color == 'grey':
            qr_color = (128, 128, 128, 255)
        elif QR.color == 'light_blue':
            qr_color = (173, 216, 230, 255)
        else:
            qr_color = (0, 0, 0, 255)

        
        qr_code.png("{}.png".format(QR.id), scale=QR.scale, module_color=qr_color)
        copy("{}.png".format(QR.id), "static/")
        os.remove("{}.png".format(QR.id))

        qrcode = QRCode.objects.filter(id = QR.id).first()

        return render(request, 'index.html', {"qrcode": qrcode})
    
    return render(request, 'generateQR.html', {"form": form})



        