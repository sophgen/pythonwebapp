from django import forms  
from order_entry.models import order  

class order_form(forms.ModelForm):  
    class Meta:  
        model = order  
        fields = "__all__"