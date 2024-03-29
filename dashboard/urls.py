from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('traffic/',TrafficList.as_view(),name='TrafficView'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/',dashboard,name='dashboard')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)