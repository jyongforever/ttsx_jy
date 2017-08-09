# coding:utf-8
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from hashlib import sha1
from models import UserInfo
from tt_goods.models import GoodsInfo
from tt_order.models import OrderInfo, OrderDetailInfo
from tt_user.user_decorators import user_login
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


# Create your views here.


def register(request):
    return render(request, 'tt_user/register.html', {'title': '注册', 'top': '0'})


def register_username(request):
    # 从数据库ttsx的UserInfo表中获取数据
    user = UserInfo.objects.all()
    # print user
    # 定义空列表，用来存储用户名数据
    list2 = []
    # 遍历列表将用户名添加到列表list2中
    for temp in user:
        list2.append(temp.uname)
    # print(list2)
    # 返回JsonResponse对象，用于js中获取数据
    return JsonResponse({'list': list2})


def register_handle(request):
    # 获取注册页面表单提交的数据
    dict = request.POST
    uname = dict.get('user_name')
    upwd = dict.get('pwd')
    upwd2 = dict.get('cpwd')
    uemail = dict.get('email')
    if upwd != upwd2:
        return redirect('/user/register/')
    # 加密并将数据储存到数据库中
    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd_sha1
    user.uemail = uemail
    user.save()
    return redirect('/user/login/')


def login(request):
    uname = ''
    # 获取cookie，如果cookie中有uname，则在用户名输入框自动填写号cookie中存储的用户名
    if request.COOKIES.has_key('uname'):
        uname = request.COOKIES['uname']
    return render(request, 'tt_user/login.html', {'title': '登录', 'uname': uname, 'top': '0'})


def login_check(request):
    # 获取登录页面表单提交的数据
    dict = request.POST
    check = dict.get('check')
    uname = dict.get('username')
    upwd = dict.get('pwd')
    # print(uname)
    # print(upwd)
    # 加密
    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()
    # top为0布加载顶部信息模板
    context = {'title': '登录', 'uname': uname, 'upwd': upwd, 'top': '0'}
    # 从数据库过滤获取uname=uname的数据对象
    users = UserInfo.objects.filter(uname=uname)
    if len(users) == 0:
        # 用户名错误
        context['name_error'] = '1'
        return render(request, 'tt_user/login.html', context)
    else:
        if users[0].upwd == upwd_sha1:  # 登录成功
            # 记录当前登录的用户
            request.session['uid'] = users[0].id
            request.session['uname'] = uname
            # 重定向，即从哪来，回哪去
            path = request.session.get('url_path', '/')
            response = redirect(path)
            # 记住用户名
            if check == 'on':
                response.set_cookie('uname', uname, max_age=7 * 24 * 60 * 60)
            else:
                response.set_cookie('uname', '', max_age=-1)
            return response
        else:
            # 密码错误
            context['pwd_error'] = '1'
            return render(request, 'tt_user/login.html', context)


def logout(request):
    # 清空session数据，忘记登录状态
    request.session.flush()
    return redirect('/user/login/')


def islogin(request):
    result = 0
    if request.session.has_key('uid'):
        result = 1
    return JsonResponse({'islogin':result})


# 装饰器用来判断用户是否登录，未登录则转到登录页面
@user_login
def info(request):
    glist=[]
    try:
        if request.COOKIES.has_key('rec'):
            rec = request.COOKIES['rec']
            list_rec = rec.split('-')
            for gid in list_rec:
                glist.append(GoodsInfo.objects.get(pk=int(gid)))
            else:
                glist.reverse()
    except:
        pass

    user = UserInfo.objects.get(pk=request.session['uid'])
    context = {'title': '用户中心', 'uname': user.uname, 'uemail': user.uemail,'list_rec':glist}
    return render(request, 'tt_user/info.html', context)


@user_login
def order(request):
    uid = request.session.get('uid')
    order_list = OrderInfo.objects.filter(user_id=uid).order_by('-odate')
    pindex = int(request.GET.get('page','1'))
    print(pindex)
    paginator = Paginator(order_list,2)
    if pindex<=0:
        pindex = 1
    if pindex >= paginator.num_pages:
        pindex=paginator.num_pages
    page = paginator.page(pindex)
    context = {'title':'用户订单','page':page,'pindex':pindex}
    return render(request, 'tt_user/order.html', context)

@user_login
def site(request):
    user = UserInfo.objects.get(pk=request.session['uid'])
    # 判断当前页面发出POST请求时，记录信息到相应的用户数据中，并展现在页面上
    if request.method == 'POST':
        post = request.POST
        user.ushou = post.get('ushou')
        user.uaddr = post.get('uaddress')
        user.uphone = post.get('uphone')
        user.save()
    context = {'title': '收货地址', 'user': user}
    return render(request, 'tt_user/site.html', context)


