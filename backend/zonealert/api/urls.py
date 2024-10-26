from django.urls import path
from . import views
# from .views import hello_world

# urlpatterns = [
#     path('hello/', hello_world),
# ]

urlpatterns = [
    path('', views.home, name='home'),
]
