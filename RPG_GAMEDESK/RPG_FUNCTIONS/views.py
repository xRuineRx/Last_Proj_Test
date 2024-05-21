from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .forms import GamePostForm
from .models import  GamePost


# Create your views here.


class GamePostList(ListView):
    model = GamePost
    template_name ='Gameposts.html'
    context_object_name = 'GamePosts'

class GamePostCreate(CreateView):
    model = GamePost
    form_class = GamePostForm
    template_name = 'GamePost_Create.html'
