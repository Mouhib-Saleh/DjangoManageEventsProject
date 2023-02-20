from django.urls import path
from.views import *
#from . import views

urlpatterns = [
    path("index/",index),
    path("affiche/<str:classe>",affiche),
    path("afficheEvt/",ListEvt,name="Aff"),
    path('list/',ListEvtGeneric.as_view()),
    #path("list/",ListEvtGeneric.as_view(),template_name="")
    path("List/<str:title>",Detail,name="D"),
    path("Ajout/",AjoutEvt,name="Add"),
    path('/supprimer/<int:id>/', SupprimerEvt, name='supprimer'),

]


