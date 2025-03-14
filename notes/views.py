from django.shortcuts import render
from django.http import Http404

from .models import Notes


def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

def detail(request, note_id):
    try:
        note = Notes.objects.get(id=note_id)
    except Notes.DoesNotExist:
        raise Http404
    return render(request, 'notes/note_detail.html', {'note': note})