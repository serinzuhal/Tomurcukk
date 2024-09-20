from django.db import models
from django.utils import timezone

class Tomurcuk(models.Model):
    resim = models.ImageField(null=True, blank=True)
    oda_adi = models.CharField(max_length=30, default="Belirtilmedi")
    aciklama = models.TextField(max_length=210,default="Açıklama girilmedi")
    created_at = models.DateTimeField(auto_now_add=True)  # Zamanı otomatik olarak ekler

    def __str__(self):
        return self.oda_adi
    
    class Meta:
        verbose_name_plural = "Kreşimizin Oda Bilgileri"
    
class Telefon(models.Model):
    telefon = models.CharField(max_length=20, help_text="+90 ile başlayacak şekilde giriniz", default="Not Provided")
    adres = models.TextField(default="Adres girilmedi")
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.telefon
    
    class Meta:
        verbose_name_plural = "İletişim Bilgileri"


class EtkinlikResim(models.Model):
    resim = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return f"Resim {self.id}"

class Etkinlik(models.Model):
    baslik = models.CharField(max_length=200)
    aciklama = models.TextField()
    resimler = models.ManyToManyField(EtkinlikResim, related_name='etkinlikler', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Zamanı otomatik olarak ekler

    def __str__(self):
        return self.baslik
    
    class Meta:
        verbose_name_plural = "Etkinlikler"

    
class Egitim(models.Model):
    egitim_adi = models.CharField(max_length=200, verbose_name="Eğitim Adı")
    aciklama = models.TextField(verbose_name="Eğitim Açıklaması")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.egitim_adi
    
    class Meta:
        verbose_name_plural = "Eğitimler"


class Ogretmen(models.Model):
    isim = models.CharField(max_length=100)  # Öğretmenin ismi
    resim = models.ImageField(upload_to='ogretmen_resimleri/')  # Öğretmenin resmi
    verdigi_egitim = models.TextField()  # Verdiği eğitim bilgileri
    linkedin = models.URLField(max_length=200, blank=True, null=True)   # LinkedIn hesabı
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.isim

    class Meta:
        verbose_name_plural = "Öğretmenler"
