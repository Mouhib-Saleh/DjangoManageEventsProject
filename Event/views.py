from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import AddForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import *
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def index(request):
    return HttpResponse("Bonjour")
def affiche(request,classe):
    return render(request,"Event/affiche.html",{"c":classe})
# QuerySets
def ListEvt(request):
    evt=Event.objects.all()
    #affichage HTTPR
    """resultat ="----".join(e.title for e in evt)
    return HttpResponse(resultat) """
    #affichage avec template
    return render(request,"Event/afficheEvt.html",{"e":evt})
class ListEvtGeneric(ListView):
    model=Event
    context_object_name='e'
    #On garde le template par defaut event_list.html
    #fields="all"
    template_name="Event/afficheEvt.html"
    ordering=['-evt_date']
def Detail(request,title):
    event = Event.objects.get(title=title)
    return render(request,"Event/Detail.html",{"t":event})


def AjoutEvt(request):
    if request.method =="GET":
        form = AddForm()
        return render(request,"Event/Ajout.html",{"f":form})
    if request.method=="POST":
        form = AddForm(request.POST)
        if form.is_valid():
           title=form.cleaned_data['title']
           if Event.objects.filter(title=title).exists():
                messages.error(request,"Un événement avec ce titre existe déja")
                return render(request,'Event/Ajout.html',{'f':form})
           else:
                new_evt=form.save(commit=False)
                new_evt.save()
                messages.success(request, "L'événement a été ajouté avec succès !")
                return HttpResponseRedirect(reverse('Aff'))        
    else:
        return render(request,"Event/Ajout.html",
                      {"f":form,"msg_erruer":"erreur lors l'ajout d'un evt"})
    
def SupprimerEvt(request,id):
    evt=get_object_or_404(Event,id=id)
    evt.delete()
    messages.success(request,"L'événement a été supprimé avec succès !")
    return redirect('Aff')
