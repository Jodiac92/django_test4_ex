from django.shortcuts import render
from myfriend.models import Friend

# Create your views here.

def Main(request):
    return render(request, 'main.html')

def showFriends(request):
    datas = Friend.objects.all()
    return render(request, 'show.html', {'datas': datas})
    
