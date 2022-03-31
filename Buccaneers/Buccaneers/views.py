from django.shortcuts import render


def hook(request):
    return render(request, 'hook.html')


def plank(request):
    return render(request, 'plank.html')


def logn(request):
    return render(request, 'logn.html')


def inn(request):
    return render(request, 'inn.html')


def signp(request):
    return render(request, 'signp.html')
