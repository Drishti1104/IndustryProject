from datetime import datetime
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View

from .models import Post, Author 
from .forms import CommentForm, PostForm

# Create your views here.

def CreateBlogPost(request):
    author = Author.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        # image = request.POST.get('image')
        content = request.POST.get('content')
        author = request.POST.get('author')
        # date = datetime.today()
        form = PostForm(request.FILES)
        if form.is_valid():
            form.save()
    
            post = Post(
                title=title,
                # image=image,
                content=content,
                author=author,
                date=datetime.today(),
            )
            post.save()
            return redirect('blog:posts-page')
    return render(request, 'blog/create-post.html', {
        'author': author,
        'post_form': PostForm(),
    })

class StartingPageView(ListView):
    template_name = "blog/blog-home.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
    
# def starting_page(request):
#     latest_posts = Post.objects.all().order_by('-date')[:3]
#     return render(request, 'blog/index.html', {
#         "posts": latest_posts
#     })

class AllPostsView(ListView):
    template_name = "blog/blog-all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

# def posts(request):
#     all_posts = Post.objects.all().order_by('-date')
#     return render(request, 'blog/all-posts.html', {
#         "all_posts": all_posts
#     })

class SinglePostView(View):
    # def is_stored_post(self, request, post_id):
    #     stored_posts = request.session.get("stored_posts")
    #     if stored_posts is not None:
    #         is_saved_for_later = post_id in stored_posts
    #     else:
    #         is_saved_for_later = False

    #     return is_saved_for_later

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        
        context = {
            "post": post,
            # "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            # "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/blog-post.html", context)

    def post(self, request, pk):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(pk=pk)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[pk]))
        
        context = {
            "post": post,
            # "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            # "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/blog-post.html", context) 

# class ReadLaterView(View):
#     def get(self, request):
#         stored_posts = request.session.get("stored_posts")
#         context = {}

#         if stored_posts is None or len(stored_posts) == 0:
#             context["posts"] = []
#             context["has_posts"] = False
#         else:
#             posts = Post.objects.filter(id__in=stored_posts)
#             context["posts"] = posts
#             context["has_posts"] = True
        
#         return render(request, "blog/stored-posts.html", context)

#     def post(self, request):
#         stored_posts = request.session.get("stored_posts")

#         if stored_posts is None:
#             stored_posts = []

#         post_id = int(request.POST["post_id"])

#         if post_id not in stored_posts:
#             stored_posts.append(post_id)
#         else:
#             stored_posts.remove(post_id)

#         request.session["stored_posts"] = stored_posts

#         return redirect("blog:starting-page")


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["post_tags"] = self.object.tags.all()
    #     context["comment_form"] = CommentForm()
    #     return context
    

# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, 'blog/post-detail.html', {
#         "post": identified_post,
#         "post_tags": identified_post.tags.all()
#     })