from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


def home(request):
    # return HttpResponse('<html><body>Olá Django</body></html>', content_type='text/html')  # Fix bug dos acentos
    # return HttpResponse('<html><body>Olá Django</body></html>')
    return render(request, 'base/home.html')
    # esse dicionario é um parametro para o template.
