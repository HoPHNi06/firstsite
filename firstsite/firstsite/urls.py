from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('news.urls')),
    path('news/', include('news.urls')),
    path('account/', include('allauth.urls')),
    path('user/', include('user.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'main.views.error_404'
handler500 = 'main.views.error_500'
handler403 = 'main.views.error_403'
handler400 = 'main.views.error_400'


