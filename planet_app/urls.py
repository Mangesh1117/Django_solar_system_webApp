from django.urls import path

from . import views

urlpatterns = [
    path("index/",views.render_index),
    path("mercury/",views.render_mercury),
    path("venus/",views.render_venus),
    path("earth/",views.render_earth),
    path("mars/",views.render_mars),
    path("jupiter/",views.render_jupiter),
    path("saturn/",views.render_saturn),
    path("uranus/",views.render_uranus),
    path("neptune/",views.render_neptune)
]