from django.shortcuts import render
from .models import Post
from django.views.generic import ListView


# Create your views here.

def index(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def galery(request):
    return render(request, 'galery.html')


def specialists(request):
    return render(request, 'specialists.html')


def sales(request):
    context = {
        'posts': Post.objects.all().order_by('-data'),
        'conteudo': Post.objects.values_list('conteudo'),
    }
    return render(request, 'sales.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'sales.html'
    context_object_name = 'posts'


def events(request):
    return render(request, 'events.html')
