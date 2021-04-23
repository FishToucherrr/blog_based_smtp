from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post,User,Comment,Category,Tag,Post_tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import markdown
from django.contrib import auth

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-created_time')
    search=None
    message=None
    if request.method == "POST":
        search = request.POST.get('search')
        de = request.POST.get('de')

        try:
            if de:
                obj=Post.objects.get(id=de)
                if request.user.is_superuser or request.user == obj.author:
                    obj.delete()
                    message="删除成功！"
                else:
                    message="又不是管理员，又不是作者，你想干啥？-_-"
        except:
            message="建议不要刷新，已经删除过了"
        
        posts = Post.objects.all().order_by('-created_time')
        if search:
            posts=Post.objects.filter(title__icontains=search).order_by('-created_time')
    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        post_list = paginator.page(paginator.num_pages)
    
    return render(request,'blog/index.html',context={'post_list':post_list,'search':search,'message':message
    })

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    post.body=md.convert(post.body)
    post.toc=md.toc
    post.increase_views()

    message=None
    
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            try:
                comment = Comment(name=request.user,text=text,post=post)
                comment.save()
            except:
                message="你是不是没登录？-_-"
    
    comment_list = Comment.objects.filter(post=post
                                    ).order_by('-created_time')

    return render(request, 'blog/detail.html', context={'post': post,'comment_list':comment_list,'message':message})

def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def tag(request,pk):
    t = get_object_or_404(Tag, pk=pk)
    post_tag_list = Post_tag.objects.filter(tag=t)
    post_list=[]
    for post_tag in post_tag_list:
        post_list.append(post_tag.post)
    return render(request, 'blog/index.html', context={'post_list': post_list})

def login(request):
    if request.method == "POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        message = "所有字段都必须填写！"
        if username and password:
            username = username.strip()
            try:
                user = auth.authenticate(username=username,password=password)
                if(user):
                    auth.login(request,user)
                    message="登录成功！"
                    return HttpResponseRedirect('/')
                else:
                    message="用户名或密码有误！"
            except:
                message="用户名或密码有误！"
        
        return render(request,'blog/login.html',{"message":message})
    return render(request,'blog/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')        
        password = request.POST.get('password') 
        message = "所有字段都必须填写！"       
        #username, email, password=None, **extra_fields
        if username and password and email:
            try:        
                user = User.objects.create_user(username=username,email=email,password=password)        
                user.save()       
                if user:            
                    auth.login(request, user)
                message = "注册成功！" 
                return HttpResponseRedirect('/')
            except:
                message="用户名已存在！"
        return render(request,'blog/signup.html',{"message":message})
    return render(request,'blog/signup.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def blog(request):
    category_list = Category.objects.all()
    if request.method == "POST":
        author=request.user
        cate_name=request.POST.get('category')
        title=request.POST.get('title')
        body=request.POST.get('body')
        excerpt=request.POST.get('excerpt')
        message="除摘要外都须填写！"
        if title and body and cate_name:
            category = get_object_or_404(Category, name=cate_name)
            post = Post(author=author,title=title,body=body,excerpt=excerpt,category=category)
            post.save()
            return HttpResponseRedirect('/')
        else:
            return render(request,'blog/blog.html',context={'category_list':category_list,'message':message
    })
    return render(request,'blog/blog.html',context={'category_list':category_list
    })

def profile(request,name):
    message=None
    if request.method == "POST":
        search = request.POST.get('search')
        de = request.POST.get('de')

        try:
            if de:
                obj=Post.objects.get(id=de)
                obj.delete()
                message="删除成功！"
            else:
                message="我怀疑你登录状态不对劲 -_-"
        except:
            message="建议不要刷新，已经删除过了"
    post_list=Post.objects.filter(author=request.user).order_by('-created_time')
    return render(request,'blog/profile.html',context={'post_list':post_list,'message':message
    })


