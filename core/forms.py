from django import forms
from .models import Room

class CreateRoom(forms.ModelForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Room
        fields = ["username", "room_name"]
        widgets = {
            'room_name': forms.TextInput(attrs={'class': 'form-control'})
        }