from django.shortcuts import render
from . forms import NoteForm
from .models import Note
from django.views.decorators.csrf import csrf_protect
# Create your views here.
def home(request):
    data={ "home":"active"}
    return render(request,"portfolio/Home.html",context=data)

@csrf_protect
def contacus(request):

    form=NoteForm()
    data_retrieve_from_noteform=Note.objects.filter()
    data={
        "form":form,
        "data_retrieve_frm_database":data_retrieve_from_noteform,
        "contact":"active"
    }
    
    if request.method=="POST":
        
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        description=request.POST.get('description')
        
        note=Note()
        note.name=name
        note.email=email
        note.description=description
        note.subject=subject
        note.save()
        print("Successfully save in database")
    return render(request,"portfolio/contact.html",context=data)