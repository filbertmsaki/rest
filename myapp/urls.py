from django.urls import path, include
from . import views
from rest_framework import routers
from . import views

#r = routers.DefaultRouter()
#r.register(r'road', views.RoadViewSet)

urlpatterns = [
        #path('', include(r.urls)),
        path('', views.RoadViewSet.as_view()),
]
