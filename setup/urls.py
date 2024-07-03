from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('apps.estoque.urls')),
        path('', include('apps.usuario.urls')),
        path('', include('apps.carrinho.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)