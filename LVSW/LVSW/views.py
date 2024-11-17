from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection

def index(request):
    return render(request, 'myindex.html')
