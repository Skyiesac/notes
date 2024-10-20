from django.shortcuts import render
from .models import Notes
from datetime import datetime


# Create your views here.
def showlist(request):
    all_notes =Notes.objects.all()
    return render(request, 'notesmain/list.html', {'notes': all_notes, 'today': datetime.today})

def details(request, pk):
    note = Notes.objects.get(pk=pk)
    return render(request, 'notesmain/brief.html', {'note': note})