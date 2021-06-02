from django.urls import path
from modelodjango.segunda_app.views import video
app_name = 'segunda_app'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
]
