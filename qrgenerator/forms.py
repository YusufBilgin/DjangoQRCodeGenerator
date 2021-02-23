from django import forms
from .models import QRCode

class GenerateQR(forms.ModelForm):
    class Meta:
        model = QRCode
        fields = [
            'content',
            'scale',
            'color'
        ]

