from django.shortcuts import render

# Create your views here.
def center(request):
    return render(request, 'centers/center.html')