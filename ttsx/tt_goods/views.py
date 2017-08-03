# coding=utf-8
from django.core.paginator import Paginator
from django.shortcuts import render
from models import TypeInfo, GoodsInfo


# Create your views here.
def index(request):
    '''
    模板中需要的数据包括：
    1、分类信息
    2、当前分类最新的四个商品
    3、当前分类人气最高的三个商品
    共6个分类，所以会有6组信息
    list=[{type:,list_new:,list_click:},{type:,list_new:,list_click:}...]
    '''
    type_list = TypeInfo.objects.all()
    list = []
    for typeinfo in type_list:
        list.append({'type': typeinfo,
                     'list_new': typeinfo.goodsinfo_set.order_by('-id')[0:4],
                     'list_click': typeinfo.goodsinfo_set.order_by('-gclick')[0:3]
                     })
    context = {'title': '首页', 'cart': 1, 'list': list}
    return render(request, 'tt_goods/index.html', context)


def list_goods(request, type_id, page_index):
    # 获取相应页面种类的商品类对象
    typeinfo = TypeInfo.objects.get(pk=type_id)
    # 获取当前页面商品类的两个最新商品
    list_new = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    # 获取当前页面商品类的所有商品对象
    list = typeinfo.goodsinfo_set.order_by('-id')
    # print(list)
    paginator = Paginator(list, 3)
    page_index = int(page_index)
    if page_index <= 0:
        page_index = 0
    if page_index >= paginator.num_pages:
        page_index = paginator.num_pages

    page = paginator.page(page_index)
    plist = paginator.page_range
    max_page = paginator.num_pages
    if max_page > 5:
        if page_index <= 2:
            plist = range(1, 6)
        elif page_index >= max_page - 1:
            plist = range(max_page - 4, max_page + 1)
        else:
            plist = range(page_index - 2, page_index + 3)

    context = {'title': '列表页', 'cart': '1', 'type': typeinfo, 'list_new': list_new, 'page': page, 'plist': plist}
    return render(request, 'tt_goods/list.html', context)


def list_detail(request):
    return render(request, 'tt_goods/detail.html')
