from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from blog.models import Profile, GalleryImg

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    #widget mi tam přidává css classes, které jsou rozpoznány bootstrapem a můžu tak udělat ten formulář hezčí - abych mohla přidat widgets také k položkám, které jsou jaksi uvnitř UserCreationForm, musím udělat trochu woodoo a to je předefinovat __init__

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2",)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control"

class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields["old_password"].widget.attrs["class"] = "form-control"
        self.fields["new_password1"].widget.attrs["class"] = "form-control"
        self.fields["new_password2"].widget.attrs["class"] = "form-control"

class CreateProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "profile_picture", "website_url", "github_url", "twitter_url", "instagram_url", "facebook_url", "linkedin_url", "any_other_url")
        widgets = {
            "bio": forms.Textarea(attrs={"class": "form-control"}),
            #"profile_picture": forms.Input(attrs={"class": "form-control"}),
            "website_url": forms.TextInput(attrs={"class": "form-control"}),
            "github_url": forms.TextInput(attrs={"class": "form-control"}),
            "twitter_url": forms.TextInput(attrs={"class": "form-control"}),
            "instagram_url": forms.TextInput(attrs={"class": "form-control"}),
            "facebook_url": forms.TextInput(attrs={"class": "form-control"}),
            "linkedin_url": forms.TextInput(attrs={"class": "form-control"}),
            "any_other_url": forms.TextInput(attrs={"class": "form-control"}),
        }

class AddImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImg
        fields = ("profile", "gallery_img", "img_text")
        widgets = {
            "profile": forms.TextInput(attrs={"class": "form-control", "value": "", "id": "jsusername2", "type": "hidden"}),
            "img_text": forms.Textarea(attrs={"class": "form-control"}),
        }
