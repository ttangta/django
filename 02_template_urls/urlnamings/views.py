from django.shortcuts import render

# Create your views here.
def naming_index(request):
    return render(request, 'urlnamings/urlnamingsindex.html')

def move(request):
    return render(request, 'urlnamings/move.html')

def data(request, data):
    context = {
        "data": data
    }
    return render(request, 'urlnamings/data.html', context)