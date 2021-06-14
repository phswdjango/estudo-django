from django.shortcuts import render, get_object_or_404
from modelodjango.segunda_app.models import Video
# --------------/nao precisa mais disso.
# videos = [
#          Video(slug='video1', title='Video 01 - segunda_app: ', vimeo_id='558095767'),
#          Video(slug='video2', title='Video 02 - segunda_app: ', vimeo_id='558546415')
#     ]
# videos_dct = {v.slug: v for v in videos}


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
