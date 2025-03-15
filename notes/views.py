from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


from .forms import NotesForm
from .models import Notes

def add_like_view(request, pk):
    if request.method == "POST":
        note = get_object_or_404(Notes, pk=pk)
        note.likes += 1
        note.save()
        return HttpResponseRedirect(reverse("notes.detail", args=(pk,)))
    return Http404

def change_visibility_view(request, pk):
    if request.method == "POST":
        note = get_object_or_404(Notes, pk=pk)
        note.is_public = not note.is_public
        note.save()
        return HttpResponseRedirect(reverse("notes.detail", args=(pk,)))
    return Http404

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'
    login_url = '/admin'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin, ListView):
    template_name = 'notes/notes_list.html'
    model = Notes
    context_object_name = 'notes'
    login_url = '/admin'
    def get_queryset(self):
        return self.request.user.notes.all()


class PopularNotesListView(ListView):
    template_name = 'notes/notes_list.html'
    model = Notes
    context_object_name = 'notes'
    queryset = Notes.objects.filter(likes__gte=1)

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'


class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'



