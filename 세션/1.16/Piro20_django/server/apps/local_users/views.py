from django.shortcuts import render, redirect
from .models import LocalUser
from .forms import LocalForm

# Create your views here.
def user_list(request):
    search_txt = request.GET.get('search_txt')
    users = LocalUser.objects.all()
    if search_txt:
        users = users.filter(name__contains = search_txt)
    ctx = {'users' : users}
    return render(request, 'users/user_list.html', ctx)

def create(request):
    if request.method == 'GET':
        form = LocalForm()
        ctx = {'form' : form}
        return render(request, 'users/user_create.html', ctx)

    form = LocalForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('users:list')

def delete(request,pk):
    if request.method == 'POST':
        LocalUser.objects.get(id=pk).delete()
    return redirect('users:list')

def update(request,pk):
    user = LocalUser.objects.get(id=pk)
    if request.method == 'GET':
        form = LocalForm(instance=user)
        ctx = {'form': form, 'pk': pk}
        return render(request, 'users/user_update.html', ctx)
    form = LocalForm(request.POST, instance=user)
    if form.is_valid():
        form.save()
    return redirect('users:list') #users:list는 pk를 안받음. 내가 억지로 pk 보내니까 오류남