from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('pages.urls', namespace='pages')),
]

# ERROR 404- NOT FOUND PAGE
#handler404 = 'shop.views.Erro404View'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
