from django.shortcuts import render
from django.http import HttpResponse
from .models import Ubezpieczenie
from .forms import OcenaForm

def test_response(request):
    wszystkie = Ubezpieczenie.objects.all()
    return HttpResponse("To jest nasz pierwszy test")

def wszystkie_ubezpieczenia(request):
    wszystkie = Ubezpieczenie.objects.all()
    return render(request, 'ubezpieczenia.html', {'ubezpieczenie': wszystkie})

def login(request):
    return render(request, 'login.html')
def index(request):
    wszystkie = Ubezpieczenie.objects.all()
    return render(request, 'index.html', {'ubezpieczenie': wszystkie})

def ocena_ubezpieczenia(request):
    form = OcenaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

    return render(request, 'ocena.html', {'form': form})


'''
from django.shortcuts import render, get_object_or_404, redirect
from .models import Film, DodatkoweInfo, Ocena
from .forms import FilmForm, DodatkoweInfoForm, OcenaForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, FilmSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FilmView(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
'''

