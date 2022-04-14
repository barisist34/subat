
"""subat14 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from anasayfa.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),

    path ("",index,name="index"),
    path("selam/<int:id>",dinamik,name="dina"),
    path("urun/<int:id>",dinamik_urun,name="dina_urun"),
    path("ornek/",ornek,name="ornek"),
    path("urungoster/",urun_goster,name="urun_goster"),
    path("tekurun/<int:id>",urun_tek_goster,name="urun_tek_goster"),
    path("user/",include("kullanici_islemleri.urls")),
    #path("ilksayfa",ilksayfa,name="ilksayfa_name")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
