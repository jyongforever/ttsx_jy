#coding=utf-8
from django.template import Library
register=Library()
@register.filter

def page_list(page):
    plist = page.paginator.page_range
    max_page = page.paginator.num_pages
    page_index = page.number
    if max_page > 5:
        if page_index <= 2:
            plist = range(1, 6)
        elif page_index >= max_page - 1:
            plist = range(max_page - 4, max_page + 1)
        else:
            plist = range(page_index - 2, page_index + 3)
    return plist