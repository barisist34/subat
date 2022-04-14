from django.conf import settings
from django.shortcuts import render,HttpResponse,redirect
from time import *
from .models import *
from subat14 import settings
#import time
# Create your views here.
"""
def index(request):
    return render(request,"ilksayfa.html")

def ilksayfa(request):
    #return render(request,"ilksayfa.html")
    sleep(5)
    return render(request,"ilksayfa2.html")
    #return HttpResponse("Django template 1")
"""
"""def index(request):
    data=ogr2.objects.all()
    sozluk={"ogrenci":data}
    return render (request,"font.html",sozluk)"""

def dinamik(request,id):  #dinamik url
    data=ogr2.objects.filter(id=id)
    sozluk={"og":data}
    return render (request,"font.html",sozluk)

def dinamik_urun(request,id):  #dinamik url
    data=Urun.objects.filter(id=id)
    urun_sayisi=Urun.objects.count()
    
    sozluk={"urunler":data,"urun_sayisi":urun_sayisi}
    #data=ogr2.objects.filter(id=id)
    #sozluk={"og":data}
    return render (request,"urundetay.html",sozluk)
    return render (request,"urundetay.html",sozluk)

"""def unionkayit(request):
    data=ogr2.objects.all().union(ogr3.objects.all())
    sozluk={"union":data}
    return render(request,"font.html",sozluk)

def ornek(request):
    return render(request,"ornek.html")
"""
def index(request):
    urunler=Urun.objects.all()
    sozluk={"urunler":urunler}
    return render(request,"index.html",sozluk)

def ornek(request):
    #base_dir=settings.BASE_DIR
    #sozluk={'base_dir':base_dir}
    #return render(request,"selam.html",sozluk)
    return render(request,"selam.html")

def urun_goster(request):
    urun_goster=Urun.objects.all()
    return render (request,"urun_goster.html",{"urun_goster":urun_goster})

def urun_tek_goster(request,id):
    tek_urun=Urun.objects.filter(id=id)
    urunler=Urun.objects.all()
    return render(request,"tek_urun.html",{"tek_urun":tek_urun,"urunler":urunler})
