from django.db import models
from django.urls import reverse
# Create your models here.
class FuqoroMurojat(models.Model):
    fish = models.CharField(max_length=500,verbose_name='Fuqaroning familyasi, ismi va sharifi')
    passportid = models.CharField(max_length=500,verbose_name='Fuqaroning pasport seriyasi va raqami')
    jshshir = models.CharField(max_length=500,verbose_name='JSHSHIR')
    tshnomi = models.CharField(max_length=500,verbose_name='Tuman/shahar nomi')
    yashmanzil = models.CharField(max_length=500,verbose_name="Yashash manzili (pasportdagi ma'lumot)")
    kraqami = models.CharField(max_length=500,verbose_name='Turar joy kadastr raqami')
    ksoni = models.IntegerField(verbose_name="Olingan ko'mir miqdori (tonnada)")
    rasm = models.CharField(max_length=500,verbose_name="Ma'lumot uchun rasm")
    tel = models.IntegerField(verbose_name='Telefon raqami')
    qachonOlgan = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.fish
    
    def get_absolute_url(self):
        return reverse('home')


class TashkilotMurojat(models.Model):
    tnomi = models.CharField(max_length=500,verbose_name='Tashkilot nomi')
    tkim = models.CharField(max_length=500,verbose_name='Tashkilotda kim bo`lib ishlashingiz')
    qachonOlgan = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.tkim
    
    def get_absolute_url(self):
        return reverse('home')