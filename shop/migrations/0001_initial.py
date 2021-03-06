# Generated by Django 2.2.5 on 2021-05-12 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=30)),
                ('productsection', models.CharField(max_length=30)),
                ('productprice', models.FloatField()),
                ('productstock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='productorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idorder', models.IntegerField()),
                ('usernameorder', models.CharField(max_length=30)),
                ('useridorder', models.IntegerField()),
                ('orderdate', models.DateField()),
                ('delivered', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('adress', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
