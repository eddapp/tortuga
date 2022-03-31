from django.shortcuts import render


# Create your views here.
def beach(request):
    return render(request, 'beach.html')
