# Generated by Django 2.1.7 on 2019-02-25 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0002_auto_20190225_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualification',
            name='certified_identity_document',
            field=models.FileField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='certified_metric_certificate',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
