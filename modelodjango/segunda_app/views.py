from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, title, vimeo_id):
        self.slug = slug
        self.title = title
        self.vimeo_id = vimeo_id

    def get_absolute_url(self):   # existe uma conveção no django de criar esse metodo para retorar a url
        return reverse('segunda_app:video', args=(self.slug,))


videos = [
         Video('video1', 'Video 01 - segunda_app: ', '558095767'),
         Video('video2', 'Video 02 - segunda_app: ', '558546415')
    ]
videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'segunda_app/indice.html', context={'videos': videos})


def video(request, slug):
    contexto_do_template = videos_dct[slug]
    return render(request, 'segunda_app/video.html', context={'video': contexto_do_template})
