from django.shortcuts import render
from .models import Post, Comment

def home(request):
    posts = Post.objects.all()
    author_stats = []

    for post in posts:
        comments = Comment.objects.filter(post=post)
        comments_count = comments.count()
        long_comments_count = sum(1 for comment in comments if len(comment.text) >= 5)

        author_stats.append({
            'post': post,
            'comments_count': comments_count,
            'long_comments_count': long_comments_count
        })

    return render(request, 'home.html', {'author_stats': author_stats})
