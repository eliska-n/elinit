from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("blog", views.PostListView.as_view(), name = "blog"), 
    path("post/<int:pk>", views.PostDetailView.as_view(), name = "post"),
    path("add_post", views.AddPostView.as_view(), name = "add_post"),
    path("post/edit/<int:pk>", views.UpdatePostView.as_view(), name = "edit_post"),
    path("post/delete/<int:pk>", views.DeletePostView.as_view(), name = "delete_post"),
    path("add_category", views.AddCategoryView.as_view(), name = "add_category"),
    path("category/<str:cats>", views.CategoryView, name = "category"),
    path("category_list", views.CategoryListView.as_view(), name = "category_list"), 
    path("post/<int:pk>/comment", views.AddCommentView.as_view(), name = "add_comment"),
    path("<int:pk>/user_posts", views.UserPostsView.as_view(), name = "user_posts"),
    path("<str:lng>/blog", views.LanguagePostListView.as_view(), name = "language_post_list"),
    path('cz/about', views.AboutczView.as_view(), name='about_cz'),
    path('eng/about', views.AboutengView.as_view(), name='about_eng'),

]