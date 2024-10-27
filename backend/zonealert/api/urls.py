from django.urls import path
from . import views
# from .views import hello_world

# urlpatterns = [
#     path('hello/', hello_world),
# ]

urlpatterns = [
    path('map/', views.map, name='map'),
]
