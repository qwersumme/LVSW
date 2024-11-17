from django.shortcuts import render

def rentalindex(request):
    return render(request, 'rentalapp/rentalindex.html')
