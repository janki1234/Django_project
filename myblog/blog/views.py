from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BlogForm
from .models import Blog
# Create your views here.


def blog_list(request):
	blog=Blog.objects.all()
	context={'blogs':blog}
	return render(request,'index.html',context)

def blog_view(request,id):
	blog=Blog.objects.get(id=id)
	context={'blog':blog}
	return render(request,'blog_view.html',context)

def blog_create(request):
	form=BlogForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/')
		
	context={"form":form}
	return render(request,'blog_create.html',context)

def blog_update(request,id):
	id=Blog.objects.get(id=id)
	form=BlogForm(request.POST or None,instance=id)
	if form.is_valid():
		form.save()
		return redirect('/')
	
	context={"form":form}
	return render(request,'blog_update.html',context)

def blog_delete(request,id):
	blog=Blog.objects.get(id=id)
	blog.delete()
	return redirect('/')

