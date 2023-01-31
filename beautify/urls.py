"""beautify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from beautyapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.index, name='index'),
     path('login', views.login, name='login'),
     path('parlour', views.parlour, name='parlour'),
     path('customer', views.customer, name='customer'),

     path('adminhome', views.adminhome, name='adminhome'),
     path('adminparlour', views.adminparlour, name='adminparlour'),
     path('updateuser', views.updateuser, name='updateuser'),
     path('admincustomer', views.admincustomer, name='admincustomer'),
     path('adminfeedback', views.adminfeedback, name='adminfeedback'),

     path('parlourhome', views.parlourhome, name='parlourhome'),
     path('parlourcategory', views.parlourcategory, name='parlourcategory'),
     path('deletecat', views.deletecat, name='deletecat'),
     path('parlourtreatment', views.parlourtreatment, name='parlourtreatment'),
     path('deltreatment', views.deletetreatment, name='deletetreatment'),
     path('parlourpackage', views.parlourpackage, name='parlourpackage'),
     path('delpackage', views.delpackage, name='delpackage'),
     path('selectpackage', views.selectpackage, name='selectpackage'),
     path('viewpackage', views.viewpackage, name='viewpackage'),
     path('parlouroffer', views.parlouroffer, name='parlouroffer'),
     path('selectoffer', views.selectoffer, name='selectoffer'),
     path('viewoffer', views.viewoffer, name='viewoffer'),
     path('parlourbooking', views.parlourbooking, name='parlourbooking'),
     path('updatebooking', views.updatebooking, name='updatebooking'),
     path('parlourfeedback', views.parlourfeedback, name='parlourfeedback'),

     path('customerhome', views.customerhome, name='customerhome'),
     path('customerofferdetails', views.customerofferdetails, name='customerofferdetails'),
     path('customerchoosedate', views.customerchoosedate, name='customerchoosedate'),
     path('customerbooking', views.customerbooking, name='customerbooking'),
     path('customerparlour', views.customerparlour, name='customerparlour'),
     path('customerparlourmore', views.customerparlourmore, name='customerparlourmore'),
     path('customertreatment', views.customertreatment, name='customertreatment'),
     path('customerpackage', views.customerpackage, name='customerpackage'),
     path('customerpackagedetails', views.customerpackagedetails, name='customerpackagedetails'),
     path('customerrate', views.customerrate, name='customerrate'),
]
