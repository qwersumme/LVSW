from django.shortcuts import render

# Create your views here.


def devicemanagerappindex(request):
    return render(request, 'devicemanagerapp/devicemanagerappindex.html')
