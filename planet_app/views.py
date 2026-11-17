from django.shortcuts import render

import datetime

def render_index(request):
    t = datetime.datetime.now().time()
    dictObj = {"name": "mangesh","time":t}
    return render(request,"planet_app/index.html",dictObj)

def render_mercury(request):
    return render(request,"planet_app/mercury.html")

def render_venus(request):
    return render(request, "planet_app/venus.html")

def render_earth(request):
    return render(request, "planet_app/earth.html")

def render_mars(request):
    return render(request, "planet_app/mars.html")

def render_jupiter(request):
    return render(request, "planet_app/jupiter.html")

def render_saturn(request):
    return render(request, "planet_app/saturn.html")

def render_uranus(request):
    return render(request, "planet_app/uranus.html")

def render_neptune(request):
    return render(request, "planet_app/neptun.html")
