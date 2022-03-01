from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .forms import contactform, customusercreationform
from .models import product



# Create your views here.
def home(request):
    return render(request, 'shop/home.html', {'title':"Home"})

    
def catalogue(request):
    products = product.objects.all()   
    return render(request, 'shop/catalogue.html', {'title':'Catalogue','lista':products})



def contact(request):
    
    if request.method == "POST":
        username = request.POST['username']
        useremail = request.POST['email'] 
        usermessage = useremail + " " +request.POST['issue']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['marceloct1986@gmail.com']
        send_mail(username,usermessage,email_from,recipient_list)      
        return render(request, 'issuesent.html' ,{'title':'Issue Sent'})
    else:
        myform = contactform()
    return render(request, 'shop/contact.html', {'title':"Contact us"})
        #myform = contactform(request.POST)
        #if myform.is_valid():
        #    forminfo = myform.cleaned_data()
        #    send_mail(forminfo['username'], forminfo['issue'], email_from,['marceloct1986@gmail.com'] )    
        #username = request.POST['username']
        #useremail = request.POST['email'] 
        #usermessage = useremail + " " +request.POST['issue']
        #email_from = settings.EMAIL_HOST_USER
        #recipient_list = ['marceloct1986@gmail.com']
        #send_mail(username,usermessage,email_from,recipient_list)      
        #return render(request, 'shop/issuesent.html' ,{'title':'Issue Sent'})
    #else:
    #data={
    #    'form': contactform()
    #    }
    #return render(request, 'shop/contact.html', data)


def signup(request):
    data= {
        'form':customusercreationform()
    }
    if request.method == "POST":
        formul = customusercreationform(data=request.POST)
        if formul.is_valid():
            formul.save()
            user = authenticate(username=formul.cleaned_data['username'],password=formul.cleaned_data['password1'])
            login(request,user)
            messages.success(request,"correctly registered")
            return redirect(to='home')
        data['form'] = formul
          
    return render(request, 'registration/signup.html', data)

def search(request):
    if request.GET["prd"]:
        productinp = request.GET["prd"]
        if len(productinp)>20:    
            message = "Nombre demasiado largo"
            return render(request,'shop/prodsearch.html',{"message":message}) 
        else:
            articles = product.objects.filter(productname__icontains=productinp) #SQL query con like productname = "productinp"
            return render(request, 'shop/prodsearch.html',{"articles":articles, "query":productinp})
    else:
        message = "Introduzca un artículo"
    return render(request,'shop/prodsearch.html',{"message":message})