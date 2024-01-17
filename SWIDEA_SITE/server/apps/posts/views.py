from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.http import JsonResponse
# Create your views here.
def main(request) :
    posts = Post.objects.all()
    sort = request.GET.get('sort_by')
    
    if sort == 'title':
        posts = posts.order_by('title')
    elif sort == 'pk':
        posts= posts.order_by('pk')
    elif sort == 'updated_date':
        posts = posts.order_by('-pk')
    elif sort == 'interest':
        posts = posts.order_by('-interest')
    elif sort == 'star':
        posts = posts.order_by('-star')
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

def interest(request):
    if request.method == 'POST':
        pk = request.POST.get('pk', None)
        check = request.POST.get('check', None)
        post = get_object_or_404(Post, id=pk)

        if check == 'increase':
            post_interest = post.interest + 1
        else:
            post_interest = post.interest - 1

        post.interest = post_interest
        post.save()

        return JsonResponse({'interest': post_interest})
    else:
        pass
    
def star_list(request, pk):
    star_toggle = Post.objects.get(id=pk)
    if star_toggle.star:
        star_toggle.star = False
    else:
        star_toggle.star = True
    star_toggle.save()
    return redirect('posts:main')

def star_detail(request, pk):
    star_toggle = Post.objects.get(id=pk)
    if star_toggle.star:
        star_toggle.star = False
    else:
        star_toggle.star = True
    star_toggle.save()
    return redirect('posts:detail', pk)
