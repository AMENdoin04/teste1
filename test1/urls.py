from django.contrib import admin
from django.urls import path, include
from website import urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls'))
]

urlpatterns += staticfiles_urlpatterns()
