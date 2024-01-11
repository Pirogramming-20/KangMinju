from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import *
# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }
    return render(request, 'posts_list.html', context)

def posts_read(request, pk):
    post = get_object_or_404(Post, id=pk)

    # lt = less than gt = greater than, order_by('-id') -> 역순 (내림차순)중 인덱스 0번
    try:
        previous_post_id = Post.objects.filter(id__lt=pk).order_by('-id')[0].id
    except IndexError:
        previous_post_id = None 

    try:
        next_post_id = Post.objects.filter(id__gt=pk).order_by('id')[0].id
    except IndexError:
        next_post_id = None 

    comments = Comment.objects.filter(post_id=pk)

    context = {
        "post": post,
        "previous_post_id": previous_post_id,
        "next_post_id": next_post_id,
        "comments": comments,
    }
    return render(request, "posts_read.html", context)
    
# create 페이지로 갔을 때 페이지를 띄워주는 함수
def posts_create (request) :
    if request.method == "POST" :
        Post.objects.create(
            title = request.POST["title"],
            user = request.POST["user"],
            content = request.POST["content"],
        )
        return redirect("/posts")
    return render(request, "posts_create.html")

# 작성 완료를 눌렀을 때 서버 저장해주는 함수    
# def posts_create_final (request) :
#     if request.method == "POST" :
#         Post.objects.create(
#             title = request.POST["title"],
#             user = request.POST["user"],
#             content = request.POST["content"],
#         )
#     #redirect -> 작동을 끝내면 /posts로 돌아가라...
#     return redirect("/posts")

def posts_update (request, pk) :
    post = Post.objects.get(id=pk)
    if request.method == "POST" :
        post.title = request.POST["title"]
        post.user = request.POST["user"]
        post.content = request.POST["content"]
        # post.save()를 써야 DB에 있는 값이 바뀜
        post.save()
        return redirect(f"/posts/{pk}")
    context = {
        "post" : post
    }
    return render(request, "posts_update.html", context)

def posts_delete (request, pk) :
    if request.method == "POST":
        post = Post.objects.get(id = pk)
        post.delete()
    return redirect("/posts")

def comments_create(request, post_id):
    Comment.objects.create(
        post_id = post_id,
        content = request.POST["content"]
    )
    return redirect(f"/posts/{post_id}")