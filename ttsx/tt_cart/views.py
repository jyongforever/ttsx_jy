# -*- coding:utf-8 -*-
from django.http import JsonResponse
from django.shortcuts import render

from models import CartInfo
from tt_user.models import UserInfo
from tt_user.user_decorators import user_login


def add(request):
    dict = request.GET
    gid = int(dict.get('gid',''))
    count = int(dict.get('count'))

    uid = int(request.session.get('uid'))

    carts = CartInfo.objects.filter(user_id=uid,goods_id=gid)
    if len(carts)==0:
        cart = CartInfo()
        cart.user_id=request.session.get('uid')
        cart.goods_id=int(gid)
        cart.count=count
        cart.save()
    else:
        cart = carts[0]
        cart.count+=count
        cart.save()


    return JsonResponse({'isok':1})


@user_login
def cart(request):
    cart_list = CartInfo.objects.filter(user_id=request.session['uid'])
    context = {'title':'购物车','cart_list':cart_list}
    return render(request,'tt_cart/cart.html',context)


def del_cart(request):
    try:
        cid = request.GET.get('cid')
        cart = CartInfo.objects.get(pk=cid)
        cart.delete()
        return JsonResponse({'isdelete':1})
    except:
        return JsonResponse({'isdelete':0})


def cart_count(request):
    count = 0
    if request.session.has_key('uid'):
        uid = int(request.session.get('uid'))
        count = len(CartInfo.objects.filter(user_id=uid))
    else:
        count = 0
    return JsonResponse({'count':count})


def add_count(request):
    dict = request.GET
    add_id = dict.get('add_id')
    cart = CartInfo.objects.get(pk=add_id)
    cart.count += 1
    cart.save()
    return JsonResponse({'isok':1})


def minus_count(request):
    dict = request.GET
    minus_id = dict.get('minus_id')
    cart = CartInfo.objects.get(pk=minus_id)
    cart.count -= 1
    cart.save()
    return JsonResponse({'isok': 1})


def change_count(request):
    dict = request.GET
    change_id = dict.get('change_id')
    count = int(dict.get('count'))
    cart = CartInfo.objects.get(pk=change_id)
    cart.count = count
    cart.save()
    return JsonResponse({'isok': 1})



