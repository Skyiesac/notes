from django.shortcuts import render ,get_object_or_404, redirect
from .models import Notes
from datetime import datetime
from .forms import Newnotes

# Create your views here.
def showlist(request):
    all_notes =Notes.objects.all()
    return render(request, 'notesmain/list.html', {'notes': all_notes, 'today': datetime.today})

def details(request, pk):
    note = Notes.objects.get(pk=pk)
    return render(request, 'notesmain/brief.html', {'note': note})

def create_note(request):
    if request.method == 'POST':
        form = Newnotes(request.POST)  
        if form.is_valid():
            form.save() 
            return redirect('gotonote') 
    else:
        form = Newnotes() 
    return render(request, 'notesmain/create_note.html', {'form': form})

def editnote(request,pk):
    note = get_object_or_404(Notes, pk=pk)
    form = Newnotes(instance=note)
    if request.method == 'POST':
        form = Newnotes(request.POST, instance= note)
        if form.is_valid():
            form.save()
            return redirect('nodetail',pk=pk)
        else:
          form = Newnotes(instance=note)
    return render(request, 'notesmain/edit.html',{'form':form})

def deletenote(request,pk):
    note = get_object_or_404(Notes, pk=pk)

    if request.method == 'POST':
        note.delete()
        return redirect('gotonote')
    return render(request, 'notesmain/delete.html', {'note':note})