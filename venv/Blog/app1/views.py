from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from app1.models import Post
from django.views.generic import UpdateView
from .forms import PostForm,UpdatePostForm,UserFormCreation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate ,login,logout
from django.urls import reverse
# login decerator
from django.contrib.auth.decorators import login_required


''' using CBV '''
# class PostListView(ListView):
#     model =  Post
#     template_name = ' index.html'


# update the post using class base views
class Updatepost(UpdateView):
    model = Post
    form_class = UpdatePostForm
    success_url ="/"
    template_name = 'update_post.html'    






''' using FBV '''

#  fuction of the home page 
def index(request):
    context = {}

    context["dataset"] = Post.objects.all().order_by('-id').values()
       
    return render(request, "index.html", context) 

# fucn of register page
def registerpage(request):
    
    if request.method == "POST":
        form = UserFormCreation(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "user/login.html")
            
    else:
        form = UserFormCreation()
    context = {"form":form}
    return render(request,'user/register.html',context)

# fucn of logout page
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect ("index")
    context ={}  
    return render(request,'user/login.html',context)

def logoutuser(request):
    logout(request)
    return redirect('login')

# fucn that shows as the detail of the post
def detail_view(request, id):
    context = {}
    context["dataset"] = Post.objects.get(id=id)
    
    return render (request, 'detail.html', context)
  
  
@login_required(login_url='login')
# use this fucn to create a new post
def Create_post(request):
    template = 'create_post.html'
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {"form": form}
    return render(request, template, context)


@login_required(login_url='login')
# use this fucn to delete a new post
def delete_post(request, id):
    template = "delete_post.html"
    context = {}
    context["dataset"] = Post.objects.get(id=id)
    obj = get_object_or_404(Post, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, template, context)


# like post function
@login_required(login_url='login')
def like_post(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
    else:
        post.like.add(request.user)

    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))

# author page
def author(request):
    context = {}

    context["dataset"] = Post.objects.all()
    return render(request, 'author.html',context)



def post(request):
    text = {"data":"jjfh"}
    return render(request, 'post.html',context=text)
