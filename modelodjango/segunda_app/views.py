from django.shortcuts import render


def video(request, slug):
    return render(request, 'segunda_app/video.html')
