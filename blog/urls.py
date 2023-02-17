from django.urls import path
from blog.views import index
from .views import PostView, AddNote

urlpatterns = [
    path('', index, name='home'),
    path('note/', PostView.as_view(), name='note'),
    path('add_note/', AddNote.as_view(), name='add_note')
]
