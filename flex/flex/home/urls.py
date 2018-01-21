from django.urls import path

from . import views

appname = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('signin', views.user_login, name='signin'),
    path('return_data', views.return_data, name='return_data'),
    path('log', views.log, name='log'),
    path('dash', views.dash, name='dash'),

]