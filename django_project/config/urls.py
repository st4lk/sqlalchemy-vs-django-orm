from django.contrib import admin
from django.urls import include, path

from active_records.urls import urlpatterns as active_records_urlpatterns
from fk.urls import urlpatterns as fk_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('activerecords/', include(active_records_urlpatterns)),
    path('fk/', include(fk_urlpatterns)),
]
