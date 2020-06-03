
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', include('src.urls')),
    path('nosotros', include('userdata.urls')),
    path('admin/', admin.site.urls),

]
