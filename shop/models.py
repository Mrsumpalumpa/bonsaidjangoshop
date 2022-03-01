from django.db import models
from django import forms

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    adress = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return ("Name: %s -- Email: %s"%(self.username,self.email))


class product(models.Model):
    productname = models.CharField(max_length=30)
    productsection = models.CharField(max_length=30)
    productprice = models.FloatField()
    productstock= models.IntegerField()
    productimg = models.ImageField(upload_to="product",null="True")

    def __str__(self):
        return ("Name: %s -- Section: %s"%(self.productname,self.productsection))


class productorder(models.Model):
    idorder = models.IntegerField()
    usernameorder = models.CharField(max_length=30)
    useridorder = models.IntegerField()
    orderdate = models.DateField()
    delivered = models.BooleanField()

    def __str__(self):
        return "Order ID: %s -- Delivered %s"%(self.idorder,self.delivered)

#Form contact
optconsult=[[0,"Consulta"],[1,"Reclamación"],[2,"Sugerencia"],[3,"Información"]]
class contact(models.Model):
    contactname =models.CharField(max_length=30)
    contactemail=models.EmailField()
    contactissuetype = models.IntegerField(choices=optconsult)
    contactmessage = models.TextField()

    #def __str__():
    #    return (self.contactname)