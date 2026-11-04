from django.shortcuts import render

# Create your views here.
def naming(request):
    return render(request, 'namingurls/naming.html')

def goto(request):
    return render(request, 'namingurls/goto.html')