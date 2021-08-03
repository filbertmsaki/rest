from django.urls import path, include
from . import views
from rest_framework import routers
from . import views

r = routers.DefaultRouter()
r.register(r'road', views.LightViewSet)

urlpatterns = [
        #path('', include(r.urls)),
        path('', views.index, name='index'),
        path('lightUpdate/<str:pk>', views.updateLight, name='updateLight'),
        path('api/', include(r.urls)),
]
