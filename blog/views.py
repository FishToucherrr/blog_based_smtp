from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Email,Category, Friends
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth
from .sklab import *
# Create your views here.
def drafts(request):
    mails = Email.objects.filter(category__name="草稿箱").order_by('-created_time')
    search=None
    message=None
    if request.method == "POST":
        search = request.POST.get('search')
        de = request.POST.get('de')

        try:
            if de:
                obj=Email.objects.get(id=de)  
                obj.delete()
                message="删除成功！"
        except:
            message="建议不要刷新，已经删除过了"
        
        mails = Email.objects.all().order_by('-created_time')
        if search:
            mails=Email.objects.filter(title__icontains=search).order_by('-created_time')
    paginator = Paginator(mails,10)
    page = request.GET.get('page')
    
    try:
        mail_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        mail_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        mail_list = paginator.page(paginator.num_pages)
    
    return render(request,'blog/index.html',context={'mail_list':mail_list,'search':search,'message':message
    })

def sent(request):
    mails = Email.objects.filter(category__name="已发送").order_by('-created_time')
    search=None
    message=None
    if request.method == "POST":
        search = request.POST.get('search')
        de = request.POST.get('de')

        try:
            if de:
                obj=Email.objects.get(id=de)  
                obj.delete()
                message="删除成功！"
        except:
            message="建议不要刷新，已经删除过了"
        
        mails = Email.objects.all().order_by('-created_time')
        if search:
            mails=Email.objects.filter(title__icontains=search).order_by('-created_time')
    paginator = Paginator(mails,10)
    page = request.GET.get('page')
    
    try:
        mail_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        mail_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        mail_list = paginator.page(paginator.num_pages)
    
    return render(request,'blog/index.html',context={'mail_list':mail_list,'search':search,'message':message
    })


def mail(request):
    category_list = Category.objects.all()
    receiver_list = Friends.objects.all()
    if request.method == "POST":
        cate_name=request.POST.get('category')
        title=request.POST.get('title')
        body=request.POST.get('body')
        receiver=request.POST.getlist('receiver')
        message="都必填"
        if title and body and cate_name and receiver:
            category = get_object_or_404(Category, name=cate_name)
            email = Email(title=title,body=body,category=category)
            email.save()
            if cate_name=="已发送":
                send_email(body,receiver,title)
            return HttpResponseRedirect('/')
        else:
            return render(request,'blog/blog.html',context={'category_list':category_list,'message':message,'receiver_list':receiver_list
    })
    return render(request,'blog/blog.html',context={'category_list':category_list,'receiver_list':receiver_list
    })


def edit(request, pk):
    mail = get_object_or_404(Email, id=pk)
    category_list = Category.objects.all()
    receiver_list = Friends.objects.all()
    message=None

    if request.method == "POST":
        cate_name=request.POST.get('category')
        title=request.POST.get('title')
        body=request.POST.get('body')
        receiver=request.POST.getlist('receiver')
        message="nothing"
        if title and body and cate_name:
            category = get_object_or_404(Category, name=cate_name)
            email = Email(title=title,body=body,category=category)
            email.save()
            if cate_name=="已发送":
                send_email(body,receiver,title)
            return HttpResponseRedirect('/')
    return render(request,'blog/edit.html',context={'category_list':category_list,'message':message,'mail':mail,'receiver_list':receiver_list
    })


