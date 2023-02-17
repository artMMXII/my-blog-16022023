from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Note
from .forms import AddNoteForm


def index(request):
    context = {'title': 'Главная страница'}
    return render(request, 'blog/index.html', context=context)


class PostView(ListView):
    model = Note
    template_name = 'blog/note.html'


class AddNote(CreateView):
    form_class = AddNoteForm
    template_name = 'blog/add_note.html'
    success_url = reverse_lazy('home')



