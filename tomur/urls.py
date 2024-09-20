from django.urls import path
from .views import hakkimizda,home,etkinlik
from . import views

urlpatterns = [
    path('', home, name='home'),  # Boş path (ana sayfa) için yönlendirme

    path('hakkimizda/', hakkimizda, name='hakkimizda'),
    path('etkinlik/', etkinlik, name='etkinlik'),
    path('iletisim/', views.iletisim, name='iletisim'),


]
