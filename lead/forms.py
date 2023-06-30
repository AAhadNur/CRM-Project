from django.forms import ModelForm

from .models import Lead


class AddLeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'description', 'priority', 'status']
