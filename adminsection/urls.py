from django.contrib import admin
from django.urls import path , include
from adminsection import views


urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('service/', views.addservice, name='addservices'),
    path('manageservices/', views.manageservices, name='manageservices'),
    path('updateservice/<int:id>/', views.updateservice, name='updateservice'),
    path('addcustomer/', views.addcustomer, name='addcustomer'),
    path('customerlist/', views.customerlist, name='customerlist'),
    path('editcustomer/<int:id>/', views.editcustomer, name='editcustomer'),
    path('assignservices/<int:id>/', views.assignservices, name='assignservices'),
    path('bwdatesreportsds/', views.bwdatesreportsds, name='bwdatesreportsds'),
    path('salesreports/', views.salesreports, name='salesreports'),
    path('allappointment/', views.allappointment, name='allappointment'),
    path('viewappointment/<int:id>/', views.viewappointment, name='viewappointment'),
    path('newappointment/', views.newappointment, name='newappointment'),
    path('acceptedappointment/', views.acceptedappointment, name='acceptedappointment'),
    path('rejectedappointment/', views.rejectedappointment, name='rejectedappointment'),
    path('invoices/', views.invoices, name='invoices'),
    path('viewinvoice/<int:id>', views.viewinvoice, name='viewinvoice'),
    path('searchappointment/', views.searchappointment, name='searchappointment'),
    path('searchinvoices/', views.searchinvoices, name='searchinvoices'),
    path('adminprofile/', views.profile, name='profile'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('forgetpassword/', views.forgetpassword, name='forgetpassword'),
    path('contactus/', views.contactus, name='contactus'),
    path('logout/', views.logout, name='logout'),
    # path('allappointment/', views.allappointment, name='allappointment'),
    # path('newappointment/', views.newappointment, name='addservices'),
    # path('acceptedappointment/', views.acceptedappointment, name='acceptedappointment'),
]
