# Generated by Django 4.1.7 on 2023-04-08 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='disease_Img',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='Media/'),
        ),
    ]
