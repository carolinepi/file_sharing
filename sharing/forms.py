from django import forms
from .models import UploadModel


class UploadForm(forms.ModelForm):
    prefix = 'upload_form'

    class Meta:
        model = UploadModel
        fields = ('title', 'file', 'ended_date')

        widgets = {'file': forms.FileInput(
            attrs={
                'class': 'form-control',
            }
        ), 'title': forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ), 'ended_date': forms.DateInput(
            attrs={
                'id': 'datepicker',
                'width': '100%'
            }
        )}
