from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.urls import reverse
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField


class Category(models.Model):
    cat_name = models.CharField(max_length=300)

    def __str__(self):
        return self.cat_name

    def get_absolute_url(self):
        return reverse("blog")

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=CASCADE)
    bio = models.CharField(max_length=30000)
    profile_picture = ResizedImageField(null=True, blank=True, upload_to="images/profile")
    website_url = models.CharField(max_length=300, null=True, blank=True)
    github_url = models.CharField(max_length=300, null=True, blank=True)
    twitter_url = models.CharField(max_length=300, null=True, blank=True)
    instagram_url = models.CharField(max_length=300, null=True, blank=True)
    facebook_url = models.CharField(max_length=300, null=True, blank=True)
    linkedin_url = models.CharField(max_length=300, null=True, blank=True)
    any_other_url = models.CharField(max_length=300, null=True, blank=True)
    gallery_images = models.ManyToManyField("GalleryImg", related_name="profile_gallery", blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("blog")

class GalleryImg(models.Model):
    profile = models.ForeignKey(Profile, null=True, on_delete=CASCADE)
    gallery_img = ResizedImageField(size=[1600, 900], upload_to="images/profile/gallery")
    img_text = models.CharField(max_length=30000, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.profile, self.img_text)
    
    class Meta:
        ordering = ['-date']


class Post(models.Model):
    language_choices = [("cz", "Czech"), ("eng", "English")]
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=1000, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    # auto_now_add by mi mělo přiřadit k příspěvku aktuální datum. tento atribut mi udělá z položky needitovatelnou - přidává se automaticky a není tedy vidět v administrátorském prostředí
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="categories")
    #likes = models.ManyToManyField(User, related_name="blog_posts")
    header_image = ResizedImageField(size=[1920, 1080], null=True, blank=True, upload_to="images/")
    language = models.CharField(max_length=3, choices=language_choices)

    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])
        # nahrazuje mi success_url pro všechny Views založené na tomto modelu (ale nefunguje pro DeleteView) args musí být v hranatých závorkách, god knows why, jinak to dvojciferná čísla vyhazuje jako dvě cifry

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title + " | " + str(self.author)
        # toto vytvoří relevantní název článku i s autorem v databázi, místo toho, aby to byl jen příspěvek 1, příspěvek 2, etc

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=CASCADE, related_name="comments")
    name = models.CharField(max_length=300)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return "%s - %s" % (self.post.title, self.name)

    def get_absolute_url(self):
        return reverse("post", args=[str(self.post.id)])
