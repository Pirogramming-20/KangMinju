from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post, Comment
# Create your views here.
def main(request) :
    posts = Post.objects.all()
    
    ctx = {'posts' : posts }
    return render(request, 'posts/post_list.html', ctx)

def create(request) :
    if request.method == 'GET':
        form = PostForm()
        ctx = {'form': form}
        return render(request, 'posts/post_create.html', ctx)
    
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect('main')

def detail(request, pk):
    posts = Post.objects.all()
    post = Post.objects.get(id=pk)
    post_comments = Comment.objects.filter(post=post)
    ctx = {'post' : post, 'comments': post_comments, 'posts':posts}
    return render(request, 'posts/post_detail.html', ctx)

def delete(request, pk):
    if request.method == 'POST':
        Post.objects.get(id=pk).delete()
    return redirect('main')

def update(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'GET':
        form = PostForm(instance=post)
        ctx = {'form':form, 'pk':pk}
        return render(request, 'posts/post_update.html', ctx)
    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
        form.save()
    return redirect('detail', pk)

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']
    button_type = req['type']
    
    post = Post.objects.get(id=post_id)
    

    if button_type == 'like':
        post.like += 1
    else:
        post.dislike += 1
        
    post.save()
    
    return JsonResponse({'id': post_id, 'type': button_type})


@csrf_exempt
def comment(request, pk):
    if request.method == 'POST':
        req = json.loads(request.body)
        post_id = req.get('id')
        post_comment = req.get('comment')
        if post_id and post_comment:
            try:
                post = Post.objects.get(id=post_id)
                comment = Comment(post=post, content=post_comment)
                comment.save()
                return JsonResponse({'status': 'success'})
            except Post.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Post does not exist'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request data'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
        
        
@csrf_exempt
def get_comments(request, pk, comment_pk):
    if request.method == 'GET':
        comments = Comment.objects.filter(post__id=pk)
        serialized_comments = [{'id': comment.id, 'content': comment.content} for comment in comments]
        return JsonResponse(serialized_comments, safe=False)

    return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def delete_comment(request, postId, commentId, pk):
    if request.method == "POST":
        post = Post.objects.get(id = postId)
        comment = Comment.objects.filter (id = commentId, post = post)
        comment.delete()
        return JsonResponse({'message': '댓글이 삭제되었습니다.'})