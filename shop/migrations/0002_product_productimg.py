# Generated by Django 2.2.5 on 2021-05-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productimg',
            field=models.ImageField(null='True', upload_to='product'),
            preserve_default='True',
        ),
    ]
