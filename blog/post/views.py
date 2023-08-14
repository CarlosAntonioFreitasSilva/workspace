from django.shortcuts import render

nome = {"nome":"Carlos Antônio"}

# Create your views here.
def home(request):
    return render(request,'post/index.html',nome)


from .models import Post
def show_posts(request):
    data = {"postagens" : Post.objects.all()}
    return render(request, 'post/postagens.html', data)
