from django.urls import path
from myfashion import views


urlpatterns = [
    path('index/',views.index, name='index'),
    path('addcategory/',views.addcategory, name='addcategory'),
    path('categorylist/',views.categorylist, name='categorylist'),
    path('addproducts/',views.addproducts, name='addproducts'),
    path('productlist/',views.productlist, name='productlist'),
    path('savecategory/',views.savecategory, name='savecategory'),
    path('saveproduct/',views.saveproduct, name='saveproduct'),
    path('editcategory/<int:dataid>/',views.editcategory, name='editcategory'),
    path('updatecategory/<int:dataid>/',views.updatecategory, name='updatecategory'),
    path('deletecategory/<int:dataid>/',views.deletecategory, name='deletecategory'),
    path('editproduct/<int:dataid>/',views.editproduct, name='editproduct'),
    path('updateproduct/<int:dataid>/',views.updateproduct, name='updateproduct'),
    path('deleteproduct/<int:dataid>/',views.deleteproduct, name='deleteproduct'),
    path('',views.adminlogin, name='adminlogin'),
    path('loginprocess/',views.loginprocess, name='loginprocess'),
]