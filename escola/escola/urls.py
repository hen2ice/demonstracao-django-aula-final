from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('cursos.urls')),
    path('admin/', admin.site.urls),
    path('alunos/', include('alunos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]