from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'BizzyCardApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login')
]

urlpatterns += staticfiles_urlpatterns()