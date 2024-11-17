from django.shortcuts import render

# Create your views here.


def eventmanagerappindex(request):
    return render(request, 'eventmanagerapp/eventmanagerappindex.html')
