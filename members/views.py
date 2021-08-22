from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy, reverse
from . import forms
from blog.models import Profile, GalleryImg

class UserRegisterView(generic.CreateView):
    form_class = forms.SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("blog")

class UserEditView(generic.UpdateView):
    form_class = forms.EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("blog")

    def get_object(self):
        return self.request.user

class ChangePasswordView(PasswordChangeView):
    form_class = forms.ChangePasswordForm
    template_name = "registration/change_password.html"
    success_url = reverse_lazy("blog")

class ProfilePageView(generic.DetailView):
    model = Profile
    template_name = "registration/user_profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
        profile_page_user = get_object_or_404(Profile, id=self.kwargs["pk"])
        context["profile_page_user"] = profile_page_user
        return context

class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = forms.CreateProfilePageForm
    template_name = "registration/edit_profile_page.html"
    success_url = reverse_lazy("blog")

class CreateProfilePageView(generic.CreateView):
    model = Profile
    form_class = forms.CreateProfilePageForm
    template_name = "registration/create_user_profile.html"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        #tak bych měla zjistit, který uživatel vyplňuje 
        return super().form_valid(form)

class GalleryListView(generic.ListView):
    model = GalleryImg
    template_name = "registration/gallery.html"
    ordering = ["-id"]

    def get_context_data(self, *args, **kwargs):
        context = super(GalleryListView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs["pk"])
        gallery_imgs = GalleryImg.objects.filter(profile=page_user)
        context["page_user"] = page_user
        context["gallery"] = gallery_imgs
        return context

class AddGalleryImgView(generic.CreateView):
    model = GalleryImg
    template_name = "registration/add_image.html"
    form_class = forms.AddImageForm

    def get_context_data(self, *args, **kwargs):
        context = super(AddGalleryImgView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs["pk"])
        context["page_user"] = page_user
        return context
    
    success_url = reverse_lazy("blog")

class DeleteGalleryImgView(generic.DeleteView):
    model = GalleryImg
    template_name = "registration/delete_image.html"
    success_url = reverse_lazy("blog")

