from django.shortcuts import render ,get_object_or_404, redirect
from .models import Notes
from datetime import datetime
from .forms import Newnotes
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def showlist(request):
    all_notes =Notes.objects.filter(user= request.user)
    return render(request, 'notesmain/list.html', {'notes': all_notes, 'today': datetime.today})
    

@login_required
def details(request, pk):
    note = Notes.objects.get(pk=pk)
    return render(request, 'notesmain/brief.html', {'note': note})

@login_required
def create_note(request):
    if request.method == 'POST':
        form = Newnotes(request.POST)  
        if form.is_valid():
            note = form.save(commit= False) 
            note.user= request.user
            note.save()
            return redirect('gotonote') 
    else:
        form = Newnotes() 
    return render(request, 'notesmain/create_note.html', {'form': form})

@login_required
def editnote(request,pk):
    note = get_object_or_404(Notes, pk=pk, user= request.user)
    form = Newnotes(instance=note)
    if request.method == 'POST':
        form = Newnotes(request.POST, instance= note)
        if form.is_valid():
            note = form.save(commit= False) 
            note.user= request.user
            note.save()
            return redirect('nodetail',pk=pk)
        else:
          form = Newnotes(instance=note)
    return render(request, 'notesmain/edit.html',{'form':form})

@login_required
def deletenote(request,pk):
    note = get_object_or_404(Notes, pk=pk, user= request.user)

    if request.method == 'POST':
        note.delete()
        return redirect('gotonote')
    return render(request, 'notesmain/delete.html', {'note':note})

@login_required
def searching(request):
    tosearch = request.GET.get('search','')
    note= Notes.objects.filter(user= request.user)
    if tosearch:
        note = note.filter(title__icontains = tosearch)
    return render(request, 'notesmain/search.html', {'note':note, 'tosearch':tosearch})
