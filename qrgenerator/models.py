from django.db import models

# Create your models here.

SCALE_OPTIONS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
)

COLOR_OPTIONS = (
    ('black', 'siyah'),
    ('red', 'kırmızı'),
    ('blue', 'mavi'),
    ('green', 'yeşil'),
    ('brown', 'kahverengi'),
    ('purple', 'mor'),
    ('pink', 'pembe'),
    ('yellow', 'sarı'),
    ('grey', 'gri'),
    ('light_blue', 'açık mavi'),
)

OUTPUT_OPTIONS = (
    ('SVG', 'SVG'),
    ('EPS', 'EPS'),
    ('PNG', 'PNG'),
)

class QRCode(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    content = models.CharField(max_length=500, verbose_name='QR Kod içeriği')
    scale = models.CharField(blank = False, null = False, max_length=2, choices=SCALE_OPTIONS, default=5)
    color = models.CharField(blank = False, null = False, max_length=15, choices=COLOR_OPTIONS, default='black')