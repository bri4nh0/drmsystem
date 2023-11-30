from django import forms
from watermark.models import ImageFile, File


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageFile
        fields = ['name', 'image']


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file']
        widgets = {
            'file': forms.FileInput(attrs={'accept': '.doc,.docx'})
        }
