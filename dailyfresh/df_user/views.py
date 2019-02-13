# coding:utf-8
from django.shortcuts import render,redirect
from .models import *
import hashlib
from django.http import JsonResponse,HttpResponseRedirect
from . import user_decorator
from df_goods.models import *


def register(request):
    return render(request,'df_user/register.html')


def register_exit(request):
    gname = request.GET
    uname = gname.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})


def register_handle(request):
    post=request.POST
    uname=post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')

    if upwd != upwd2:
        return redirect('df_user/register.html')

    #jiami
    s1=hashlib.sha1()
    s1.update(upwd.encode("utf-8"))
    upwd3=s1.hexdigest()

    #
    user=UserInfo()
    user.uname=uname
    user.upwd=upwd3
    print(user.upwd)
    user.uemail=uemail
    user.save()

    return render(request,'df_user/login.html')


def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'df_user/login.html',context)


def login_handle(request):

#接收数据
    get = request.POST
    uname = get.get('username')
    upwd = get.get('pwd')
    allow = get.get('allow',0)
    cname = UserInfo.objects.filter(uname=uname)
    if len(cname) == 1:
        s1 = hashlib.sha1()
        s1.update(upwd.encode("utf-8"))
        upwd3 = s1.hexdigest()
        if upwd3 == cname[0].upwd:
            red = HttpResponseRedirect('/df_user/info/')
            if allow != 0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname',"",max_age=-1)
            request.session["user_id"] = cname[0].id
            request.session["user_name"] = cname
            return red
        else:
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': uname, 'upwd': upwd}
            return render(request,'df_user/login.html',context)

    else:
        context = {'title':'用户登录','error_name':1,'error_pwd':0,'uname':uname,'upwd':upwd}
    return render(request,'df_user/login.html',context)

def logout(request):
    request.session.flush()
    return redirect('/')

@user_decorator.login
def info(request):
    email_addr=UserInfo.objects.get(id=request.session["user_id"]).uemail
    #最近浏览
    goods_ids=request.COOKIES.get('goods_ids','')
    goods_ids1=goods_ids.split(',')
    goods_list=[]
    # for goods_id in goods_ids1:
    #     goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))

    uname=UserInfo.objects.get(id=request.session["user_id"]).uname
    context={"title":'用户中心',
             "uname":uname,
             "email_addr":email_addr,
             'user_name':request.session['user_name'],
             'page_name':1,
              'goods_list':goods_list
             }
    return render(request,"df_user/user_center_info.html",context)

@user_decorator.login
def site(request):
    user = UserInfo.objects.get(id=request.session["user_id"])
    # print("11111")
    # t=request.method
    # print(t)
    if request.method == "POST":
        post = request.POST
        user.ushou = post.get("ushou")
        user.uaddress = post.get("uaddress")
        user.uyoubian = post.get("uyoubian")
        user.uphone = post.get("uphone")
        # print("22222")
        user.save()
    context = {"title":'用户地址',
               "user":user}
    return render(request,"df_user/user_center_site.html",context)

@user_decorator.login
def order(request):

    context = {"title":'用户订单'}
    return render(request,"df_user/user_center_order.html",context)


