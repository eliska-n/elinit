from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
    path('password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('<int:pk>/profile', views.ProfilePageView.as_view(), name='profile_page'),
    path('<int:pk>/edit_profile', views.EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile', views.CreateProfilePageView.as_view(), name='create_profile_page'),
    path('<int:pk>/gallery', views.GalleryListView.as_view(), name='gallery'),
    path('<int:pk>/add_image', views.AddGalleryImgView.as_view(), name='add_image'),
    path('delete_image/<int:pk>', views.DeleteGalleryImgView.as_view(), name='delete_image'),
]