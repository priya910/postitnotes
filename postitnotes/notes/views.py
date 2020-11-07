from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm, NoteCreateForm

# List Notes
def list_notes(request):
    active_notes = Note.objects.all().filter(completed=False)  
    done_notes = Note.objects.all().filter(completed=True)
    favourite_notes = Note.objects.all().filter(favourite=True)
    notes_context = {'active_notes': active_notes, 'done_notes': done_notes, 'favourite_notes': favourite_notes}
    return render(request, "index.html", notes_context)


# Delete Notes
def delete_note(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect("/notes/")

# Create Notes
def create_note(request):   
    if request.method == "POST":
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/notes/")
    else:
        form = NoteCreateForm()
    return render(request, "create.html", {'form': form})

#Edit Note
def edit(request, id):
    note = Note.objects.get(id=id)
    initial_dict = { 
        "title": note.title, "description": note.description, "author": note.author, "completed": note.completed
    } 
    form = NoteForm(request.POST, instance=note, initial=initial_dict)
    if form.is_valid():
        form.save()
        return redirect('/notes/')
    return render(request, "edit.html", {'form':form})

#Mark Done
def mark_done(request, id):
    note = Note.objects.get(id=id)
    note.completed = True
    note.save()
    return redirect('/notes/')

#Mark Favourite
def mark_favourite(request, id):
    note = Note.objects.get(id=id)
    note.favourite = True
    note.save()
    return redirect('/notes/')

#Remove Favourite
def remove_favourite(request, id):
    note = Note.objects.get(id=id)
    note.favourite = False
    note.save()
    return redirect('/notes/')