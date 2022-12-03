from django.shortcuts import render,redirect
from app1.models import Post
from django.views.generic import DetailView,DeleteView,ListView,UpdateView
from .forms import PostForm
''' using CBV '''
# class PostListView(ListView):
#     model =  Post
#     template_name = ' index.html'
    






''' using FBV '''
def index(request):
    context = {}

    context["dataset"] = Post.objects.all()
       
    return render(request, "index.html", context) 


def detail_view(request, id):
    context = {}
        
    context["dataset"] = Post.objects.get(id=id)
        
    return render (request, 'detail.html', context)
    


def Create_post(request):
    template = 'create_post.html'
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {"form": form}
    return render(request, template, context)

def author(request):
    context = {}

    context["dataset"] = Post.objects.all()
    return render(request, 'author.html',context)



def post(request):
    text = {"data":"jjfh"}
    return render(request, 'post.html',context=text)
