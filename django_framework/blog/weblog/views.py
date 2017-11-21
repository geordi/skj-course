from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import Post, Comment
from .forms import CommentForm

def index(request):
    posts = Post.objects.all()

    return render(request, 'weblog/index.html', {'posts': posts})

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)

    comment_form = CommentForm()

    return render(request, 'weblog/post.html', {'post': post, 'comments': comments,
                                                'comment_form': comment_form})

def addcomment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        #print(request.POST)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_body = comment_form.cleaned_data['body']
            comment = Comment(post=post, body=comment_body)
            comment.save()

            return redirect('post', post_id=post.id)

def search(request):
    return render(request, 'weblog/search.html', {})

def livesearch(request, word, sid):
    posts = Post.objects.filter(title__icontains=word)

    if len(posts) > 0:
        response = ''
        for p in posts:
            response += '<a href="' + reverse('post', args=(p.id,)) + '">{}</a><br/>'.format(p.title)
    else:
        response = 'no suggestion'

    return HttpResponse(response)
