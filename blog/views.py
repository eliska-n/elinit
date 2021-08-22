from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from .forms import PostForm, CategoryForm, CommentForm
from django.urls import reverse_lazy



class IndexView(TemplateView):
    template_name = "index.html"

class AboutczView(TemplateView):
    template_name = "about_cz.html"

class AboutengView(TemplateView):
    template_name = "about_eng.html"

class PostListView(ListView):
    model = models.Post
    template_name = "post_list.html"
    #ordering = ["-id"]

    #jak vytvořit QuerySet (pokud bych chtěla přidávat na stránku "blog" seznam kategorií) skrze který mohu na stránce iterovat
    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = models.Category.objects.all()
    #     context = super(PostListView, self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context

class PostDetailView(DetailView):
    model = models.Post
    template_name = "post_detail.html"

class AddPostView(CreateView):
    model = models.Post
    form_class = PostForm
    template_name = "add_post.html"
    #fields = ["title", "author", "body"]

class UpdatePostView(UpdateView):
    model = models.Post
    form_class = PostForm
    template_name = "update_post.html"
    #fields = ["title", "body"]

class DeletePostView(DeleteView):
    model = models.Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("blog")
    
class AddCategoryView(CreateView):
    model = models.Category
    form_class = CategoryForm
    template_name = "add_category.html"
    success_url = reverse_lazy("blog")

def CategoryView(request, cats):
    cats_name = models.Category.objects.get(cat_name = cats.replace("-", " "))
    category_posts = models.Post.objects.filter(category=cats_name)
    return render(request, "categories.html", {"cats": cats.replace("-", " ").upper(), "category_posts": category_posts,})
        # .title() mi zajistí první velké písmeno pro název kategorie, .upper() všechna velká a .replace mi deslugifikuje cats 

class CategoryListView(ListView):
    model = models.Category
    template_name = "category_list.html"

class AddCommentView(CreateView):
    model = models.Comment
    form_class = CommentForm
    template_name = "add_comment.html"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)

class UserPostsView(ListView):
    model = models.Post
    template_name = "user_posts.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UserPostsView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(models.User, id=self.kwargs["pk"])
        user_posts = models.Post.objects.filter(author=page_user)
        context["page_user"] = page_user
        context["user_posts"] = user_posts
        return context

class LanguagePostListView(ListView):
    model = models.Post
    template_name = "language_post_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(LanguagePostListView, self).get_context_data(*args, **kwargs)
        post_lng = self.kwargs["lng"]
        language_posts = models.Post.objects.filter(language=post_lng)
        context["language"] = post_lng.upper()
        context["language_posts"] = language_posts
        return context

