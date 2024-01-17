from django.shortcuts import render, redirect
from .models import DevTool
from .forms import DevForm
# Create your views here.
def devtool_list(request):
    devtools = DevTool.objects.all()
    ctx = {'devtools' : devtools}
    return render(request, 'devtools/devtool_list.html', ctx)

def create(request):
    if request.method == 'GET':
        form = DevForm()
        ctx = {'form' : form}
        return render(request, 'devtools/devtool_create.html', ctx)

    form = DevForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('devtools:list')

def detail(request, pk):
    devtool = DevTool.objects.get(id=pk)
    ctx = {'devtool' : devtool}
    return render(request, 'devtools/devtool_detail.html', ctx)

def delete(request,pk):
    if request.method == 'POST':
        DevTool.objects.get(id=pk).delete()
    return redirect('devtools:list')

def update(request,pk):
    devtool = DevTool.objects.get(id=pk)
    if request.method == 'GET':
        form = DevForm(instance=devtool)
        ctx = {'form': form, 'pk': pk}
        return render(request, 'devtools/devtool_update.html', ctx)
    form = DevForm(request.POST, instance=devtool)
    if form.is_valid():
        form.save()
    return redirect('devtools:detail', pk) #users:list는 pk를 안받음. 내가 억지로 pk 보내니까 오류남