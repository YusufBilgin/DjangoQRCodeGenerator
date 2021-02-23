# Generated by Django 3.0.7 on 2020-09-13 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrgenerator', '0002_qrcode_output_format'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qrcode',
            name='background_color',
        ),
        migrations.RemoveField(
            model_name='qrcode',
            name='output_format',
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='color',
            field=models.CharField(choices=[('black', 'siyah'), ('red', 'kırmızı'), ('blue', 'mavi'), ('green', 'yeşil'), ('brown', 'kahverengi'), ('purple', 'mor'), ('pink', 'pembe'), ('yellow', 'sarı'), ('grey', 'gri'), ('light_blue', 'açık mavi')], max_length=15),
        ),
    ]