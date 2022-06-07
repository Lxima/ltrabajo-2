from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns  = [
    path('admin/', admin.site.urls),
    re_path('',include("applications.Médicos.urls")),
    re_path('',include("applications.Paciente.urls")),
    re_path('',include("applications.Rd.urls")),
]