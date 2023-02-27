from django.forms import ModelForm
from .models import attendance

class expform(ModelForm):
    class Meta:
        model = attendance
        fields = ['Date','Morning','Afternoon']