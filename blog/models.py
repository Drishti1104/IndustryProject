from django.utils import timezone
from distutils.command.upload import upload
from select import select
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"

class Post(models.Model):
    title = models.CharField(max_length=100)
    # excerpt = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    author = models.CharField(max_length=100, default='abcde')
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(default=timezone.now)
    # slug = models.SlugField(unique=True, db_index=True)
    
    # author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    
    # tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")