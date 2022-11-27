from django.shortcuts import render
from app1.models import Post
from django.views.generic import DetailView,DeleteView,ListView,UpdateView

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
    





def author(request):
    text = {"data":"jjfh"}
    return render(request, 'author.html',context=text)



def post(request):
    text = {"data":"jjfh"}
    return render(request, 'post.html',context=text)
