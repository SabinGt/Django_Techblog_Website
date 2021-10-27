from django.shortcuts import HttpResponse,render,redirect
from blog.models import Blog,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from blog.forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

def about(request):
    return render(request,'about.html')




def home(request):
    data = Blog.objects.all()  # SELECT * FROM 'blog'
    category = Category.objects.all()
    context = {
        'blog': data,
        'cat':category
    }
    return render(request, 'home.html', context)



@login_required(login_url='login')
def dashboard(request):
    data = Blog.objects.all()
    category = Category.objects.all()
    context = {

        'blog':data,
        'cat': category
    }
    return render(request,'dashboard.html',context)

@login_required(login_url='login')
def create_post(request):
    form = BlogForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS,"Created successfully")
        return redirect('dashboard')
    context = {
        'form':form
    }
    return render(request,'create_post.html',context)

@login_required(login_url='login')
def edit_post(request,id):
    data = Blog.objects.get(pk=id)
    form = BlogForm(request.POST or None,request.FILES or None,instance=data)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS,"update successfully")
        return redirect('dashboard')
    context = {
        'form':form
    }
    return render(request,'edit_post.html',context)

@login_required(login_url='login')
def delete_post(request,id):
    b = Blog.objects.get(pk=id)
    b.delete()
    messages.add_message(request,messages.SUCCESS,"successfully deleted")
    return redirect('dashboard')
