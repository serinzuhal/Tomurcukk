from django.shortcuts import render,redirect
from .models import Tomurcuk, Telefon
from .models import Etkinlik,Egitim, Ogretmen


def home(request):
    telefonlar = Telefon.objects.all()  # Telefon verilerini al
    return render(request, 'index.html', {'telefonlar': telefonlar})

def hakkimizda(request):
    telefonlar = Telefon.objects.all()  # Telefon verilerini al
    tomurcuklar = Tomurcuk.objects.all().order_by('-created_at')  # En son eklenenler en başta
    egitimler = Egitim.objects.all().order_by('-created_at')
    ogretmenler = Ogretmen.objects.all().order_by('-created_at')  # Veritabanındaki tüm öğretmenleri alır

    # Hem telefonlar hem de tomurcuklar verilerini içeren bir sözlük oluştur
    context = {
        'telefonlar': telefonlar,
        'tomurcuklar': tomurcuklar,
        'egitimler': egitimler,
        'ogretmenler': ogretmenler,
    }

    # Verileri şablona gönder
    return render(request, 'hakkimizda.html', context)


def iletisim(request):
    telefonlar = Telefon.objects.all()  # Tüm Telefon nesnelerini al
    return render(request, 'iletisim.html', {'telefonlar': telefonlar})


def etkinlik(request):
    telefonlar = Telefon.objects.all()  # Telefon verilerini al
    tomurcuklar = Tomurcuk.objects.all().order_by('-created_at')  # En son eklenenler en başta
    tomurcuk_count = tomurcuklar.count()  # Veri sayısını al
    etkinlikler = Etkinlik.objects.all().order_by('-created_at')  # 'created_at' yerine etkinliklerin oluşturulma tarihini belirten alan

    # Hem telefonlar hem de tomurcuklar verilerini içeren bir sözlük oluştur
    context = {
        'telefonlar': telefonlar,
        'tomurcuklar': tomurcuklar,
        'tomurcuk_count': tomurcuk_count,
        'etkinlikler': etkinlikler,
    }

    # Verileri şablona gönder
    return render(request, 'etkinlik.html', context)

def whatsapp(request):
    telefonlar = Telefon.objects.all()  # Telefon verilerini al
    return render(request, '_whatsapp.html', {'telefonlar': telefonlar})

