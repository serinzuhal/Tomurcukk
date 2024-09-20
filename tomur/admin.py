from django.contrib import admin
from .models import Tomurcuk, Telefon
from .models import Etkinlik, EtkinlikResim, Egitim, Ogretmen



# Tomurcuk modelini admin paneline ekle
admin.site.register(Tomurcuk)
admin.site.register(Telefon)



@admin.register(EtkinlikResim)
class EtkinlikResimAdmin(admin.ModelAdmin):
    list_display = ['id', 'resim']

@admin.register(Etkinlik)
class EtkinlikAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'aciklama']
    filter_horizontal = ('resimler',)


@admin.register(Egitim)
class EgitimAdmin(admin.ModelAdmin):
    list_display = ('egitim_adi', 'aciklama')  # Admin panelinde hangi alanları göstereceğini ayarlıyoruz
    search_fields = ('egitim_adi',)  # Eğitim adına göre arama yapabilirsin

@admin.register(Ogretmen)
class OgretmenAdmin(admin.ModelAdmin):
    list_display = ('isim', 'verdigi_egitim')