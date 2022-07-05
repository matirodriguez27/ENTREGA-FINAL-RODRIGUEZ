from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)