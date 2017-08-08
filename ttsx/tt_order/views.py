# -*- coding:utf-8 -*-
import datetime
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from tt_cart.models import CartInfo
from tt_order.models import OrderInfo, OrderDetailInfo
from tt_user.models import UserInfo


def list(request):
    dict = request.POST
    cid = dict.getlist('cid')
    cart_list = CartInfo.objects.filter(pk__in=cid)
    uid = request.session.get('uid')
    user = UserInfo.objects.get(pk=uid)
    context={'title':'订单页面','user':user,'cart_list':cart_list}
    return render(request, 'tt_order/list.html',context)


def handle(request):
    sid = transaction.savepoint()
    try:
        dict = request.POST
        cids = dict.getlist('cid')
        addr = dict.get('addr')
        uid = request.session.get('uid')
        '''
        创建订单主表对象
        判断商品库存是否足够
        遍历购物车信息，创建订单详表
        将商品数量减少
        '''
        order=OrderInfo()
        order.oid=datetime.datetime.now().strftime('%Y%m%d%H%M%S')+str(uid)
        order.user_id=uid
        order.ototal=0
        order.oaddress=addr
        order.save()

        cart_list = CartInfo.objects.filter(pk__in=cids)
        total=0
        for cart in cart_list:
            # 库存不够，放弃购买
            if cart.count > cart.goods.gkucun:
                print('111')
                transaction.savepoint_rollback(sid)
                print('222')
                return redirect('/cart/')
            # 库存足够，创建订单详表
            else:
                detail = OrderDetailInfo()
                detail.goods=cart.goods
                detail.order=order
                detail.price=cart.goods.gprice*cart.count
                detail.count=cart.count
                detail.save()
                # 修改库存
                goods=cart.goods
                goods.gkucun-=cart.count
                goods.save()
                # 计算总价
                total+=detail.price
                # 删除购物侧
                cart.delete()
        else:
            # 保存总价
            order.ototal=total
            order.save()
            transaction.savepoint_commit(sid)
            return redirect('/user/order/')

    except:

        transaction.savepoint_rollback(sid)
        return redirect('/cart/')