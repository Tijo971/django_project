from django.urls import path
from webfashion import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('product/<cat_nme>', views.product, name='product'),
    path('singleproduct/<int:dataid>', views.singleproduct, name='singleproduct'),
    path('cart/', views.cart, name='cart'),
    path('', views.userlogin, name='userlogin'),
    path('usersignin/', views.usersignin, name='usersignin'),
    path('loginproces/', views.loginproces, name='loginproces'),
    path('savecart/', views.savecart, name='savecart'),
    path('checkout/', views.checkout, name='checkout'),
    path('storecheckout/', views.storecheckout, name='storecheckout'),
]