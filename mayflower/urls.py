from django.urls import path
from mayflower import views

urlpatterns=[
    path('indexpage/', views.indexpage, name="indexpage"),
    path('adminpage/', views.adminpage, name="adminpage"),
    path('savedata/', views.savedata, name="savedata"),
    path('display/', views.display, name="display"),
    path('editpage/<int:dataid>/', views.editpage, name="editpage"),
    path('updatepage/<int:dataid>/', views.updatepage, name="updatepage"),
    path('deletepage/<int:dataid>/', views.deletepage, name="deletepage"),
    path('catpage/',views.catpage,name="catpage"),
    path('datasave/', views.datasave, name="datasave"),
    path('catdisplay/', views.catdisplay, name="catdisplay"),
    path('cateditpage/<int:dataid>/', views.cateditpage ,name="cateditpage"),
    path('catupdate/<int:dataid>/', views.catupdate, name="catupdate"),
    path('catdelete/<int:dataid>/', views.catdelete, name="catdelete"),
    path('icepage/', views.icepage, name="icepage"),
    path('icesave/', views.icesave, name="icesave"),
    path('icedisplay/',views.icedisplay,name="icedisplay"),
    path('iceedit/<int:dataid>/', views.iceedit, name="iceedit"),
    path('iceupdate/<int:dataid>/', views.iceupdate, name="iceupdate"),
    path('icedelete/<int:dataid>/', views.icedelete, name="icedelete"),
    path('adminloginpage/', views.adminloginpage, name="adminloginpage"),
    path('adminlog/', views.adminlog, name="adminlog"),
    path('cntdispage/', views.cntdispage, name="cntdispage")
]

