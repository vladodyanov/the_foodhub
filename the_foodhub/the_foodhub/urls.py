from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('the_foodhub.web.urls')),
    path('accounts/', include('the_foodhub.accounts.urls')),
    path('vendor_accounts/', include('the_foodhub.vendor.urls')),
    path('menu/', include('the_foodhub.menu.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
