from django import forms
from .models import Pay

class PaymentUploadForm(forms.ModelForm):
    class Meta:
        model = Pay
        fields = "__all__"



