# Generated by Django 3.2 on 2022-03-17 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_auto_20220316_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='docfile',
            field=models.FileField(blank=True, null=True, upload_to='case_<built-in function id>/documents/'),
        ),
    ]
