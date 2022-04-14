from django.db import models

# Create your models here.

class ogr(models.Model):
    isim_soyad=models.CharField(max_length=50)

class ogr2(models.Model):
    isim_soyad=models.CharField(max_length=50)
    aciklama=models.TextField(max_length=50)
    resim=models.FileField(upload_to='kisiresmi/',blank=True,null=True,verbose_name="Kişi resmi ekleyin")
    def __str__(self):
        return self.isim_soyad

class ogr3(models.Model):
    isim_soyad=models.CharField(max_length=50)
    aciklama=models.TextField(max_length=50)
    resim=models.FileField(upload_to='kisiresmi/',blank=True,null=True,verbose_name="Kişi resmi ekleyin")
    def __str__(self):
        return self.isim_soyad
class Urun(models.Model):
    #id=models.AutoField(primary_key=True,verbose_name="Ürün Kodu")
    urun_adi=models.CharField(max_length=50,verbose_name="Ürün Adı")
    urun_fiyat=models.FloatField()
    kategori=models.CharField(max_length=20,verbose_name="Kategori")
    detay=models.TextField(verbose_name="Ürün Açıklaması")
    resim=models.FileField(upload_to='img/',blank=True,null=True,verbose_name="Ürün resmi ekleyin")

    def __str__(self):
        return self.urun_adi

class Urunler2(models.Model):
    urun_adi=models.CharField(max_length=50)
    urun_fiyat=models.FloatField()
    kategori=models.CharField(max_length=20,verbose_name="Kategori")
    detay=models.TextField(verbose_name="Ürün Açıklaması")
    def __str__(self):
        return self.urun_adi

class Urunler3(models.Model):
    urun_adi=models.CharField(max_length=50)
    #urun_fiyat=models.FloatField()
    kategori=models.CharField(max_length=20,verbose_name="Kategori")
    detay=models.TextField(verbose_name="Ürün Açıklaması")
    def __str__(self):
        return self.urun_adi