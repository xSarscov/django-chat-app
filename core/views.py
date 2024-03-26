from django.shortcuts import redirect, render
from .forms import CreateRoom
from .models import Message, Room

# Create your views here.
def room(request, room_name, username):
        rooms = Room.objects.all()
        room = Room.objects.get(room_name=room_name)
        messages = Message.objects.filter(room=room)

        if not rooms or not room:
            return redirect('join_room') 

        context = {
            "messages": messages,
            "user": username,
            "room_name": room_name,
            "rooms": rooms
        }

        return render(request, "core/index.html", context)

    

def create_room(request):
    if request.method == 'POST':
        form = CreateRoom(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            room_name = form.cleaned_data['room_name']

            room, create = Room.objects.get_or_create(room_name=room_name)
            if create:
                return redirect('room', room_name=room_name, username=username)
            else:
                return render(request, "core/create-room.html", {
                    "form": form,
                    "error": "Room already exists."
                })

        else:
            return render(request, 'core/index.html', {
                'form': form
            })
        
    form = CreateRoom()
    context = {
        "form": form
    }
    return render(request, "core/create-room.html", context)

def join_room(request):
    if request.method == "POST":
        form = CreateRoom(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            room_name = form.cleaned_data['room_name']

            room = Room.objects.get(room_name=room_name)
        
            if not room:
                return render(request, 'core/create-room.html', {
                "form": form,
                "error": "Room not found."
                })
                
            return redirect('room', room_name=room.room_name, username=username)
        else:
            print("error")
            return render(request, 'core/create-room.html', {
                "form": form,
            })

    form = CreateRoom()
    context = {
        "form": form
    }
    return render(request, "core/create-room.html", context)
    