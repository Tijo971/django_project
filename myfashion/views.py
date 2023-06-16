from django.shortcuts import render, redirect
from myfashion.models import Category, Products
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

def index(arg):
    return render(arg, 'index.html')

def addcategory(arg):
    return render(arg, 'add_category.html')

def categorylist(arg):
    data = Category.objects.all()
    return render(arg, 'category_list.html',{'data':data})

def addproducts(arg):
    data = Category.objects.all()
    return render(arg, 'add_product.html', {'data':data})

def productlist(arg):
    pro = Products.objects.all()
    return render(arg, 'product_lists.html', {'pro':pro})

def savecategory(arg):
    if arg.method == 'POST':
        c_name = arg.POST.get('cat_name')
        des = arg.POST.get('cat_des')
        img = arg.FILES['imge']
        obj = Category(cate_name=c_name, description=des, image=img)
        obj.save()
        messages.success(arg,"category saved successful")
        return redirect(addcategory)

def saveproduct(arg):
    if arg.method == 'POST':
        p_cat = arg.POST.get('p_category')
        p_nme = arg.POST.get('pro_name')
        p_pri = arg.POST.get('pro_price')
        p_des = arg.POST.get('pro_des')
        p_bran = arg.POST.get('pro_brand')
        image = arg.FILES['imge']
        obj = Products(p_category=p_cat, prod_name=p_nme, prod_price=p_pri, prod_description=p_des, prod_brand=p_bran, image=image)
        obj.save()
        return redirect(addproducts)

def editcategory(arg, dataid):
    data = Category.objects.get(id=dataid)
    cat = Category.objects.all()
    return render(arg, 'edit_category.html', {'data':data, 'cat':cat})


def updatecategory(arg, dataid):
    if arg.method == 'POST':
        c_name = arg.POST.get('c_category')
        des = arg.POST.get('cat_des')
        try:
            img = arg.FILES['imge']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Category.objects.get(id=dataid).image
        Category.objects.filter(id=dataid).update(cate_name=c_name, description=des, image=file)
        return redirect(categorylist)

def deletecategory(arg, dataid):
    data=Category.objects.filter(id=dataid)
    data.delete()
    return redirect(categorylist)

def editproduct(arg, dataid):
    data = Products.objects.get(id=dataid)
    cat = Category.objects.all()
    return render(arg, 'edit_product.html',{'data':data, 'cat':cat})

def updateproduct(arg, dataid):
    if arg.method == 'POST':
        p_cat = arg.POST.get('p_category')
        p_nme = arg.POST.get('pro_name')
        p_pri = arg.POST.get('pro_price')
        p_des = arg.POST.get('pro_des')
        p_bran = arg.POST.get('pro_brand')
        try:
            img = arg.FILES['imge']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Products.objects.get(id=dataid).image
        Products.objects.filter(id=dataid).update(p_category=p_cat, prod_name=p_nme, prod_price=p_pri, prod_description=p_des, prod_brand=p_bran, image=file)
        return redirect(productlist)


def deleteproduct(arg, dataid):
    data = Products.objects.filter(id=dataid)
    data.delete()
    return redirect(productlist)

def adminlogin(arg):
    return render(arg, 'admin_login.html')

def loginprocess(arg):
    if arg.method == 'POST':
        uname=arg.POST.get('unme')
        pwd = arg.POST.get('passwd')
        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(arg,user)
                messages.success(arg, "Login Successful")
                return redirect(index)
            else:
                messages.error(arg, "Invalid Username or Password")
                return redirect(adminlogin)
        else:
            messages.error(arg, "Invalid Username or Password")
            return redirect(adminlogin)


