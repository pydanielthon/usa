from django.urls import path
from . import views

app_name = 'app'


urlpatterns = [
    path('', views.home, name='home'),
    path('site2/', views.site2, name='site2'),

]

