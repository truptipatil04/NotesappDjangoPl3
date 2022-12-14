from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path("",views.acc,name='acc'),
    path("",views.register,name='register'),
    path("login/",views.login,name='login'),
    path("logout/",views.logout,name='logout')
] 

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)