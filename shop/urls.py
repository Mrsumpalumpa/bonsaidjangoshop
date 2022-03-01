from django.urls import path
from .views import home,catalogue,login,signup,contact,search

urlpatterns=[
    path('', home, name='home' ),
    path('catalogue/', catalogue, name='catalogue' ),
    #path('login/', login, name='login' ),
    path('signup/', signup, name='signup' ),
    path('contact/', contact, name='contact' ),    
    path('catalogue/search/', search, name ='search'),
]