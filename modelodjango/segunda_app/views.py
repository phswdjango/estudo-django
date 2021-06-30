from django.shortcuts import render, get_object_or_404, HttpResponse
from modelodjango.segunda_app.models import Video
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


@login_required
def email(request):
    send_mail(
        "teste",
        "olá, eu sou um testes",
        "noreply@phsolucoesweb.com.br<noreply@phsolucoesweb.com.br>",
        ["pedrohenriquemadureira@gmail.com"]
    )

    return HttpResponse("email enviado, se deus quiser")


def indice(request):
    videos = Video.objects.order_by('creation').all()
    # order_by: ordena a query pelos valores da coluna 'creation'.
    # all(): pega todos os valores
    return render(request, 'segunda_app/indice.html', context={'videos': videos})


def video(request, slug):
    # contexto_do_template = Video.objects.get(slug=slug)
    contexto_do_template = get_object_or_404(Video, slug=slug)
    # faz a busca no banco do model "Video" utilizando o slug expecificado, e caso nao econcontre, retorna um 404
    # ao invez de dar erro.
    return render(request, 'segunda_app/video.html', context={'video': contexto_do_template})
