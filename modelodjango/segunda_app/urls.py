from django.urls import path
from modelodjango.segunda_app.views import video, indice, email
app_name = 'segunda_app'
urlpatterns = [
    path('video/<slug:slug>', video, name='video'),
    path('', indice, name='indice'),
    path('email', email, name='email'),
]
