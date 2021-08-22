from django import forms
from . import models


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ["cat_name"]
        labels = {"cat_name": "New category name" }
        widgets = {
            "cat_name": forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean_cat_name(self):
        cat_name = self.cleaned_data.get("cat_name")
        if not all(i.isascii() for i in cat_name):
            raise forms.ValidationError(
                    'Please, use only ascii.'
                )
        if not all(i.islower() for i in cat_name):
            raise forms.ValidationError(
                "Sorry, my program is still quite lame. Please use only lowercase and ASCII chracters."
            )
        if models.Category.objects.filter(cat_name=cat_name):
                   raise forms.ValidationError(
                            'This category already exists.')
        else:
            return cat_name


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["title", "subtitle", "author", "language", "category", "body", "header_image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "subtitle": forms.TextInput(attrs={"class": "form-control"}),
            #"author": forms.Select(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control", "value": "", "id": "jsusername", "type": "hidden"}),
            "language": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
            }
# form model allows us to create form fields for our model
# "class" zde je CSS class

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ("name", "body")
        labels = {
            "name": "Your Name", 
            "body": "Your Comment"
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }