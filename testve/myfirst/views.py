
from asyncio import subprocess
from webbrowser import get
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
import requests
from django.http import HttpResponseRedirect
import random
import string
from django.shortcuts import get_object_or_404
import subprocess
# Create your views here.
def home(request):
        if request.method == 'POST':
            form = SightUp(request.POST or None)
            if form.is_valid():
                user_obj = form.save()#Сохранение значений в датабазе методом .save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            if User.objects.filter(email__iexact = email).exists():
                raise forms.ValidationError('User with email already exist')
            user = authenticate(username=username,password =raw_password,email=email)
            login(request,user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/userprofile/')# ЗАМЕНИТЬ
        else:
            form = SightUp()
            context =  {'form':form }

        return render(request, 'home.html',context)


def registerform(request):
        if request.method == 'POST':
            form = SightUp(request.POST or None)
            if form.is_valid():
                user_obj = form.save()#Сохранение значений в датабазе методом .save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username,password =raw_password,email=email)
            login(request,user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/userprofile/')# ЗАМЕНИТЬ
        else:
            form = SightUp()
            context =  {'form':form }

            return render(request,'user.html',context)


def qiwi(request):
      s = requests.Session()
      form = Oplata(request.POST)
      amount = form.data.get('oplata')
      publikey = '48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iP3ETaUg9ucKRzdiiqXagHoBkTWWWps1R2sXia1BGuyh56N8sxvFbaBdSSQ8cDQgYA2KP9qJa5UYhnowCmPftopmC2wZwc2m9DY24GFiEAr'
      amountsrr = str(amount)
      add= string.ascii_letters
      generate = ''.join(random.choice(add) for i in range(16))
      sucsess= ('20.79.176.157/sucsess?uid='+ generate)  #amoundid) заменить
      saveuid =detailsuser(userdetails=request.user,oplatil=generate,temporaryamount=amount)
      saveuid.save()
      getuseremail = User.objects.filter(username=request.user).values_list()[0]
      email = getuseremail[7]
      return HttpResponseRedirect('https://oplata.qiwi.com/create?publicKey='+ publikey+'&amount='+ amountsrr + "&email" + email +'&successUrl=' + sucsess)
def qiwiplata(request):

         if request.method == 'POST':
             form = Oplata(request.POST or None)
             if form.is_valid():
               summai = form.save()
               summa = form.cleaned_data.get('oplata')
         else:
            form = Oplata()
            context = {'form':form}

         return render(request,'qiwi.html',context)
def qiwipass(request):
    getuser= detailsuser.objects.filter(userdetails=request.user).values_list()[0]
    getuseremail = User.objects.filter(username=request.user).values_list()[0]
    publikey = 'eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6IjFmaHR4cS0wMCIsInVzZXJfaWQiOiI3OTI4NDMzMDU4NyIsInNlY3JldCI6Ijg1MmVhM2UxMjRlZTQ0ZDFlZGUwMGI1ODc0YjliYjEyMGQ5NjZlMDdjOTdjOTA4NDUyNzgxYmY3NmQ1NWY4OWIifX0='
    headers ={
    'accept': 'application/json',
    'Authorization': 'Bearer ' + publikey,
    'content-type': 'application/json'
    }
    params = {
    'amount': {
        'currency': 'RUB',
        'value': f'{getuser[3]}'
        },
    }
    requ =requests.put('https://api.qiwi.com/partner/bill/v1/bills/'+getuser[2],json=params, headers=headers)
    json = requ.json()
    get_status = json['status']
    sucess = get_status['value']
    if get_status =='PAID':
        yep = detailsuser(userdetails=request.user,money=sucess)
        yep.save()
        #Месяц траты на платёжку объявляю закрытым!
    return render(request,'succses.html')

def creatprices(request):
    if request.method == 'POST':
        create_form = Product(request.POST or None)#instance=user)
        if create_form.is_valid():
                #create_form.save()
            getproduct = create_form.data.get('product')
            # if " " in getproduct:
                
            getprice = create_form.data.get('prices')
            print(getproduct)
            gettext = create_form.data.get('text')
            getcontainer = create_form.data.get('docker_image')
            add= string.ascii_letters # добавление всех символов
            generate = ''.join(random.choice(add) for i in range(11))     
            saveuser = Prices(useralot=request.user,prise=getprice,product=getproduct,slug = getproduct,docker_choose=getcontainer,uuid = generate,userconnect= request.user)
            saveuser.save()
            return HttpResponseRedirect('#')
            
        else:
           context ={
            'create_form':create_form
            }
    else:
                context = {
                'create_form': Product()
                    }
    return render(request,'create.html',context)

def priselist(request):
    prise = Prices.objects.all().filter(is_active=True)
    prisetrue = Prices.objects.filter(is_active=True).values_list()[0]
    prisefalse = Prices.objects.filter(is_active= False).values_list()

    context = {
        'objects': prise
    }
    return render(request,'prisec.html',context)
    
def prisedetails(request,slug):

    post = get_object_or_404(Prices, slug=slug)
    getinfo = Prices.objects.filter(slug=slug).values_list()[0] ## Получение информации о тарифе(покупке)
    
    return render(request,'details.html',{"post":post,'object':getinfo},)

def oplata(request,slug):
    getuserinfo = detailsuser.objects.filter(userdetails=request.user).values_list()[0]
    gettarifinfo =Prices.objects.filter(slug=slug).values_list()[0]

    gettarifinfo1 =Prices.objects.get(slug=slug)
    terminal =Prices.objects.get(slug=slug)
    gettarifinfof =Prices.objects.filter(slug=slug).update(userconnect=request.user)

    #gettarifinfo1 = gettarifinfo1.userconnect.all()
    

    # addinfo = gettarifinfo1.add(userconnect=request.user)
   # addtarifinfo1 = gettarifinfo1.userconnect.add(userconnect=request.user)
    if getuserinfo[1] < gettarifinfo[3]: ##запили проверку баланса!!! Продумать систему с терминалом.
        print('Пополни!!')
    else:
        seting = getuserinfo[1] - gettarifinfo[3]
        getuserinfo = detailsuser.objects.filter(userdetails=request.user).update(money=seting)
        return HttpResponseRedirect(f'localhost/terminal/{terminal}')
    return render(request,'oplata.html')
@method_decorator(login_required, name='dispatch')
class UserView(DetailView):
    model = User
    template_name = 'registration/userprofile.html'
    context = 'detailsuser'
def get_queryset(self,*args,**kwargs):
    return self.request.user.all()

@login_required
def terminal(request,slug):
    getunit =Prices.objects.filter(useralot=request.user).values_list()[0]
    if getunit[7] == True:
     context = {
     'image':getunit[5],
     'uuid':getunit[6],
     "file":getunit[9],
        }
    #subprocess.call(['cp' f'{getunit[8]}',f'/var/lib/docker/volumes/{getunit[6]}/_data/']) #Копирование файлов клиента
    #subprocess.call(' unzip' + f'/var/lib/docker/volumes/{getunit[6]}/_data/arhive.zip' )
    return render(request,'terminal/terminal.html',context)