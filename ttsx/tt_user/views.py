# coding:utf-8
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from hashlib import sha1
from models import UserInfo


# Create your views here.
def register(request):
    return render(request, 'tt_user/register.html', {'title': '注册'})


def register_username(request):
    user = UserInfo.objects.all()
    # print user
    list2 = []
    for temp in user:
        list2.append(temp.uname)
    # print(list2)
    return JsonResponse({'list':list2})


def register_handle(request):
    dict = request.POST
    uname = dict.get('user_name')
    upwd = dict.get('pwd')
    upwd2 = dict.get('cpwd')
    uemail = dict.get('email')
    if upwd != upwd2:
        return redirect('/user/register/')
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
    uname=''
    if request.COOKIES.has_key('uname'):
        uname=request.COOKIES['uname']
    return render(request, 'tt_user/login.html', {'title': '登录','uname':uname})


def login_userinfo(request):
    user = UserInfo.objects.all()
    # print user
    list2 = []
    for temp in user:
        list2.append([temp.uname,temp.upwd])
    # print(list2)
    return JsonResponse({'list':list2})


def login_check(request):

    dict = request.POST
    check = dict.get('check')
    uname = dict.get('username')
    # print(check)
    if check == 'on':
        response = render(request,'tt_user/index.html')
        response.set_cookie('uname',uname)
        print(check)
    return response
    # uname = dict.get('username')
    # upwd = dict.get('pwd')
    # user = UserInfo.objects.all()
    # s1 = sha1()
    # s1.update(upwd)
    # upwd_sha1 = s1.hexdigest()
    # for temp in user:
    #     if uname==temp.uname and upwd_sha1 ==temp.upwd:
    # else:
    #     return redirect('/user/login/')


def index(request):
    return render(request, 'tt_user/index.html', {'title': '首页'})
