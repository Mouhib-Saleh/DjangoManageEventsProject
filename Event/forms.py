from .models import Event
from django.forms import Textarea
from django.forms import ModelForm


class AddForm(ModelForm):
    class Meta:
        model = Event
        #fields = ("__all__",)
        fields=("title","description","evt_date","organizer","category","nbe_participant")
        widgets={'description':Textarea(
            attrs={'cols':20,'rows':4}
        ),}