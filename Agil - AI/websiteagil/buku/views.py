from django.shortcuts import render
from . models import post
# Create your views here.


def index(request):
    postingan= post.objects.all()

    context={'TampungPostingan':postingan,}
  
    return render(request,'buku/index.html',context)