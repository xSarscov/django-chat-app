from django.urls import path
from .views import room, create_room, join_room

urlpatterns = [
    path('', create_room, name='create_room'),
    path('join_room/', join_room, name='join_room'),
    path('<str:room_name>/<str:username>', room, name='room'),
]