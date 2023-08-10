from django import forms
from .models import Review

class ReviewUploadForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"



