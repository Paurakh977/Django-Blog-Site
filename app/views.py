from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from app.models import Blog
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from app.models import BlogComments

def inp(request):
    return render(request,'inp.html')

def home(request):
    return render(request,'home.html')

def blogs(request):
    all_obj=Blog.objects.all()
    context={'obj':all_obj}
    return render(request,'blogs.html',context)

def register(request):
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        slug=request.POST['slug']
        if title and desc and slug:
            obj=Blog(title=title,desc=desc,slug=slug)
            obj.save()
            return redirect('home')
    return render(request,'register.html')

def blogpost(request, page_slug):
    ins = Blog.objects.get(slug=page_slug)   
    
    if ins:
        comment_ins = BlogComments.objects.filter(comment=ins)

    else:
        comment_ins = []

    context = {
        'obj': ins,
        'comments': comment_ins,
        
    }

    return render(request, 'blogpost.html', context)

def search(request):
    if request.method=='POST':
        query=request.POST['search']
        if query:
            if len(query)<1 or len(query)>50:
                return render(request,'error.html') 
            else :
                obj_title = Blog.objects.filter(title__icontains=query)
                obj_slug=Blog.objects.filter(slug__icontains=query)
                obj_desc=Blog.objects.filter(desc__icontains=query)
                obj=obj_title.union(obj_desc,obj_slug)
                context={'obj':obj}
                if len(obj)==0:
                    return render(request,'error.html') 
                else:

                    return render(request,'blogs.html',context)
        else: 
            return render(request,'error.html') 

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        email_validator = EmailValidator(message='Invalid email format.')
        try:
            email_validator(email)
        except ValidationError:
            messages.error(request,'The email you have chosen is invalid',extra_tags='signup')
            return redirect('home')
        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.save()
        messages.success(request,'Your Id was sucessfuly signed in!. Please login now ',extra_tags='signup')
        return redirect('home')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully logged in.", extra_tags='login')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials', extra_tags='login')
            return redirect('home')
            
def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, 'Successfully Logged Out', extra_tags='logout')
        return redirect('blog')

def postcomment(request,id):
    if request.method=="POST":
        content=request.POST['content']
        author = request.user
        comment_blog = Blog.objects.get(id=id)  # Get the blog post associated with the comment
        new_comment = BlogComments(comment=comment_blog, content=content, author=author)
        new_comment.save()
        url=f"/blogpost/{comment_blog.slug}/"
        return redirect(url)
