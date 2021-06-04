from django.shortcuts import render

videos = [
         {'slug': 'video1', 'title': 'Video 01 - segunda_app: ', 'vimeo_id': "558095767"},
         {'slug': 'video2', 'title': 'Video 02 - segunda_app: ', 'vimeo_id': "558546415"}
    ]
videos_dct = {dct['slug']: dct for dct in videos}


def indice(request):
    return render(request, 'segunda_app/indice.html', context={'videos': videos})


def video(request, slug):

    contexto_do_template = videos_dct[slug]

    return render(request, 'segunda_app/video.html', context={'video': contexto_do_template})
