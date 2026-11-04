from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "appurls/index.html")

def detail(request, pk):
    context = {
        "pk":pk
    }
    return render(request, 'appurls/detail.html', context)