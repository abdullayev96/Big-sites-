from django import  forms
from .models import *
from django.core.exceptions import ValidationError
# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=300, label="Super title", widget=forms.TextInput(attrs={'class': 'form-input'}))
#     slug = forms.SlugField(max_length=260, label="Url")
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10}), label="Content")
#     is_published = forms.BooleanField(label="Bool", required=False, initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Category")

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Category is empty "

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content','image', 'is_published', 'cat']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-input'}),
            'content':forms.Textarea(attrs={'cols': 60, 'rows': 10}),

                }


    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title)>200:
            raise ValidationError("you must write only 200 simbole  ")
        return title

