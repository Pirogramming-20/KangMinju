from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# Create your views here.
def main(request) :
    posts = Post.objects.all()
    sort_by = request.GET.get('sort_by')
    
    if sort_by == 'interest':
        posts = sorted(posts, key=lambda post: int(post.interest), reverse=True) 
    # if sort_by == 'newest':
    #     posts = sorted(posts, key=lambda post: int(post.newest)) 
    # elif sort_by == 'written':
    #     posts = sorted(posts, key=lambda post: int(post.written))   
    else:
        posts = posts.order_by('title') 
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
    return redirect('posts:main')

def detail(request, pk):
    post = Post.objects.get(id=pk)
    ctx = {'post' : post}
    return render(request, 'posts/post_detail.html', ctx)

def delete(request, pk):
    if request.method == 'POST':
        Post.objects.get(id=pk).delete()
    return redirect('posts:main')

def update(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'GET':
        form = PostForm(instance=post)
        ctx = {'form':form, 'pk':pk}
        return render(request, 'posts/post_update.html', ctx)
    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
        form.save()
    return redirect('posts:detail', pk)