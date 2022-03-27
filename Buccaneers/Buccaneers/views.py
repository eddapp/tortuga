from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from Buccaneers import *


def home(request):
    return render(request, 'index.html')
