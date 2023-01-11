from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from app1.models import Post,Profile,Comment
from django.views.generic import UpdateView,CreateView
from .forms import PostForm,UpdatePostForm,UserFormCreation,ProfileFormUpdate,UserUpdateForm,CommentForm,PostimageForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate ,login,logout
from django.urls import reverse, reverse_lazy
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
    dataset = Post.objects.get(id=id)
    
    return render (request, 'detail.html', {"dataset":dataset})
  
  
@login_required(login_url='login')
# use this fucn to create a new post
def Create_post(request):
    img_f = PostimageForm(request.POST,request.FILES)
    form = PostForm(request.POST,request.FILES,)  # Postform from Form.py
    if request.method == 'POST':
        
        if form.is_valid() and img_f.is_valid():
            form.save()
            img_f.save()
            return redirect('index')
    context = {"form": form,
               "img_f":img_f}
    return render(request, 'create_post.html', context)


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
@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        prof_from = ProfileFormUpdate(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and prof_from.is_valid():
            user_form.save()
            prof_from.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        prof_from = ProfileFormUpdate(instance=request.user.profile)
    context = {
        'user_form':user_form,
        'prof_from':prof_from,
    }
    
    return render(request, 'profile.html',context)



def post(request):
    text = {"data":"jjfh"}
    return render(request, 'post.html',context=text)
