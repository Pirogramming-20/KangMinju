from django.shortcuts import render, HttpResponse

# Create your views here.
def review_list(request):
    return render(request, 'review_list.html')
