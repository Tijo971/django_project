from django.shortcuts import render,redirect
from myfashion.models import Category,Products
from webfashion.models import UserDB, CartDB, Checkout
from PIL import Image

# Create your views here.
def index(arg):
    data = Category.objects.all()
    pro = Products.objects.all()
    return render(arg,'home.html', {'data':data, 'pro':pro})

def product(arg, cat_nme):
    data = Category.objects.filter(cate_name=cat_nme)
    prod = Products.objects.filter(p_category=cat_nme)
    cat = Category.objects.all()
    return render(arg, 'products.html',{'data':data, 'prod':prod, 'cat':cat})

def singleproduct(arg, dataid):
    data = Products.objects.get(id=dataid)
    pro = Products.objects.filter(p_category= dataid)
    return render(arg, 'single_pdt.html', {'data':data, 'pro':pro} )

def cart(arg):
    crt = CartDB.objects.filter(Username=arg.session['usernme'])
    return render(arg, 'cart.html', {'crt':crt})


def userlogin(arg):
    return render(arg, 'userlogin.html')

def usersignin(arg):
    if arg.method == 'POST':
        unme = arg.POST.get('usrname') 
        ema = arg.POST.get('email')
        pn = arg.POST.get('number')
        passw = arg.POST.get('password')
        img = arg.FILES['image']
        obj = UserDB(usernme=unme, email=ema, phnumber=pn, Password=passw, image=img)
        obj.save()
        return redirect(userlogin)

def loginproces(arg):
    if arg.method=='POST':
        unme=arg.POST.get('usrname')
        passw=arg.POST.get('password')
        if UserDB.objects.filter(usernme=unme, Password=passw).exists():
            arg.session['usernme']=unme
            arg.session['Password']=passw
            return redirect(index)
        else:
            return redirect(userlogin)
    else:
        return redirect(userlogin)


def savecart(arg):
    if arg.method=='POST':
        unme = arg.POST.get('uname')
        pro = arg.POST.get('p_name')
        pri = arg.POST.get('p_price')
        qty = arg.POST.get('num-product')
        siz = arg.POST.get('size')
        col = arg.POST.get('color')
        tot = arg.POST.get('total')
        obj = CartDB(pro_name=pro, price=pri, quantity=qty, total=tot, colour=col, size=siz, Username=unme)
        obj.save()
        return redirect(cart)


def checkout(arg):
    return render(arg, 'checkout.html')



def storecheckout(arg):
    if arg.method == 'POST':
        nme = arg.POST.get('firstname')
        ema = arg.POST.get('email')
        add = arg.POST.get('address')
        cit = arg.POST.get('city')
        sta = arg.POST.get('state')
        sip = arg.POST.get('zip')
        cna = arg.POST.get('cardname')
        cnm = arg.POST.get('cardnumber')
        exp = arg.POST.get('expmonth')
        exy = arg.POST.get('expyear')
        evv = arg.POST.get('cvv')
        obj = Checkout(name=nme, email=ema, address=add, city=cit, State=sta, zip= sip, c_name= cna, c_number= cnm,exp_month= exp, exp_yer=exy, cvv=evv)
        obj.save()
        return redirect(index)