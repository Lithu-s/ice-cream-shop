from django.urls import path
from mayflowerweb import views


urlpatterns=[
    path('', views.homepage, name="homepage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('discategory/<itemcatg>', views.discategory, name="discategory"),
    path('icecredetails/<int:dataid>/', views.icecredetails, name="icecredetails"),
    path('pagelogin/', views.pagelogin, name="pagelogin"),
    path('logindata/', views.logindata, name="logindata"),
    path('registerdata', views.registerdata, name="registerdata"),
    path('logout/', views.logout, name="logout"),
    path('cntsave/', views.cntsave, name="cntsave"),


]